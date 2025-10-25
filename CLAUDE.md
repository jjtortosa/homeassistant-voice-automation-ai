# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Voice Automation AI** is a Home Assistant custom integration that allows users to create automations using natural language voice commands powered by Anthropic's Claude AI.

- **Domain:** `voice_automation_ai`
- **Type:** Home Assistant Custom Component (HACS-compatible)
- **Language:** Python 3.11+
- **Dependencies:** `anthropic>=0.40.0`

## Architecture

### Core Components

1. **`__init__.py`** - Main integration logic
   - Service handlers: `create_automation` and `validate_automation`
   - Claude API integration via `_generate_automation_yaml()`
   - Entity context gathering via `_get_entities_context()`
   - Automation file management via `_add_automation_to_file()`

2. **`config_flow.py`** - Configuration UI flow
   - API key validation against Anthropic API
   - Model selection (Sonnet, Opus, Haiku)
   - Language selection (CA, ES, EN, FR, DE)

3. **`const.py`** - Constants and configuration
   - Available models and languages
   - Service names and attributes
   - API settings (timeout, max_tokens)

### Service Flow

```
User voice command → Home Assistant Assist → Anthropic Claude
    ↓
voice_automation_ai.create_automation service
    ↓
1. Get available entities context
2. Call Claude API with description + context
3. Validate generated YAML
4. Add to automations.yaml (optional)
5. Reload automations
```

## Testing

No automated tests are currently implemented. Testing is done manually via:

1. **Developer Tools** → **Services** → `voice_automation_ai.create_automation`
2. Voice assistant integration with Anthropic Claude conversation agent
3. Home Assistant installation with the integration loaded

### Manual Testing Steps

```bash
# 1. Link/copy integration to Home Assistant config
ln -s $(pwd)/custom_components/voice_automation_ai ~/.homeassistant/custom_components/

# 2. Restart Home Assistant
# Via UI: Settings → System → Restart
# Or via CLI if using Home Assistant Core

# 3. Add integration via UI
# Settings → Devices & Services → Add Integration → Voice Automation AI

# 4. Test service call
# Developer Tools → Services → voice_automation_ai.create_automation
# Data: { "description": "Turn on lights when motion detected", "preview": true }
```

## Important Implementation Notes

### YAML Generation
- The prompt in `_generate_automation_yaml()` is currently hardcoded in **Catalan**
- The prompt should respect the `language` parameter but currently doesn't
- Generated YAML must start with `- alias:` format (list item)
- Markdown code blocks are stripped from Claude's response

### Entity Context
- Only sends first 5 entities per domain to Claude (to limit token usage)
- Focuses on relevant domains: light, switch, binary_sensor, sensor, climate, cover, lock, media_player
- Context helps Claude generate automations with valid entity IDs

### File Operations
- Automations are added to `automations.yaml` in Home Assistant config directory
- Auto-generates unique IDs using timestamp if not present
- Preserves existing automations when adding new ones
- Uses `yaml.safe_load()` and `yaml.dump()` for file operations

## Configuration

### API Settings
- **Timeout:** 30 seconds (`API_TIMEOUT`)
- **Max tokens:** 2048 (`MAX_TOKENS`)
- **Default model:** `claude-3-5-sonnet-20241022`
- **Default language:** Catalan (`ca`)

### Supported Models
- Claude 3.5 Sonnet (recommended)
- Claude 3 Opus (most powerful)
- Claude 3 Haiku (fastest, most economical)

## HACS Publishing

This integration is designed for HACS (Home Assistant Community Store):

- **Repository type:** Integration
- **Minimum HA version:** 2025.3.0
- **Installation method:** HACS custom repository
- See `PUBLICACIO_HACS.md` for publishing instructions

## Known Limitations

1. Prompt language is hardcoded to Catalan regardless of `language` setting
2. No automated tests
3. Limited entity context (5 per domain)
4. No support for editing existing automations
5. No support for scripts or scenes (only automations)

## Development Workflow

Since this is a Home Assistant integration with no build step:

1. Make code changes in `custom_components/voice_automation_ai/`
2. Restart Home Assistant to reload the integration
3. Test via Developer Tools or voice assistant
4. Check logs in Home Assistant for errors: `_LOGGER` uses domain name

### Version Updates

Update version in these files:
- `custom_components/voice_automation_ai/manifest.json` - `version` field
- Create corresponding GitHub release tag

## Code Style

- Follow Home Assistant integration conventions
- Use type hints (e.g., `dict[str, Any]`, `list[str]`)
- Use `async`/`await` for I/O operations
- Use `hass.async_add_executor_job()` for blocking calls (Claude API)
- Log errors with `_LOGGER.error()`, info with `_LOGGER.info()`
