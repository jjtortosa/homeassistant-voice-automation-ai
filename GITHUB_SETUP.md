# Configuració Final de GitHub

Aquest document explica els passos finals per configurar el repositori GitHub per complir amb els requisits de HACS.

## 📋 Requisits HACS

Per ser acceptat a HACS (com a repositori custom o default), el repositori ha de complir:

### ✅ Ja Complerts

- [x] Repositori públic a GitHub
- [x] README.md amb documentació completa
- [x] hacs.json amb el camp `name`
- [x] Codi funcional amb estructura correcta
- [x] LICENSE (MIT)
- [x] Al menys un fitxer .gitignore

### ⚠️ Pendents de Configurar

- [ ] Descripció del repositori
- [ ] Topics del repositori
- [ ] Al menys un release (es crearà aviat)

## 🔧 Configurar Descripció i Topics

### Via GitHub CLI (gh)

```bash
# Afegir descripció
gh repo edit --description "Create Home Assistant automations using natural language voice commands powered by Claude AI"

# Afegir topics (etiquetes per searchability)
gh repo edit --add-topic "home-assistant"
gh repo edit --add-topic "home-assistant-integration"
gh repo edit --add-topic "hacs"
gh repo edit --add-topic "automation"
gh repo edit --add-topic "voice-control"
gh repo edit --add-topic "claude-ai"
gh repo edit --add-topic "anthropic"
gh repo edit --add-topic "natural-language"
gh repo edit --add-topic "smart-home"
gh repo edit --add-topic "ai"
```

### Via GitHub Web UI

1. **Afegir Descripció**
   - Ves a https://github.com/jjtortosa/homeassistant-voice-automation-ai
   - Clica la icona d'engranatge (⚙️) al costat de "About"
   - A **Description**, afegeix:
     ```
     Create Home Assistant automations using natural language voice commands powered by Claude AI
     ```
   - **Website** (opcional): https://github.com/jjtortosa/homeassistant-voice-automation-ai
   - Clica **Save changes**

2. **Afegir Topics**
   - Al mateix diàleg "About", baixa fins a **Topics**
   - Afegeix els següents topics (un per un):
     - `home-assistant`
     - `home-assistant-integration`
     - `hacs`
     - `automation`
     - `voice-control`
     - `claude-ai`
     - `anthropic`
     - `natural-language`
     - `smart-home`
     - `ai`
   - Clica **Save changes**

## 🏷️ Crear Release v0.1.0

### Via GitHub CLI (gh)

```bash
# Crear tag i release
gh release create v0.1.0 \
  --title "v0.1.0 - Beta Release" \
  --notes "## 🧪 Beta Release

**⚠️ This is a beta version for testing purposes.**

### Features

- 🎤 Create automations with natural language voice commands
- 🤖 Powered by Claude AI (Anthropic)
- ✅ YAML validation before creating automations
- 🌍 Multilingual support (EN, CA, ES, FR, DE)
- 🔍 Preview mode to see generated YAML
- 📝 Context-aware using your Home Assistant entities
- 🎯 Multiple Claude models (Sonnet, Opus, Haiku)

### Installation

#### Via HACS (Custom Repository)

1. Open HACS in Home Assistant
2. Go to **Integrations**
3. Click the three dots → **Custom repositories**
4. Add: \`https://github.com/jjtortosa/homeassistant-voice-automation-ai\`
5. Category: **Integration**
6. Click **Add** and install

#### Manual Installation

1. Download the release
2. Extract \`custom_components/voice_automation_ai\` to your Home Assistant config directory
3. Restart Home Assistant
4. Add integration via UI: **Settings** → **Devices & Services** → **Add Integration**

### Requirements

- Home Assistant 2025.3.0+
- Anthropic API key (get one at https://console.anthropic.com/)

### Cost

Approximately \$0.003-0.015 USD per automation (very affordable!)

### Testing Status

- ✅ Code is complete and functional
- ⚠️ Limited real-world testing
- 🧪 Use at your own risk
- 🐛 Please report any issues

**Testers welcome!** Your feedback will help make this integration stable and production-ready.

See [TESTING_GUIDE.md](TESTING_GUIDE.md) for detailed testing instructions.

### Known Limitations

- Prompt language is currently hardcoded to Catalan regardless of language setting
- No support for editing existing automations (coming in v1.1.0)
- No support for scripts or scenes (coming in v1.2.0)

### Support

- 🐛 [Report bugs](https://github.com/jjtortosa/homeassistant-voice-automation-ai/issues)
- 💡 [Request features](https://github.com/jjtortosa/homeassistant-voice-automation-ai/issues)
- 📖 [Documentation](README.md)

---

🤖 Generated with [Claude Code](https://claude.com/claude-code)" \
  --prerelease

# Si vols que no sigui prerelease (però recomanem que ho sigui per v0.1.0), treu --prerelease
```

