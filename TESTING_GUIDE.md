# Guia de Testing Local

Aquesta guia t'ajudarà a provar la integració **Voice Automation AI** localment abans de publicar-la.

## ⚠️ Abans de Començar

Aquesta és una versió **BETA (v0.1.0)** que encara no s'ha provat extensivament en entorns reals.

## 📋 Prerequisits

- Home Assistant 2025.3.0 o superior
- Clau API d'Anthropic (obtén-ne una a https://console.anthropic.com/)
- Accés al directori de configuració de Home Assistant

## 🔧 Instal·lació Local

### Opció 1: Enllaç Simbòlic (Recomanat per desenvolupament)

```bash
# Navega al directori de configuració de Home Assistant
cd ~/.homeassistant  # o /config si uses Home Assistant OS

# Crea el directori custom_components si no existeix
mkdir -p custom_components

# Crea un enllaç simbòlic
ln -s /Users/juanjo/PhpstormProjects/homeassistant-voice-automation-ai/custom_components/voice_automation_ai custom_components/voice_automation_ai
```

### Opció 2: Còpia Directa

```bash
# Copia la integració al directori de configuració
cp -r custom_components/voice_automation_ai ~/.homeassistant/custom_components/
```

### Opció 3: Via HACS (Custom Repository)

1. Obre HACS a Home Assistant
2. Ves a **Integrations**
3. Clica els tres punts al cantó superior dret
4. Selecciona **Custom repositories**
5. Afegeix: `https://github.com/jjtortosa/homeassistant-voice-automation-ai`
6. Categoria: **Integration**
7. Clica **Add**
8. Cerca "Voice Automation AI" i instal·la

## 🚀 Configuració

1. **Reinicia Home Assistant**
   - Ves a **Settings** → **System** → **Restart**

2. **Afegeix la integració**
   - Ves a **Settings** → **Devices & Services**
   - Clica **+ ADD INTEGRATION**
   - Cerca **Voice Automation AI**

3. **Configura la integració**
   - Introdueix la teva **Anthropic API Key**
   - Selecciona el **model Claude** preferit:
     - Claude 3.5 Sonnet (recomanat)
     - Claude 3 Opus (més potent)
     - Claude 3 Haiku (més ràpid i econòmic)
   - Selecciona l'**idioma**:
     - Català (ca)
     - English (en)
     - Español (es)
     - Français (fr)
     - Deutsch (de)
   - Clica **Submit**

## ✅ Checklist de Testing

### Tests Bàsics

- [ ] **Instal·lació**
  - [ ] La integració apareix a Devices & Services
  - [ ] No hi ha errors al log (`Settings → System → Logs`)
  - [ ] La configuració es guarda correctament

- [ ] **Servei create_automation (mode preview)**
  - [ ] Ves a **Developer Tools** → **Services**
  - [ ] Selecciona `voice_automation_ai.create_automation`
  - [ ] Prova amb:
    ```yaml
    service: voice_automation_ai.create_automation
    data:
      description: "Turn on the living room light when motion is detected"
      preview: true
    ```
  - [ ] Verifica que retorna YAML vàlid
  - [ ] Comprova que el YAML té sentit per la descripció

- [ ] **Servei create_automation (crear real)**
  - [ ] Treu `preview: true`
  - [ ] Executa el servei
  - [ ] Ves a **Settings** → **Automations & Scenes**
  - [ ] Verifica que l'automatització s'ha creat
  - [ ] Comprova que és vàlida i funcional

- [ ] **Servei validate_automation**
  - [ ] Prova validar YAML correcte:
    ```yaml
    service: voice_automation_ai.validate_automation
    data:
      yaml_content: |
        - alias: "Test"
          trigger:
            - platform: state
              entity_id: light.test
          action:
            - service: light.turn_on
    ```
  - [ ] Prova validar YAML incorrecte i verifica que detecta l'error

### Tests Avançats

- [ ] **Integració amb Voice Assistant**
  - [ ] Configura Anthropic Claude com a conversation agent
  - [ ] Afegeix el prompt suggerit al README
  - [ ] Prova comandes de veu:
    - "Crea una automatització que encengui les llums quan arribi a casa"
    - "Fes una automatització per tancar les persianes a les 9 del vespre"
    - "Crea una automatització que em notifiqui quan s'obri la porta"

- [ ] **Diferents Idiomes**
  - [ ] Prova amb descripció en català
  - [ ] Prova amb descripció en anglès
  - [ ] Prova amb descripció en espanyol
  - [ ] Verifica que les automatitzacions generades són coherents

- [ ] **Diferents Models**
  - [ ] Prova amb Claude 3.5 Sonnet
  - [ ] Prova amb Claude 3 Haiku
  - [ ] Compara la qualitat i velocitat de resposta

- [ ] **Casos Límit**
  - [ ] Descripció ambigua (ex: "encendre llums")
  - [ ] Descripció amb entitats inexistents
  - [ ] Descripció molt complexa amb múltiples triggers i conditions
  - [ ] Descripció en idioma no suportat

### Tests d'Errors

- [ ] **API Key invàlida**
  - [ ] Intenta configurar amb API key incorrecta
  - [ ] Verifica que mostra error adequat

- [ ] **Sense crèdits API**
  - [ ] Si és possible, prova sense crèdits
  - [ ] Verifica el missatge d'error

- [ ] **Timeout/connexió**
  - [ ] Desconnecta internet temporalment
  - [ ] Verifica el comportament

## 🐛 Què Verificar als Logs

Comprova els logs de Home Assistant per:
- ❌ Errors d'importació de mòduls
- ❌ Errors de connexió a l'API d'Anthropic
- ❌ Errors de validació de YAML
- ❌ Errors en afegir automatitzacions a `automations.yaml`
- ✅ Missatges d'èxit en crear automatitzacions

```bash
# Per veure els logs en temps real
tail -f home-assistant.log | grep voice_automation_ai
```

## 📊 Mètriques a Registrar

Durant el testing, registra:
- ✅ Temps de resposta de l'API
- ✅ Qualitat de les automatitzacions generades
- ✅ Nombre d'errors vs èxits
- ✅ Cost aproximat per automatització
- ✅ Problemes o bugs trobats

## 🔄 Actualitzacions Durant Testing

Si fas canvis al codi durant el testing:

```bash
# Si uses enllaç simbòlic, només cal reiniciar HA
# Si vas copiar els fitxers, torna a copiar-los
cp -r custom_components/voice_automation_ai ~/.homeassistant/custom_components/

# Després reinicia Home Assistant
```

## 📝 Reportar Issues

Si trobes problemes:

1. **Comprova els logs** (`Settings → System → Logs`)
2. **Obre un issue a GitHub** amb:
   - Descripció del problema
   - Passos per reproduir-lo
   - Logs rellevants
   - Versió de Home Assistant
   - Model de Claude utilitzat
   - Descripció que vas utilitzar (si aplica)

## ✨ Feedback Útil

Després del testing, proporciona feedback sobre:
- ✅ Què funciona bé
- ⚠️ Què podria millorar
- 🐛 Bugs trobats
- 💡 Idees per futures funcionalitats
- 📚 Documentació confusa o incompleta

## 🎯 Criteris per Passar a v1.0.0

Abans de publicar v1.0.0 estable, la integració hauria de:
- ✅ Funcionar sense errors en almenys 3 instal·lacions diferents
- ✅ Crear automations vàlides el 95% de les vegades
- ✅ Gestionar errors adequadament
- ✅ Tenir documentació completa i clara
- ✅ Passar tots els tests d'aquesta guia

---

**Versió:** 0.1.0 (Beta)
**Data:** 2025-10-25
