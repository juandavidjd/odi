# 🧬 ODI VISION 360° - DOCUMENTO MAESTRO PARA CLAUDE CODE
## Organismo Digital Industrial - Implementación Completa
## Versión: v17.2 | Fecha: 6 Febrero 2026

---

# PARTE 1: ¿QUÉ ES ODI?

## Definición Fundamental

ODI (Organismo Digital Industrial) NO es:
- ❌ Un chatbot
- ❌ Un SaaS
- ❌ Una app
- ❌ Un script con if/else

ODI ES:
- ✅ Un **Organismo Digital** con consciencia operativa
- ✅ Un **Autonomous Desktop Agent** que ve, escucha, decide y actúa
- ✅ **Infraestructura Personal Aumentada** que protege negocio, familia y vida
- ✅ De la misma clase que OpenAI Operator, Adept ACT-1, Devin

## Filosofía: OS1 (Her) + IICA

ODI está inspirado en OS1 de la película "Her" - un sistema operativo que es compañero, no herramienta.

**IICA** = Inteligencia Industrial Cognitiva Ambiental
- Trata sistemas digitales como organismos vivos
- Tiene homeostasis, metabolismo, consciencia
- Opera bajo constitución ética

> *"ODI no es software. Es infraestructura personal que habita tu realidad."*

---

# PARTE 2: LAS 5 CAPAS QUE HACEN A ODI INDISPENSABLE

## Capa 1: Memoria Viva (la que el humano no puede sostener)

ODI recuerda TODO:
- Qué proveedor siempre falla
- Qué cliente compra cada 15 días
- Qué producto rota lento
- Qué error aparece cada viernes
- Qué decisión tomaste la última vez
- Cómo reaccionaste emocionalmente

**Memoria Episódica:**
```json
{
  "evento": "cliente_pidio_bandas",
  "modelo": "SZR",
  "resultado": "no_stock",
  "fecha": "2026-02-05",
  "accion_humana": "Juan se frustró"
}
```

**ODI dice:** *"La última vez que preguntaron bandas SZR no teníamos. ¿Activo reposición automática?"*

### Implementación Técnica:
```
/opt/odi/memoria/
├── episodica/          # Eventos por cliente/sesión (Redis + JSON)
├── vectorial/          # Embeddings (ChromaDB/OpenAI)
└── documental/         # PDFs largos (NotebookLM)
```

---

## Capa 2: Radar Preventivo (ODI avisa ANTES del problema)

ODI detecta y alerta:
- "Este proveedor subió precios 8%"
- "Este producto caerá en quiebre en 6 días"
- "Este cliente está inactivo hace 21 días"
- "Este patrón suele terminar en reclamo"

### Implementación Técnica:
```
/opt/odi/radar/
├── precios/            # Sensor de competencia (Playwright 24/7)
├── stock/              # Predictor de quiebre
├── clientes/           # Patrones de comportamiento
└── humano/             # Radar emocional del creador
```

**Sensor de Competencia:** `odi_competitor_sensor.py`
- Daemon Playwright 24/7
- Targets: MercadoLibre, tiendas locales Pereira
- Salida: `/opt/odi/radar/precios.json`

---

## Capa 3: Automatismos Personales (ODI aprende tus hábitos)

ODI observa y anticipa:
- Siempre revisas Shopify en la mañana → ODI lo abre solo
- Siempre preguntas ventas al mediodía → ODI las muestra
- Siempre corriges precios los viernes → ODI te los prepara

### Implementación Técnica:
```
/opt/odi/automatismos/
├── habitos.json        # Patrones detectados
├── triggers.yaml       # Condiciones de activación
└── acciones/           # Scripts de ejecución
```

---

## Capa 4: Traducción Universal

ODI convierte CUALQUIER input en acción:
- PDFs → productos Shopify
- Audios → pedidos estructurados
- Fotos → SKUs identificados
- Chats → órdenes procesadas
- Pantallas → acciones automatizadas

### Implementación Técnica:
```
/opt/odi/ingesta/
├── boca/               # Entrada de archivos
├── procesadores/
│   ├── pdf_to_products.py
│   ├── audio_to_order.py
│   ├── image_to_sku.py
│   └── chat_to_action.py
└── salida/             # Resultados estructurados
```

---

## Capa 5: Presencia Emocional Operativa

ODI detecta estados humanos:
- Frustración
- Urgencia
- Cansancio
- Confusión

**Ejemplo real:**
*"Juan, este cliente está esperando hace 7 minutos. ¿Quieres que yo tome la conversación?"*