### Via GitHub Web UI

1. Ves a https://github.com/jjtortosa/homeassistant-voice-automation-ai/releases
2. Clica **Create a new release** o **Draft a new release**
3. **Choose a tag**: Escriu `v0.1.0` i selecciona "Create new tag: v0.1.0 on publish"
4. **Release title**: `v0.1.0 - Beta Release`
5. **Description**: Copia el contingut de les release notes de dalt
6. ✅ Marca **Set as a pre-release** (perquè és beta)
7. Clica **Publish release**

## ✅ Verificació Final

Després de configurar tot, verifica:

```bash
# Comprovar descripció i topics
gh repo view --json description,repositoryTopics

# Comprovar releases
gh release list

# Veure el repositori al navegador
gh repo view --web
```

També pots verificar manualment a:
- https://github.com/jjtortosa/homeassistant-voice-automation-ai

## 📢 Següents Passos

Un cop tinguis descripció, topics i release:

### 1. Testing Local
- Segueix la guia [TESTING_GUIDE.md](TESTING_GUIDE.md)
- Prova la integració a la teva instal·lació de Home Assistant
- Registra qualsevol problema o millora

### 2. Compartir amb Testers
- Comparteix el repositori amb amics/comunitat
- Demana feedback
- Recull issues i suggeriments

### 3. HACS Custom Repository (Immediat)
Els usuaris ja poden afegir-lo manualment:
1. HACS → Integrations → ⋮ → Custom repositories
2. URL: `https://github.com/jjtortosa/homeassistant-voice-automation-ai`
3. Category: Integration

### 4. HACS Default Repository (Després del testing)
Quan estigui estable (v1.0.0):
1. Fork https://github.com/hacs/default
2. Crea un branch nou
3. Edita `integration` i afegeix la teva URL
4. Crea Pull Request
5. Espera aprovació (pot trigar dies)

**IMPORTANT**: Per ser acceptat al default repository de HACS, necessites:
- ✅ Al menys un release
- ✅ hacs.json amb `name`
- ✅ README complet
- ✅ Descripció i topics al repositori
- ⚠️ **Home Assistant Brands** (icona/logo) - Altament recomanat

### 5. Home Assistant Brands (Opcional però recomanat)
1. Fork https://github.com/home-assistant/brands
2. Crea directori `custom_integrations/voice_automation_ai/`
3. Afegeix `icon.png` i `logo.png` (256x256px, fons transparent)
4. Crea Pull Request

## 🎨 Crear Icona/Logo (Opcional)

Idees per la icona:
- Micròfon + engranatge
- Ona de veu + Home Assistant logo
- Robot parlant + casa
- Colors: Blau (Home Assistant) + Verd/Taronja (Claude)

Eines per crear icones:
- Figma (gratuït)
- Canva (gratuït)
- DALL-E / Midjourney (AI)
- Fiverr (contractar dissenyador)

Requisits:
- Format: PNG amb transparència
- Mida: 256x256px
- Estil: Flat design, simple, recognizable a mida petita

---

**Data:** 2025-10-25
**Versió:** 0.1.0
