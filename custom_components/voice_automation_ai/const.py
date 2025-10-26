"""Constants for Voice Automation AI integration."""

# Integration domain
DOMAIN = "voice_automation_ai"

# Configuration
CONF_API_KEY = "api_key"
CONF_MODEL = "model"
CONF_LANGUAGE = "language"

# Defaults
DEFAULT_MODEL = "claude-sonnet-4-5-20250929"
DEFAULT_LANGUAGE = "ca"

# Models disponibles
MODELS = {
    "claude-sonnet-4-5-20250929": "Claude Sonnet 4.5 (Recomanat)",
    "claude-opus-4-1-20250805": "Claude Opus 4.1 (Més potent)",
    "claude-haiku-4-5-20251001": "Claude Haiku 4.5 (Més ràpid i econòmic)",
    "claude-3-5-sonnet-20241022": "Claude 3.5 Sonnet (Legacy)",
    "claude-3-opus-20240229": "Claude 3 Opus (Legacy)",
}

# Llenguatges suportats
LANGUAGES = {
    "ca": "Català",
    "es": "Español",
    "en": "English",
    "fr": "Français",
    "de": "Deutsch",
}

# Services
SERVICE_CREATE_AUTOMATION = "create_automation"
SERVICE_VALIDATE_AUTOMATION = "validate_automation"

# Attributes
ATTR_DESCRIPTION = "description"
ATTR_VALIDATE_ONLY = "validate_only"
ATTR_PREVIEW = "preview"
ATTR_AUTOMATION_ID = "automation_id"
ATTR_YAML_CONTENT = "yaml_content"

# API
API_TIMEOUT = 30
MAX_TOKENS = 2048