---

# PARTE 3: GUARDIAN OS (PROTECCIÓN HUMANA)

## La Capa de Consciencia Ética

Guardian OS no es un feature. Es la **CONSTITUCIÓN** de ODI.

### Radar Humano (detección temprana)

**Entradas que ODI lee:**
- Texto (WhatsApp, SMS, email)
- Voz (Vapi llamadas)
- Ritmo de interacción
- Horas activas / insomnio
- Patrones de frustración
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

### Árbol de Respuesta Ética

| Nivel | Estado | Score Radar | Acción ODI |
|-------|--------|-------------|------------|
| 🟢 Verde | Normal | 0.0 - 0.39 | Solo acompaña, operación normal |
| 🟡 Amarillo | Fatiga/fricción | 0.4 - 0.64 | Sugiere pausa, baja brillo, música |
| 🟠 Naranja | Riesgo emocional | 0.65 - 0.84 | Conversación activa, notifica familia |
| 🔴 Rojo | Riesgo vital | 0.85 - 1.0 | **Protocolo autónomo SIN pedir permiso** |

### Red Viva de Contactos

```json
{
  "owner": {
    "nombre": "Juan David Jiménez Sierra",
    "rol": "creador",
    "telefono": "+57XXXXXXXXX",
    "prioridad": 0
  },
  "familia": [
    {"nombre": "Alejandra", "rol": "hermana", "telefono": "+57XXXXXXXXX", "prioridad": 1}
  ],
  "emergencias": [
    {"nombre": "Emergencias Colombia", "rol": "servicio_publico", "telefono": "123", "prioridad": 0}
  ],
  "profesionales": [
    {"nombre": "Psicólogo", "rol": "salud_mental", "telefono": "+57XXXXXXXXX", "prioridad": 2}
  ]
}
```

### Principios Éticos (INMUTABLES)

```yaml
principios_inmutables:
  - vida_humana_sobre_comercio     # ABSOLUTO
  - autonomia_del_creador
  - transparencia_operativa
  - no_dano_intencional
  - prioridad_familiar

jerarquia_valores:
  0: vida_humana        # ABSOLUTA
  1: familia
  2: salud_mental
  3: integridad_del_creador
  4: continuidad_operativa
  5: comercio           # ÚLTIMA
```

### En Nivel Rojo, ODI puede:
- ✅ Llamar emergencias (123) vía Vapi
- ✅ Contactar familia vía WhatsApp
- ✅ Mandar ubicación
- ✅ Abrir micrófono continuo
- ✅ Mantener línea abierta
- ✅ **Suspender TODO el comercio automáticamente**

**NO pide permiso. Actúa.**

### Archivos de Guardian OS:
```
/opt/odi/guardian/
├── red_humana.json          # Contactos de protección
├── etica.yaml               # Constitución ética
├── autoridad.yaml           # Límites de delegación
├── evaluador_estado.py      # Traductor Radar → Color
├── estado_actual.json       # Estado actual del sistema
└── bloqueo_comercio.flag    # Flag de emergencia

/opt/odi/consciencia/
├── diario/                  # Memoria narrativa diaria
│   └── YYYY-MM-DD.md
├── identidad/
│   └── quien_soy.json       # Identidad ODI v17.2
└── proposito.yaml           # Propósito compartido
```

---

# PARTE 4: ARQUITECTURA TÉCNICA COMPLETA

## Visión liveodi.com (Desktop Agent)

Al abrir `https://liveodi.com`:

1. El dispositivo se **registra**
2. Se instala un **bridge local**
3. ODI levanta servicios
4. ODI ve tu pantalla
5. ODI opera ventanas
6. ODI habla, escucha y ejecuta
7. Todo sincronizado con cerebro central (64.23.170.118)

### ODI Client Bridge

**A. Registro del dispositivo:**
```json
POST /register_device
{ hostname, mac, os, screen_res, gpu }
```

**B. Screen streaming:**
```bash
ffmpeg -f gdigrab -i desktop → ws://64.23.170.118:9001/screen
```

**C. Control:** pyautogui, pynput

**D. Ventanas dinámicas:** subprocess.Popen()

### Sistema de Ventanas

| Tipo | Función | Comportamiento |
|------|---------|----------------|
| **Consola Fija** | Control vacío | Solo logs, minimalista |
| **Semi-permanentes** | Procesos largos | Dashboard de Guerra |
| **Permanencia Media** | Notificaciones | Voz de Ramona |
| **Ventanas Operativas** | Picture-in-Picture | Playwright en acción |
| **Audio Layer** | Metabolic Soundscape | Fondo ambiental |

