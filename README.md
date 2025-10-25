# Voice Automation AI for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![GitHub release](https://img.shields.io/github/release/jjtortosa/homeassistant-voice-automation-ai.svg)](https://GitHub.com/jjtortosa/homeassistant-voice-automation-ai/releases/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Create Home Assistant automations using natural language voice commands powered by Claude AI from Anthropic.

## Features

- 🎤 **Voice-controlled automation creation** - Just describe what you want in natural language
- 🤖 **Powered by Claude AI** - Uses Anthropic's advanced language models
- ✅ **YAML validation** - Ensures generated automations are valid before creating them
- 🌍 **Multilingual** - Supports English, Catalan, Spanish, French, and German
- 🔍 **Preview mode** - See the generated YAML before creating the automation
- 📝 **Context-aware** - Uses your existing Home Assistant entities
- 🎯 **Multiple models** - Choose between Claude 3.5 Sonnet, Opus, or Haiku

## Installation

### HACS (Recommended)

1. Open HACS in your Home Assistant instance
2. Click on "Integrations"
3. Click the three dots in the top right corner
4. Select "Custom repositories"
5. Add `https://github.com/jjtortosa/homeassistant-voice-automation-ai` as an Integration
6. Click "Install" on the Voice Automation AI card
7. Restart Home Assistant

### Manual Installation

1. Copy the `custom_components/voice_automation_ai` folder to your `config/custom_components/` directory
2. Restart Home Assistant

## Configuration

1. Go to **Settings** → **Devices & Services**
2. Click **+ ADD INTEGRATION**
3. Search for **Voice Automation AI**
4. Enter your **Anthropic API Key** (get one at https://console.anthropic.com/)
5. Select your preferred **Claude model** and **language**
6. Click **Submit**

## Usage

### With Voice Assistant

1. Configure your voice assistant to use Anthropic Claude as the conversation agent:
   - Go to **Settings** → **Voice Assistants**
   - Select your assistant
   - Choose **Anthropic Claude** as the conversation agent

2. Add this prompt to your Anthropic integration instructions:
   ```
   When the user asks you to create an automation, use the service:
   - Service: voice_automation_ai.create_automation
   - Data: description: "<user's description>"

   Examples:
   - "Create an automation that turns on the lights when I arrive home"
   - "Make the blinds close at sunset"
   - "Notify me when the front door opens"
   ```

3. Use voice commands like:
   - "Create an automation that turns on the living room lights when I arrive"
   - "Make an automation to close the blinds at 9 PM"
   - "Set up an automation to notify me when the door opens"

### Via Service Call

You can also use the service directly in automations or scripts:

```yaml
service: voice_automation_ai.create_automation
data:
  description: "Turn on the kitchen lights when motion is detected"
  preview: false  # Set to true to preview without creating
  validate_only: false  # Set to true to only validate
```

### Developer Tools

Test the integration in **Developer Tools** → **Services**:

1. Select `voice_automation_ai.create_automation`
2. Enter a description
3. Call the service

## Examples

### Example 1: Motion-activated lights

**Voice command:** "Create an automation that turns on the bathroom light when motion is detected"

**Generated automation:**
```yaml
- alias: "Turn on bathroom light with motion"
  description: "Turns on the bathroom light when motion sensor detects movement"
  mode: single
  trigger:
    - platform: state
      entity_id: binary_sensor.bathroom_motion
      to: "on"
  condition: []
  action:
    - service: light.turn_on
      target:
        entity_id: light.bathroom
```

### Example 2: Time-based automation

**Voice command:** "Close all blinds at sunset"

**Generated automation:**
```yaml
- alias: "Close blinds at sunset"
  description: "Automatically closes all blinds when the sun sets"
  mode: single
  trigger:
    - platform: sun
      event: sunset
  condition: []
  action:
    - service: cover.close_cover
      target:
        entity_id: all
```

## Services

### `voice_automation_ai.create_automation`

Create a new automation from a natural language description.

**Parameters:**
- `description` (required): Natural language description of what you want to automate
- `preview` (optional): Preview the YAML without creating (default: false)
- `validate_only` (optional): Only validate without creating (default: false)

**Returns:**
- `success`: Whether the operation was successful
- `automation_id`: ID of the created automation (if created)
- `alias`: Friendly name of the automation
- `yaml`: Generated YAML (if preview mode)

### `voice_automation_ai.validate_automation`

Validate automation YAML syntax.

**Parameters:**
- `yaml_content` (required): YAML content to validate

**Returns:**
- `success`: Whether the validation was successful
- `valid`: Whether the YAML is valid
- `error`: Error message (if invalid)

## Configuration Options

| Option | Description | Default |
|--------|-------------|---------|
| API Key | Your Anthropic API key | Required |
| Model | Claude model to use | Claude 3.5 Sonnet |
| Language | Language for generated automations | English |

### Available Models

- **Claude 3.5 Sonnet** (Recommended) - Best balance of speed, intelligence, and cost
- **Claude 3 Opus** - Most powerful, best for complex automations
- **Claude 3 Haiku** - Fastest and most economical

## Cost

Using this integration calls the Anthropic API. Estimated costs:

- **Per automation:** ~$0.003-0.015 USD
- **Monthly (10 automations):** ~$0.15 USD

Very affordable! 💰

## Troubleshooting

### "Cannot connect to API"
- Check your internet connection
- Verify your API key is correct
- Ensure you have API credits in your Anthropic account

### "Invalid YAML generated"
- Try rephrasing your description more clearly
- Ensure the entities you mention exist in Home Assistant
- Use the preview mode to see the generated YAML

### Automation doesn't work as expected
- Check the generated automation in **Settings** → **Automations**
- Edit it manually if needed
- Provide more specific descriptions next time

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Powered by [Anthropic Claude AI](https://www.anthropic.com/)
- Inspired by the Home Assistant community
- Built with ❤️ for the smart home enthusiasts

## Support

- [Report bugs](https://github.com/jjtortosa/homeassistant-voice-automation-ai/issues)
- [Request features](https://github.com/jjtortosa/homeassistant-voice-automation-ai/issues)
- [Community discussion](https://community.home-assistant.io/)

---

**Note:** This is a custom integration and is not affiliated with or endorsed by Home Assistant or Anthropic.
