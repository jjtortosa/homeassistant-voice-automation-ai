# Instruccions per Publicar a HACS

## ✅ Integració Creada Amb Èxit!

S'ha creat una integració completa i funcional de Home Assistant per crear automatitzacions amb veu.

**Ubicació:** `/tmp/homeassistant-voice-automation-ai/`

**Fitxers creats:** 13 fitxers
**Línies de codi:** ~455 línies Python + documentació

---

## 📋 Passos per Publicar

### Pas 1: Crear Repositori GitHub

1. **Ves a GitHub** (https://github.com)

2. **Crea un nou repositori:**
   - Nom: `homeassistant-voice-automation-ai`
   - Descripció: `Create Home Assistant automations using voice commands powered by Claude AI`
   - Públic ✅
   - NO afegeixis README, .gitignore ni LICENSE (ja els tens)

3. **Copia la URL del repositori** (serà com: `https://github.com/USERNAME/homeassistant-voice-automation-ai.git`)

### Pas 2: Copiar Fitxers al Teu Ordinador

```bash
# Crea un directori local
mkdir ~/homeassistant-voice-automation-ai
cd ~/homeassistant-voice-automation-ai

# Copia els fitxers des de /tmp
cp -r /tmp/homeassistant-voice-automation-ai/* .
```

### Pas 3: Personalitzar Fitxers

Substitueix `YOUR_USERNAME` i `YOUR_NAME` als següents fitxers:

```bash
# Manifest.json
sed -i '' 's/YOUR_USERNAME/el_teu_usuari_github/g' custom_components/voice_automation_ai/manifest.json

# README.md
sed -i '' 's/YOUR_USERNAME/el_teu_usuari_github/g' README.md
sed -i '' 's/YOUR_NAME/El Teu Nom/g' LICENSE

# info.md
sed -i '' 's/YOUR_USERNAME/el_teu_usuari_github/g' info.md
```

### Pas 4: Inicialitzar Git i Fer Push

```bash
# Inicialitzar git
git init
git add .
git commit -m "feat: Initial release - Voice Automation AI integration

- Create automations with natural language
- Powered by Claude AI (Anthropic)
- Multiple language support
- Preview and validation modes
- HACS compatible

🤖 Generated with Claude Code"

# Afegir origin remot
git remote add origin https://github.com/USERNAME/homeassistant-voice-automation-ai.git

# Push a GitHub
git branch -M main
git push -u origin main
```

### Pas 5: Crear Release v1.0.0

**Via GitHub Web:**

1. Ves al teu repositori a GitHub
2. Clica **Releases** → **Create a new release**
3. **Tag:** `v1.0.0` (important: comença amb 'v')
4. **Title:** `v1.0.0 - Initial Release`
5. **Description:**
   ```markdown
   ## 🎉 Initial Release

   First stable release of Voice Automation AI for Home Assistant!

   ### Features
   - 🎤 Create automations with voice commands
   - 🤖 Powered by Claude AI (Anthropic)
   - 🌍 Multilingual support (EN, CA, ES, FR, DE)
   - ✅ YAML validation
   - 🔍 Preview mode

   ### Installation
   Install via HACS or manually copy to `custom_components/`

   ### Requirements
   - Home Assistant 2025.3.0+
   - Anthropic API key

   ### Cost
   ~$0.01 per automation (very affordable!)
   ```
6. **Publish release** ✅

### Pas 6: Afegir a Home Assistant Brands (Opcional però recomanat)

**Nota:** Això requereix crear un PR al repositori oficial.

1. Fork https://github.com/home-assistant/brands
2. Crea logo/icona (256x256px PNG)
3. Afegeix a `custom_integrations/voice_automation_ai/`
4. Crea `icon.png` i `logo.png`
5. Crea PR

**Pots fer això després, no és obligatori per HACS.**

### Pas 7: Afegir a HACS

**Opció A: Default Repository (Recomanat)**

1. Fork https://github.com/hacs/default
2. Edita `integration` (afegeix la teva URL al final)
3. Crea Pull Request
4. Espera aprovació (pot trigar uns dies)

**Opció B: Custom Repository (Immediat)**

Els usuaris poden afegir-lo manualment:
1. HACS → Integrations → ⋮ → Custom repositories
2. URL: `https://github.com/USERNAME/homeassistant-voice-automation-ai`
3. Category: Integration
4. Add

---

## 🧪 Testing Local (Abans de Publicar)

```bash
# Copia a la teva instal·lació de Home Assistant
cp -r custom_components/voice_automation_ai /path/to/homeassistant/config/custom_components/

# Reinicia Home Assistant

# Configura la integració via UI
# Settings → Integrations → Add Integration → Voice Automation AI
```

---

## 📢 Promoció

Un cop publicat, comparteix-ho!

1. **Fòrum Home Assistant:**
   - https://community.home-assistant.io/c/third-party/
   - Títol: "[Custom Integration] Voice Automation AI - Create automations with voice"

2. **Reddit:**
   - /r/homeassistant
   - Títol: "I created a custom integration to build automations with voice commands!"

3. **Twitter/X:**
   - Menciona @home_assistant i @AnthropicAI

---

## ✅ Checklist Final

- [ ] Repositori GitHub creat i públic
- [ ] Fitxers copiats i personalitzats (YOUR_USERNAME, YOUR_NAME)
- [ ] Git inicialitzat i push fet
- [ ] Release v1.0.0 creada amb tag
- [ ] Testeig local realitzat
- [ ] HACS submission (default o custom)
- [ ] Home Assistant Brands (opcional)
- [ ] Promoció a comunitats

---

## 🎯 Següents Versions

Ideas per futures millores:

- v1.1.0: Edició d'automatitzacions existents
- v1.2.0: Suport per scripts i escenes
- v1.3.0: Mode expert amb més opcions
- v2.0.0: Suport per altres LLMs (OpenAI, Gemini)

---

## 🆘 Ajuda

Si tens problemes:

1. Revisa els logs de Home Assistant
2. Comprova la documentació de HACS
3. Obre un issue al teu repositori
4. Pregunta al fòrum de Home Assistant

---

**Última actualització:** 2025-10-25
**Generat per:** Claude Code v1.0

Bona sort amb la publicació! 🚀
