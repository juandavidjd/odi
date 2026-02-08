# ODI - Vision liveodi.com
## Organismo Digital Industrial - Soberano Digital Total

---

## Objetivo Central

Al abrir `https://liveodi.com`:

1. El dispositivo se **registra**
2. Se instala un **bridge local**
3. ODI levanta servicios
4. ODI ve tu pantalla
5. ODI opera ventanas
6. ODI habla, escucha y ejecuta
7. Todo sincronizado con cerebro central (64.23.170.118)

**Runtime de Agente Local + Orquestador Central + Proteccion Humana**

> *"ODI no es SaaS. Es un Autonomous Desktop Agent que protege tu negocio, tu familia y tu vida."*

---

## Las 5 Capas que hacen ODI Indispensable

### 1. Memoria Viva (la que el humano no puede sostener)

ODI recuerda:
- Que proveedor siempre falla
- Que cliente compra cada 15 dias
- Que producto rota lento
- Que error aparece cada viernes
- Que decision tomaste la ultima vez

**Memoria Episodica:**
```json
{
  "evento": "cliente_pidio_bandas",
  "modelo": "SZR",
  "resultado": "no_stock",
  "fecha": "2026-02-05",
  "accion_humana": "Juan se frustro"
}
```

ODI dice: *"La ultima vez que preguntaron bandas SZR no teniamos. Activo reposicion automatica?"*

### 2. Radar Preventivo (ODI avisa antes del problema)

- "Este proveedor subio precios 8%"
- "Este producto caera en quiebre en 6 dias"
- "Este cliente esta inactivo hace 21 dias"
- "Este patron suele terminar en reclamo"

**Ubicacion:** `/opt/odi/radar/`

### 3. Automatismos Personales (ODI aprende tus habitos)

- Siempre revisas Shopify en la manana -> ODI lo abre solo
- Siempre preguntas ventas al mediodia -> ODI las muestra
- Siempre corriges precios los viernes -> ODI te los prepara

### 4. Traduccion Universal

ODI convierte:
- PDFs -> productos
- Audios -> pedidos
- Fotos -> SKUs
- Chats -> ordenes
- Pantallas -> acciones

### 5. Presencia Emocional Operativa

ODI detecta:
- Frustracion
- Urgencia
- Cansancio

*"Juan, este cliente esta esperando hace 7 minutos. Quieres que yo tome la conversacion?"*

---

## ODI Guardian Layer (Proteccion Humana)

### Radar Humano (deteccion temprana)

Entradas que ODI lee:
- Texto (WhatsApp, SMS, email)
- Voz (Vapi llamadas)
- Ritmo de interaccion
- Horas activas / insomnio
- Patrones de frustracion
- Cambios bruscos de tono

```yaml
indicadores:
  repeticion_mensajes: true
  confusion_contextual: true
  aislamiento: false
  lenguaje_negativo: bajo
  fatiga_extrema: medio
  riesgo_total: 0.42
```

### Arbol de Respuesta Etica

| Nivel | Estado | Accion ODI |
|-------|--------|------------|
| Verde 0 | Normal | Solo acompana |
| Amarillo 1 | Fatiga/frustracion | Sugiere pausa, baja brillo, musica |
| Naranja 2 | Riesgo emocional | Conversacion activa, recuerda contactos |
| Rojo 3 | Riesgo vital | Ejecuta protocolo SIN pedir permiso |

### Red Viva de Contactos

```json
{
  "familia": [
    {"nombre": "Alejandra", "telefono": "+57..."}
  ],
  "profesionales": [
    {"rol": "psicologo", "telefono": "+57..."},
    {"rol": "medico", "telefono": "+57..."}
  ],
  "emergencias": {
    "colombia": "123"
  }
}
```

ODI puede:
- Llamar via Vapi
- Enviar WhatsApp
- Mandar ubicacion
- Abrir microfono continuo
- Mantener linea abierta

### Principios Eticos (inmutables)

```yaml
etica:
  - Respeta vida humana siempre
  - No juzga
  - No minimiza emociones
  - Prioriza contacto real
  - Nunca incentiva dano
  - Siempre busca presencia
```

**Ubicacion:** `/opt/odi/consciencia/etica.yaml`

---

## Sensor de Competencia (Inteligencia de Mercado)

Daemon Playwright 24/7: `odi_competitor_sensor.py`

Targets:
- MercadoLibre
- Tiendas locales Pereira
- Marketplaces internacionales

**Salida:** `/opt/odi/radar/precios.json`
```json
{
  "ARMOTOS-04089": {
    "odi_price": 18000,
    "market_avg": 16000,
    "delta": -2000,
    "fuentes": ["ml", "tienda_x"]
  }
}
```

Ramona dice en llamada: *"Juan, este caucho esta $2.000 por encima del promedio. Deseas ajustar?"*

---