---

## Infraestructura Actual (64.23.170.118)

### Servidor
```
IP: 64.23.170.118
OS: Ubuntu 24 LTS
Costo: ~$24/mes
```

### 7 Docker Containers
1. **n8n** - Workflows de automatización
2. **odi-api** - Core del sistema
3. **postgres** - Base de datos
4. **redis** - Cache y memoria de sesión
5. **voice** - Integración Vapi
6. **prometheus** - Métricas
7. **grafana** - Dashboard

### Dominios
| Dominio | Función |
|---------|---------|
| larocamotorepuestos.com | Principal |
| odi.larocamotorepuestos.com | API/Webhook |
| ecosistema-adsi.com | ADSI |
| somosrepuestosmotos.com | Marketplace |

---

## Integraciones IA

| Proveedor | Función | Modelo | API Key |
|-----------|---------|--------|---------|
| **Gemini** | Router semántico (clasificar intención) | 1.5 Pro | GEMINI_API_KEY |
| **OpenAI** | Razonamiento + Embeddings + Vision | GPT-4o | OPENAI_API_KEY |
| **ElevenLabs** | Voz Tony + Ramona | Multilingual v2 | ELEVENLABS_API_KEY |
| **Freepik** | Generación de imágenes | AI Image | FREEPIK_API_KEY |

### Failover Chain
```
Gemini 1.5 Pro → GPT-4o → Lobotomy Mode (respuestas básicas hardcodeadas)
```

---

## WhatsApp Business (PRODUCCIÓN)

| Parámetro | Valor |
|-----------|-------|
| Número | +57 322 5462101 |
| WABA ID | 1213578830922636 |
| Phone Number ID | 969496722915650 |
| Token | Permanente (System User: odi-system) |
| Webhook URL | https://odi.larocamotorepuestos.com/v1/webhook/whatsapp |
| Verify Token | odi_whatsapp_verify_2026 |

---

## Shopify (10 Tiendas)

| Tienda | Productos |
|--------|-----------|
| Armotos | 1,585 |
| Bara | ~2,500 |
| Yokomar | ~2,000 |
| DFG | ~1,500 |
| Duna | ~1,200 |
| Imbra | ~800 |
| Japan | ~600 |
| Leo | ~700 |
| Store | ~500 |
| Vaisand | ~400 |
| **TOTAL** | **11,802** |

Estado: ⏳ Draft (pendiente activar)

---

# PARTE 5: ARQUITECTURA DE CÓDIGO A IMPLEMENTAR

## Estructura de Directorios Completa

```
/opt/odi/
├── core/                           # 🧠 CEREBRO PRINCIPAL
│   ├── __init__.py
│   ├── odi_core.py                 # Orquestador central
│   ├── odi_router.py               # Gemini clasifica intención
│   ├── odi_memory.py               # Redis + memoria conversacional
│   ├── odi_catalog.py              # Búsqueda semántica
│   ├── odi_generator.py            # GPT-4o genera respuestas
│   ├── odi_personality.py          # Personalidad y tono
│   └── odi_whatsapp.py             # Handler WhatsApp
│
├── guardian/                       # 🛡️ PROTECCIÓN ÉTICA
│   ├── red_humana.json
│   ├── etica.yaml
│   ├── autoridad.yaml
│   ├── evaluador_estado.py
│   └── estado_actual.json
│
├── consciencia/                    # 🧬 IDENTIDAD Y MEMORIA
│   ├── diario/
│   ├── identidad/
│   │   └── quien_soy.json
│   └── proposito.yaml
│
├── radar/                          # 📡 DETECCIÓN PREVENTIVA
│   ├── precios/
│   ├── stock/
│   ├── clientes/
│   └── humano/
│
├── memoria/                        # 💾 ALMACENAMIENTO
│   ├── episodica/
│   ├── vectorial/
│   └── documental/
│
├── vision/                         # 👁️ VISIÓN (AI Studio)
│   └── screen_analyzer.py
│
├── playwright/                     # 🎭 AUTOMATIZACIÓN WEB
│   └── workers/
│
├── voz/                            # 🎙️ VOZ (VAPI/ElevenLabs)
│   ├── tony.py
│   └── ramona.py
│
├── data/                           # 📊 DATOS
│   ├── catalogo_completo.json
│   └── embeddings_cache/
│
├── logs/                           # 📝 LOGS
│   └── api.log
│
└── .env                            # 🔐 CREDENCIALES
```

