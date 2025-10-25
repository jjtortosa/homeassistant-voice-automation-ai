"""Voice Automation AI integration for Home Assistant."""
from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Any

import anthropic
import voluptuous as vol
import yaml

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers import config_validation as cv

from .const import (
    API_TIMEOUT,
    ATTR_DESCRIPTION,
    ATTR_PREVIEW,
    ATTR_VALIDATE_ONLY,
    ATTR_YAML_CONTENT,
    CONF_API_KEY,
    CONF_LANGUAGE,
    CONF_MODEL,
    DEFAULT_LANGUAGE,
    DEFAULT_MODEL,
    DOMAIN,
    MAX_TOKENS,
    SERVICE_CREATE_AUTOMATION,
    SERVICE_VALIDATE_AUTOMATION,
)

_LOGGER = logging.getLogger(__name__)

# Service schemas
CREATE_AUTOMATION_SCHEMA = vol.Schema({
    vol.Required(ATTR_DESCRIPTION): cv.string,
    vol.Optional(ATTR_VALIDATE_ONLY, default=False): cv.boolean,
    vol.Optional(ATTR_PREVIEW, default=False): cv.boolean,
})

VALIDATE_AUTOMATION_SCHEMA = vol.Schema({
    vol.Required(ATTR_YAML_CONTENT): cv.string,
})


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Voice Automation AI from a config entry."""
    hass.data.setdefault(DOMAIN, {})

    # Store configuration
    hass.data[DOMAIN][entry.entry_id] = {
        CONF_API_KEY: entry.data[CONF_API_KEY],
        CONF_MODEL: entry.data.get(CONF_MODEL, DEFAULT_MODEL),
        CONF_LANGUAGE: entry.data.get(CONF_LANGUAGE, DEFAULT_LANGUAGE),
    }

    # Register services
    async def handle_create_automation(call: ServiceCall) -> dict[str, Any]:
        """Handle create_automation service call."""
        description = call.data[ATTR_DESCRIPTION]
        validate_only = call.data.get(ATTR_VALIDATE_ONLY, False)
        preview = call.data.get(ATTR_PREVIEW, False)

        try:
            # Get configuration
            config = hass.data[DOMAIN][entry.entry_id]
            api_key = config[CONF_API_KEY]
            model = config[CONF_MODEL]
            language = config[CONF_LANGUAGE]

            # Generate automation YAML with Claude
            automation_yaml = await hass.async_add_executor_job(
                _generate_automation_yaml,
                api_key,
                model,
                language,
                description,
                hass,
            )

            # Validate YAML
            try:
                automation_data = yaml.safe_load(automation_yaml)
            except yaml.YAMLError as err:
                raise HomeAssistantError(f"Invalid YAML generated: {err}") from err

            # Preview mode: return YAML without creating
            if preview:
                return {
                    "success": True,
                    "preview": True,
                    "yaml": automation_yaml,
                    "parsed": automation_data,
                }

            # Validate only mode: validate but don't create
            if validate_only:
                return {
                    "success": True,
                    "validated": True,
                    "yaml": automation_yaml,
                }

            # Create automation
            automation_id = await _add_automation_to_file(hass, automation_data)

            # Reload automations
            await hass.services.async_call("automation", "reload")

            _LOGGER.info(f"Automation created successfully: {automation_id}")

            return {
                "success": True,
                "automation_id": automation_id,
                "alias": automation_data.get("alias", "Unknown"),
            }

        except Exception as err:
            _LOGGER.error(f"Error creating automation: {err}")
            raise HomeAssistantError(f"Failed to create automation: {err}") from err

    async def handle_validate_automation(call: ServiceCall) -> dict[str, Any]:
        """Handle validate_automation service call."""
        yaml_content = call.data[ATTR_YAML_CONTENT]

        try:
            automation_data = yaml.safe_load(yaml_content)
            return {
                "success": True,
                "valid": True,
                "parsed": automation_data,
            }
        except yaml.YAMLError as err:
            return {
                "success": False,
                "valid": False,
                "error": str(err),
            }

    # Register services
    hass.services.async_register(
        DOMAIN,
        SERVICE_CREATE_AUTOMATION,
        handle_create_automation,
        schema=CREATE_AUTOMATION_SCHEMA,
    )

    hass.services.async_register(
        DOMAIN,
        SERVICE_VALIDATE_AUTOMATION,
        handle_validate_automation,
        schema=VALIDATE_AUTOMATION_SCHEMA,
    )

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    hass.data[DOMAIN].pop(entry.entry_id)
    return True


def _generate_automation_yaml(
    api_key: str,
    model: str,
    language: str,
    description: str,
    hass: HomeAssistant,
) -> str:
    """Generate automation YAML using Claude API."""

    # Get available entities for context
    entities_context = _get_entities_context(hass)

    prompt = f"""Genera una automatització de Home Assistant en format YAML per a la següent descripció:

{description}

Requisits IMPORTANTS:
- Format YAML vàlid i complet
- Inclou SEMPRE un alias descriptiu
- Inclou una description detallada
- Utilitza mode: single per defecte
- Les entitats han d'existir a Home Assistant
- Retorna NOMÉS el bloc YAML de l'automatització començant amb '- alias:', sense explicacions, sense markdown, sense ```yaml

Entitats disponibles a Home Assistant:
{entities_context}

Exemple de format exacte:
- alias: "Nom de l'automatització"
  description: "Descripció detallada"
  mode: single
  trigger:
    - platform: state
      entity_id: light.example
      to: "on"
  condition: []
  action:
    - service: light.turn_on
      target:
        entity_id: light.example

Genera l'automatització ara en {language}:"""

    # Call Claude API
    client = anthropic.Anthropic(api_key=api_key)

    try:
        message = client.messages.create(
            model=model,
            max_tokens=MAX_TOKENS,
            messages=[{
                "role": "user",
                "content": prompt
            }],
            timeout=API_TIMEOUT,
        )

        yaml_content = message.content[0].text.strip()

        # Clean up markdown code blocks if present
        if yaml_content.startswith("```"):
            lines = yaml_content.split("\n")
            yaml_content = "\n".join(lines[1:-1]) if len(lines) > 2 else yaml_content

        # Remove any remaining markdown
        yaml_content = yaml_content.replace("```yaml", "").replace("```", "").strip()

        return yaml_content

    except Exception as err:
        _LOGGER.error(f"Error calling Claude API: {err}")
        raise HomeAssistantError(f"Failed to generate automation: {err}") from err


def _get_entities_context(hass: HomeAssistant) -> str:
    """Get a summary of available entities for context."""
    states = hass.states.async_all()

    # Group by domain
    entities_by_domain = {}
    for state in states:
        domain = state.entity_id.split(".")[0]
        if domain not in entities_by_domain:
            entities_by_domain[domain] = []
        entities_by_domain[domain].append(state.entity_id)

    # Limit to most relevant domains and first 5 entities per domain
    relevant_domains = ["light", "switch", "binary_sensor", "sensor", "climate", "cover", "lock", "media_player"]

    context = []
    for domain in relevant_domains:
        if domain in entities_by_domain:
            entities = entities_by_domain[domain][:5]
            context.append(f"{domain}: {', '.join(entities)}")

    return "\n".join(context) if context else "No entities available"


async def _add_automation_to_file(hass: HomeAssistant, automation_data: dict) -> str:
    """Add automation to automations.yaml file."""

    # Get automations file path
    config_dir = hass.config.config_dir
    automations_file = Path(config_dir) / "automations.yaml"

    # Read existing automations
    if automations_file.exists():
        with open(automations_file, "r", encoding="utf-8") as f:
            existing_automations = yaml.safe_load(f) or []
    else:
        existing_automations = []

    # Ensure it's a list
    if not isinstance(existing_automations, list):
        existing_automations = [existing_automations]

    # Add new automation
    if isinstance(automation_data, list):
        new_automation = automation_data[0]
    else:
        new_automation = automation_data

    # Generate unique ID if not present
    if "id" not in new_automation:
        import time
        new_automation["id"] = str(int(time.time() * 1000))

    existing_automations.append(new_automation)

    # Write back to file
    with open(automations_file, "w", encoding="utf-8") as f:
        yaml.dump(
            existing_automations,
            f,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False,
        )

    return new_automation.get("id", "unknown")
