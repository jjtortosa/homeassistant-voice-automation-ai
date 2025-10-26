# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2025-10-26

### Added
- Integration with Claude 4.5 models:
  - Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`) as default - Recommended
  - Claude Opus 4.1 (`claude-opus-4-1-20250805`) - Most powerful
  - Claude Haiku 4.5 (`claude-haiku-4-5-20251001`) - Fastest, most economical
- Auto-detection of language from Home Assistant configuration (`hass.config.language`)
- Support for both list and dict YAML formats from Claude responses

### Changed
- **[Breaking]** Default model changed from `claude-3-5-sonnet-20241022` to `claude-sonnet-4-5-20250929`
- Language field removed from configuration flow (auto-detected now)
- Improved UX: users no longer need to select language manually
- Updated prompts to respect language parameter from HA config

### Fixed
- Fixed `'list' object has no attribute 'get'` error when creating automations
- Proper handling of YAML list format (starting with `- alias:`) from Claude responses
- Corrected automation data extraction when Claude returns YAML as list

### Development
- Setup dedicated HAOS testing environment for development
- Configured automated deployment workflow for faster testing cycles
- Updated all documentation to reflect HA 2025 UI changes (Services → Actions)

### Testing
- Successfully tested 3 automation creations
- Preview mode verified working
- YAML validation confirmed functional
- Claude Sonnet 4.5 generating high-quality, valid automations
- Average response time: 3-5 seconds

### Documentation
- Updated `CLAUDE.md` - Development workflow, testing procedures, recent changes

## [0.0.1] - 2025-10-25

### Added
- Initial release
- Basic integration with Home Assistant
- Service `voice_automation_ai.create_automation` for creating automations via natural language
- Service `voice_automation_ai.validate_automation` for YAML validation
- Support for Claude 3.5 Sonnet, Claude 3 Opus, Claude 3 Haiku
- Configuration flow with API key validation
- Multi-language support (Catalan, Spanish, English, French, German)
- Entity context gathering for better automation generation
- Automatic ID generation for automations
- Integration with `automations.yaml`
- Preview and validate-only modes

### Known Issues
- Language parameter not respected in prompts (hardcoded to Catalan)
- Error when automation YAML is returned as list format

---

## Legend

- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security improvements
- **Development**: Development workflow improvements
- **Testing**: Testing improvements
- **Documentation**: Documentation changes