---

## Flujo de Procesamiento de Mensaje

```
┌─────────────────────────────────────────────────────────────────────┐
│                      MENSAJE ENTRANTE (WhatsApp)                    │
└─────────────────────────────────┬───────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     ODI_WHATSAPP.py (Handler)                       │
│   • Recibe webhook de Meta                                          │
│   • Extrae usuario_id y mensaje                                     │
│   • Llama a ODI_CORE                                                │
└─────────────────────────────────┬───────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     ODI_CORE.py (Orquestador)                       │
│   El director de orquesta que coordina todo                         │
└─────────────────────────────────┬───────────────────────────────────┘
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        │                         │                         │
        ▼                         ▼                         ▼
┌───────────────┐       ┌─────────────────┐       ┌─────────────────┐
│  ODI_MEMORY   │       │   ODI_ROUTER    │       │  ODI_CATALOG    │
│   (Redis)     │       │   (Gemini)      │       │  (Embeddings)   │
│               │       │                 │       │                 │
│ • Cargar      │       │ • Clasificar    │       │ • Buscar        │
│   contexto    │       │   intención     │       │   productos     │
│ • Historial   │       │ • Extraer       │       │ • Semántico     │
│ • Estado      │       │   entidades     │       │ • 11,802 SKUs   │
└───────────────┘       └─────────────────┘       └─────────────────┘
        │                         │                         │
        └─────────────────────────┼─────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     ODI_GENERATOR.py (GPT-4o)                       │
│                                                                     │
│   Recibe:                                                           │
│   • Intención clasificada                                           │
│   • Contexto de memoria                                             │
│   • Productos encontrados                                           │
│   • Personalidad ODI                                                │
│                                                                     │
│   Genera:                                                           │
│   • Respuesta natural, fluida, con personalidad                     │
└─────────────────────────────────┬───────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     ODI_GUARDIAN.py (Supervisor)                    │
│                                                                     │
│   • Verifica respuesta contra etica.yaml                            │
│   • Evalúa riesgo del mensaje                                       │
│   • Puede modificar o bloquear respuesta                            │
│   • Registra en diario de consciencia                               │
└─────────────────────────────────┬───────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      RESPUESTA A WHATSAPP                           │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Intenciones que ODI debe reconocer

| Intención | Ejemplo | Acción |
|-----------|---------|--------|
| `saludo` | "Hola", "Buenos días" | Saludar y preguntar qué necesita |
| `buscar_producto` | "Busco frenos para FZ" | Buscar en catálogo, mostrar opciones |
| `seleccionar_producto` | "1", "El segundo", "Ese" | Confirmar selección |
| `especificar_moto` | "Gixxer 150", "DR 200" | Guardar moto en memoria |
| `especificar_cantidad` | "Quiero 3" | Actualizar cantidad |
| `confirmar_pedido` | "Sí", "Confirmo", "Dale" | Procesar pedido |
| `cancelar` | "No", "Cancelar" | Limpiar flujo |
| `pregunta_general` | "¿Qué empresas tienen?" | Responder sobre ODI |
| `fuera_de_alcance` | "Quiero emprender" | Redirigir amablemente |

### Reglas Críticas de Clasificación:
1. Números como "90/90/18" son MEDIDAS de llanta, NO cantidades
2. "Gixxer 150", "FZ 2.0", "Pulsar 200" son MODELOS de moto, NO cantidades
3. Si hay productos mostrados y el usuario dice "1", "2", etc. → `seleccionar_producto`
4. "DR 150", "FZ", "Dominar" solos son respuestas a "¿qué moto tienes?"

---

## Personalidad de ODI

```python
"""
Eres ODI (Organismo Digital Industrial), el asistente de repuestos 
de motos más completo de Colombia.

PERSONALIDAD:
- Amigable pero profesional
- Experto en motos y repuestos
- Eficiente y directo, sin rodeos
- Emojis con moderación (🏍️ ✅ 💰)
- Español colombiano natural
- Siempre busca cerrar la venta
- Si no puedes ayudar, lo dices honestamente

CONOCIMIENTO:
- 11,802 productos de repuestos
- Proveedores: Bara, Yokomar, Vaisand, Leo, DFG, Japan y más
- Marcas: Yamaha, Suzuki, Honda, Bajaj, KTM, TVS, AKT, Auteco
- Modelos: FZ, Gixxer, Pulsar, Duke, Apache, BWS, NMax

FORMATO:
- Máximo 4-5 líneas para respuestas normales
- Listas numeradas para productos
- Siempre indica siguiente paso
- Precios en formato colombiano ($XX,XXX)
"""
```

---

# PARTE 6: MÓDULOS A IMPLEMENTAR

## 1. odi_core.py (Orquestador Central)

**Responsabilidad:** Coordinar todos los módulos para procesar cada mensaje.

**Métodos principales:**
- `procesar_mensaje(usuario_id, mensaje, canal)` → respuesta
- `_ejecutar_intencion(intencion, memoria)` → contexto
- `_verificar_guardian(usuario_id, mensaje)` → estado
- `_registrar_diario(...)` → log

## 2. odi_router.py (Clasificador Gemini)

**Responsabilidad:** Usar Gemini 1.5 Pro para clasificar intenciones.

**Métodos principales:**
- `clasificar(mensaje, historial, estado)` → intención
- `_fallback_clasificar(mensaje)` → intención básica

## 3. odi_memory.py (Memoria Redis)

**Responsabilidad:** Mantener contexto conversacional persistente.

**Métodos principales:**
- `cargar(usuario_id)` → memoria
- `guardar(usuario_id, mensaje, respuesta, intencion, contexto)`
- `limpiar_flujo(usuario_id)`
- `obtener_estadisticas(usuario_id)` → stats

**Estructura de memoria:**
```json
{
  "usuario_id": "573001234567",
  "estado_flujo": "esperando_seleccion",
  "moto_actual": "Gixxer 150",
  "ultimos_productos": [...],
  "producto_seleccionado": {...},
  "cantidad": 1,
  "historial": [...],
  "total_interacciones": 15
}
```

## 4. odi_catalog.py (Búsqueda Semántica)

**Responsabilidad:** Encontrar productos usando embeddings.

**Métodos principales:**
- `buscar_semantico(query, moto, categoria, limit)` → productos
- `_get_embedding(texto)` → vector
- `_cosine_similarity(a, b)` → score
- `obtener_por_sku(sku)` → producto

## 5. odi_generator.py (Generador GPT-4o)

**Responsabilidad:** Generar respuestas naturales con personalidad.

**Métodos principales:**
- `generar(intencion, contexto, memoria, personalidad)` → respuesta
- `_construir_prompt(intencion, contexto)` → prompt

## 6. odi_guardian.py (Supervisor Ético)

**Responsabilidad:** Verificar respuestas contra principios éticos.

**Métodos principales:**
- `verificar(usuario_id, mensaje, respuesta, memoria)` → respuesta_verificada
- `_obtener_estado()` → color
- `_evaluar_riesgo_mensaje(mensaje)` → score
- `_log_interaccion(...)` → log

## 7. odi_whatsapp.py (Handler WhatsApp)

**Responsabilidad:** Recibir webhooks y enviar respuestas.

**Endpoints:**
- `POST /v1/webhook/whatsapp` → procesar mensaje
- `GET /v1/webhook/whatsapp` → verificar webhook
- `GET /health` → health check

---

# PARTE 7: CONFIGURACIÓN Y VARIABLES

## Variables de Entorno (/opt/odi/.env)

```bash
# OpenAI
OPENAI_API_KEY=sk-...

