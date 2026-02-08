# ODI - Visión liveodi.com
## Agente Operativo de Escritorio (Desktop Agent)

---

## Objetivo

Al abrir `https://liveodi.com`:

1. El dispositivo se **registra**
2. Se instala un **bridge local**
3. ODI levanta servicios
4. ODI ve tu pantalla
5. ODI opera ventanas
6. ODI habla, escucha y ejecuta
7. Todo sincronizado con cerebro central (64.23.170.118)

**Esto es un Runtime de Agente Local + Orquestador Central.**

---

## Arquitectura

### 1. liveodi.com = Launcher

```
liveodi.com → detecta OS → descarga odi-client-bridge
```

- Windows → `odi-client.exe`
- Linux → `odi-client.AppImage`

### 2. ODI Client Bridge (pieza clave)

Proceso local en laptop/PC:

#### A. Registro del dispositivo
```json
POST /register_device
{ hostname, mac, os, screen_res, gpu }
```

#### B. Screen streaming
```bash
ffmpeg -f gdigrab -i desktop
```
Envío por WebSocket: `ws://64.23.170.118:9001/screen`

#### C. Control mouse/teclado
- pyautogui
- pynput

#### D. Ventanas dinámicas
```python
subprocess.Popen("chrome https://shopify.com")
```

### 3. Playwright Continuo

Workers permanentes en servidor:
- Navegan
- Scrollean
- Scrapean
- Capturan

### 4. AI Studio (Gemini) = Comprensión Visual

```
frame → Gemini → JSON → ODI decide → ODI actúa
```

**Separación clara:**
- Gemini VE
- ODI ACTÚA

### 5. Sistema de Ventanas

| Tipo | Función | Comportamiento |
|------|---------|----------------|
| **Consola Fija** | Control vacío | Solo logs, minimalista |
| **Semi-permanentes** | Procesos largos | Carga productos, scraping |
| **Permanencia Media** | Notificaciones | WhatsApp, correo, SMS |
| **Ventanas Operativas** | Picture-in-Picture | Playwright en acción |

### 6. Centro de Comunicaciones

```
WhatsApp → ODI → habla (Ramona/Tony)
Correo → ODI → lee
Llamada → Vapi → ODI decide
```

---

## Fases de Construcción

| Fase | Componente | Estado |
|------|------------|--------|
| 1 | odi-client-bridge (registro, screen, mouse) | Pendiente |
| 2 | Playwright + client bridge | Pendiente |
| 3 | Session Memory + catálogo conversacional | **EN PROGRESO** |
| 4 | Ventanas Famous + telemetría | Pendiente |
| 5 | Voz integrada | 60% (Vapi/ElevenLabs) |

---

## Comparación con Proyectos Similares

ODI es de la misma clase que:
- OpenAI Operator
- Adept ACT-1
- Devin

**Pero aplicado a industria real:**
- Inventarios reales
- Ventas reales
- Máquinas reales

---

## Tecnologías Clave

- **Frontend:** Electron / Tauri / Famous.ai
- **Screen Capture:** mss, ffmpeg, webrtc
- **Control:** pyautogui, pynput
- **Automatización:** Playwright, Selenium
- **Visión:** Gemini AI Studio
- **Voz:** Vapi, ElevenLabs (Tony, Ramona)
- **Comunicación:** WebSockets, WebRTC

---

*"ODI no es SaaS. Es un Autonomous Desktop Agent para industria real."*