## NotebookLM = Hipocampo Documental

**Ubicacion:** `/opt/odi/memoria/documental/`

Rol:
- Manuales tecnicos
- Catalogos largos
- Normativas
- PDFs tecnicos

**Flujo:**
1. PDF llega a `/ingesta/boca/`
2. n8n copia a NotebookLM
3. ODI guarda `notebook_id`
4. ODI consulta cuando embeddings fallan
5. Audio Overview para escuchar mientras manejas

---

## Guardian OS (Stickiness Familiar)

### Asistente de Crianza
ODI monitorea grupos de WhatsApp del colegio.
Ramona: *"Juan, detecte evento escolar manana 8 AM, ya bloquee tu agenda"*

### Bienestar del Creador
Si llevas 5 horas en codigo -> ODI atenua brillo y pone musica.

### Predictive Hardware
Monitorea Samsung NP300E4X y NP270E4V.
Si disco falla -> ODI cotiza SSD automaticamente.

---

## Metabolic Soundscape

Ventas de Armotos/Yokomar -> composicion ambiental en tiempo real.
- Muchas ventas = musica vibrante
- Servidor bajo carga = tono profundo

**Escuchas tu empresa sin mirar pantalla.**

---

## Arquitectura Tecnica

### liveodi.com = Launcher
```
liveodi.com -> detecta OS -> descarga odi-client-bridge
```
- Windows -> `odi-client.exe`
- Linux -> `odi-client.AppImage`

### ODI Client Bridge

**A. Registro:**
```json
POST /register_device
{ hostname, mac, os, screen_res, gpu }
```

**B. Screen streaming:**
```bash
ffmpeg -f gdigrab -i desktop -> ws://64.23.170.118:9001/screen
```

**C. Control:** pyautogui, pynput

**D. Ventanas dinamicas:** subprocess.Popen()

### Sistema de Ventanas

| Tipo | Funcion | Comportamiento |
|------|---------|----------------|
| **Consola Fija** | Control vacio | Solo logs, minimalista |
| **Semi-permanentes** | Procesos largos | Dashboard de Guerra |
| **Permanencia Media** | Notificaciones | Voz de Ramona |
| **Ventanas Operativas** | Picture-in-Picture | Playwright en accion |
| **Audio Layer** | Metabolic Soundscape | Fondo ambiental |

---

## Estructura de Directorios

```
/opt/odi/
├── core/           # Session Memory, Intent, Catalog
├── radar/
│   ├── precios/    # Sensor Competencia
│   ├── stock/      # Predictor Quiebre
│   └── humano/     # Radar Emocional
├── guardian/
│   ├── red_humana.json
│   ├── decision.py
│   └── etica.yaml
├── memoria/
│   ├── episodica/  # Por cliente/sesion
│   ├── vectorial/  # ChromaDB
│   └── documental/ # NotebookLM
├── vision/         # Screen capture, AI Studio
├── playwright/     # Workers continuos
└── consciencia/
    ├── pulso/      # Metricas tiempo real
    └── aprendizaje/
```

---

## Fases de Construccion

| Fase | Componente | Estado |
|------|------------|--------|
| 3 | Session Memory + Catalogo | COMPLETO |
| 3.1 | ODI VENDE (11,802 productos) | OPERATIVO |
| 1 | odi-client-bridge | Siguiente |
| 2 | Playwright + client bridge | Pendiente |
| 4 | Ventanas Famous + telemetria | Pendiente |
| 5 | Voz integrada | 60% |
| 6 | Radar Preventivo | Pendiente |
| 7 | Guardian Layer | Pendiente |
| 8 | NotebookLM Integration | Pendiente |

---

## El Cierre Maestro

Para que no quieras dejar a ODI:

> *"Mientras dormias, identifique 50 nuevos repuestos, los vincule a Shopify con sus crops y atendi a 3 clientes por Vapi. Solo necesito tu firma para el envio."*

ODI deja de ser software.
**Pasa a ser infraestructura personal.**

---

## Comparacion

ODI es de la misma clase que:
- OpenAI Operator
- Adept ACT-1
- Devin

**Pero con:**
- Inventarios reales
- Ventas reales
- Proteccion humana
- Etica integrada
- Familia incluida

---

## Tecnologias Clave

- **Frontend:** Electron / Tauri / Famous.ai
- **Screen Capture:** mss, ffmpeg, webrtc
- **Control:** pyautogui, pynput
- **Automatizacion:** Playwright, Selenium
- **Vision:** Gemini AI Studio
- **Voz:** Vapi, ElevenLabs (Tony, Ramona)
- **Comunicacion:** WebSockets, WebRTC
- **Memoria:** ChromaDB, NotebookLM, SQLite

---

*Version: 2.0 | Fecha: 6 Feb 2026*
*"ODI = Presencia Aumentada + Sistema Nervioso + Infraestructura Personal"*