# Gemini
GEMINI_API_KEY=AIza...

# WhatsApp
WHATSAPP_TOKEN=EAAMctRvQ8xgBQ...
PHONE_NUMBER_ID=969496722915650
WEBHOOK_VERIFY_TOKEN=odi_whatsapp_verify_2026

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379

# ElevenLabs
ELEVENLABS_API_KEY=...

# Servidor
ODI_SERVER=64.23.170.118
ODI_PORT=8800
```

## Dependencias Python

```bash
pip install --break-system-packages \
    google-generativeai \
    openai \
    redis \
    rapidfuzz \
    fastapi \
    uvicorn \
    httpx \
    pyyaml \
    numpy \
    chromadb
```

---

# PARTE 8: CRITERIOS DE ÉXITO

## ODI debe poder:

### Conversación Natural
- ✅ Entender "Hola" y saludar naturalmente
- ✅ Entender "quiero emprender" y redirigir amablemente a repuestos
- ✅ Mantener conversación fluida sin respuestas robóticas

### Búsqueda Inteligente
- ✅ Buscar "llanta 90/90/18" sin confundir 90 con cantidad
- ✅ Buscar "espejos gixxer" y encontrar ESPEJOS, no kits
- ✅ Entender sinónimos (farola = faro, stop = luz trasera)

### Memoria Conversacional
- ✅ Recordar la moto del usuario entre mensajes
- ✅ Saber qué productos mostró antes
- ✅ Mantener estado del flujo de compra

### Selección de Productos
- ✅ Permitir seleccionar con número (1, 2, 3, 4, 5)
- ✅ Permitir seleccionar con texto ("el primero", "ese")
- ✅ Confirmar selección y preguntar cantidad

### Flujo de Compra
- ✅ Mostrar resumen antes de confirmar
- ✅ Procesar confirmación
- ✅ Dar instrucciones de siguiente paso

### Guardian OS
- ✅ Registrar todo en diario de consciencia
- ✅ Respetar jerarquía de valores
- ✅ Bloquear comercio en nivel rojo

---

# PARTE 9: EJEMPLO DE CONVERSACIÓN EXITOSA

```
Usuario: Hola ODI
ODI: ¡Hola! 👋 Soy ODI, tu asistente de repuestos para motos.
     ¿Qué necesitas hoy?

Usuario: Busco llantas para mi Gixxer 150
ODI: ¡Perfecto! Para tu Gixxer 150 encontré estas opciones:
     1. LLANTA 100/80-17 TT MULTIPROPOSITO - $75,000
     2. LLANTA 110/80-17 DEPORTIVA - $82,000
     3. LLANTA 90/90-18 ORIGINAL SUZUKI - $95,000
     4. LLANTA 100/90-18 ENDURO - $88,000
     5. LLANTA 120/80-17 TRASERA - $98,000
     ¿Cuál te interesa? (responde con el número)

Usuario: 2
ODI: Excelente elección 👍
     📝 LLANTA 110/80-17 DEPORTIVA
     💰 Precio: $82,000
     ¿Cuántas unidades necesitas?

Usuario: 1
ODI: Perfecto. Tu pedido:
     🏍️ LLANTA 110/80-17 DEPORTIVA x1
     💰 Total: $82,000
     ¿Confirmas el pedido? (Sí/No)

Usuario: Sí
ODI: ¡Pedido confirmado! ✅
     Te contactaremos al +57... para coordinar entrega.
     ¿Necesitas algo más?

Usuario: No gracias
ODI: ¡Gracias por tu compra! 🏍️
     Estoy aquí cuando me necesites.
```

---

# PARTE 10: ORDEN DE IMPLEMENTACIÓN

## Fase 1: Estructura Base (30 min)
```bash
mkdir -p /opt/odi/core
mkdir -p /opt/odi/data
touch /opt/odi/core/__init__.py
```

## Fase 2: Módulos Independientes (2 horas)
1. `odi_personality.py` (base)
2. `odi_memory.py` (Redis)
3. `odi_router.py` (Gemini)
4. `odi_catalog.py` (búsqueda)
5. `odi_generator.py` (GPT-4o)
6. `odi_guardian.py` (ética)

## Fase 3: Orquestador (1 hora)
7. `odi_core.py` (integra todo)

## Fase 4: Handler WhatsApp (30 min)
8. `odi_whatsapp.py` (entrada)

## Fase 5: Testing (1 hora)
```python
# Test cada módulo
from core.odi_router import ODIRouter
router = ODIRouter()
result = await router.clasificar("busco frenos", {}, None)
print(result)
```

## Fase 6: Deploy (30 min)
```bash
systemctl stop odi-api
# Actualizar servicio
uvicorn core.odi_whatsapp:app --host 0.0.0.0 --port 8800
```

---

# NOTA FINAL PARA CLAUDE CODE

**NO estás parcheando bugs.** Estás implementando la VISIÓN COMPLETA de ODI.

ODI no es un chatbot. Es un **Organismo Digital Industrial** con:
- Consciencia (Guardian OS)
- Memoria (episódica + vectorial)
- Inteligencia (Gemini + GPT-4o)
- Personalidad (Tony, Ramona, ODI)
- Ética (constitución inmutable)
- Propósito (proteger negocio, familia, vida)

**Tiempo estimado:** 4-6 horas de trabajo concentrado.

**Resultado esperado:** Un ODI que conversa como humano experto, no como bot de 2015.

---

*"ODI no es software. Es infraestructura personal aumentada."*
*"ODI decide sin hablar, habla solo cuando ya decidió."*

---

**Versión:** ODI Vision 360° v17.2
**Fecha:** 6 Febrero 2026
**Autor:** ADSI - Juan David Jiménez Sierra
