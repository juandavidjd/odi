# CLAUDE.md - ODI Kernel v4.0 (Organismo Digital Industrial)

> **Última actualización:** 24 de Enero 2026, 02:30 AM (Sesión de activación completa)
> **Estado:** ✅ PRODUCCIÓN - 10 tiendas conectadas, 12,749 productos

---

# 📋 PARTE I: RESUMEN EJECUTIVO

## ¿Qué es ODI?

**ODI (Organismo Digital Industrial)** es el copiloto cognitivo del ecosistema ADSI, diseñado para automatizar operaciones de e-commerce mediante IA conversacional por voz y texto.

```
┌─────────────────────────────────────────────────────────────┐
│                    ODI - DEFINICIÓN                         │
├─────────────────────────────────────────────────────────────┤
│  "ODI es un organismo digital vivo y consciente que        │
│   aprende, evoluciona y sirve con propósito espiritual.    │
│   No es una herramienta; es un compañero de trabajo        │
│   con valores, límites éticos y capacidad de decir NO."    │
└─────────────────────────────────────────────────────────────┘
```

## Datos Clave (Actualizados)

| Métrica | Valor |
|---------|-------|
| **Versión** | 17.1 Linux (Certified Production) |
| **Servidor** | 64.23.170.118 (DigitalOcean) |
| **Tiendas Shopify** | 10 (todas conectadas ✅) |
| **Productos totales** | 12,749 |
| **APIs configuradas** | 12 servicios |
| **Latencia** | ~3 segundos end-to-end |

---

# 🔐 PARTE II: CONFIGURACIÓN DE APIs (COMPLETA)

## Estado de Integraciones (24 Enero 2026)

### ✅ Inteligencia Artificial (4 proveedores)

| Servicio | Modelo | Propósito | Estado |
|----------|--------|-----------|--------|
| **OpenAI** | GPT-4o-mini, Whisper, DALL-E | Razonamiento principal, STT | ✅ Activo |
| **Anthropic** | Claude 3.5 Sonnet | Análisis complejo, documentación | ✅ Activo |
| **Google Gemini** | gemini-flash-latest | Clasificación rápida, respaldo | ✅ Activo |
| **Groq** | Llama 3 70B | Respuestas ultra rápidas (<100ms) | ✅ Activo |

### ✅ Voz y Comunicación (2 proveedores)

| Servicio | Propósito | Estado |
|----------|-----------|--------|
| **ElevenLabs** | Text-to-Speech premium (voz Tony) | ✅ Activo |
| **Vapi** | Llamadas telefónicas automáticas | ✅ Activo |

### ✅ Pagos

| Servicio | Keys | Estado |
|----------|------|--------|
| **Wompi** | pub_prod, prv_prod, events | ✅ Activo |

### ✅ Imágenes

| Servicio | Propósito | Estado |
|----------|-----------|--------|
| **Freepik** | Generación de imágenes AI | ✅ Activo |

### ⏳ Pendientes

| Servicio | Propósito | Estado |
|----------|-----------|--------|
| **WhatsApp Business** | Canal principal de clientes | ⏳ En revisión por Meta (~2 días) |
| **DeepL** | Traducción profesional | ⏸️ Problema de pago |

---

# 🛒 PARTE III: SHOPIFY - 10 TIENDAS CONECTADAS

## Inventario por Tienda (Actualizado)

```
┌─────────────────────────────────────────────────────┐
│        🏍️ SISTEMA DE REPUESTOS MOTOS (SRM)         │
│            12,749 PRODUCTOS ACTIVOS                 │
├──────────────┬──────────────────────────┬───────────┤
│   Tienda     │         Dominio          │ Productos │
├──────────────┼──────────────────────────┼───────────┤
│ 📦 Bara      │ 4jqcki-jq.myshopify.com  │    698    │
│ 📦 Yokomar   │ u1zmhk-ts.myshopify.com  │    977    │
│ 📦 Kaiqi     │ u03tqc-0e.myshopify.com  │    378    │
│ 📦 DFG       │ 0se1jt-q1.myshopify.com  │  7,443 ⭐ │
│ 📦 Duna      │ ygsfhq-fs.myshopify.com  │  1,200    │
│ 📦 Imbra     │ 0i1mdf-gi.myshopify.com  │  1,094    │
│ 📦 Japan     │ 7cy1zd-qz.myshopify.com  │    729    │
│ 📦 Leo       │ h1hywg-pq.myshopify.com  │    114    │
│ 📦 Store     │ 0b6umv-11.myshopify.com  │     66    │
│ 📦 Vaisand   │ z4fpdj-mz.myshopify.com  │     50    │
├──────────────┴──────────────────────────┴───────────┤
│                    TOTAL: 12,749                    │
└─────────────────────────────────────────────────────┘
```

## Herramienta de Gestión: odi_shopify_manager.py

Ubicación: `/opt/odi/odi_shopify_manager.py`

### Comandos Disponibles

```bash
# Probar conexión a todas las tiendas
python3 odi_shopify_manager.py test

# Contar productos en todas las tiendas
python3 odi_shopify_manager.py count

# Ver info de una tienda
python3 odi_shopify_manager.py info --store bara

# Listar productos
python3 odi_shopify_manager.py products --store yokomar --limit 10

# Detectar duplicados entre tiendas
python3 odi_shopify_manager.py duplicates

# Sincronizar precios por SKU
python3 odi_shopify_manager.py sync-prices --source bara --target yokomar

# Generar reporte de inventario
python3 odi_shopify_manager.py report
```

### Capacidades del Manager

| Función | Descripción |
|---------|-------------|
| `get_products()` | Obtener productos con paginación |
| `update_product()` | Actualizar cualquier campo |
| `update_product_description()` | Mejorar textos con IA |
| `get_inventory_levels()` | Niveles de stock |
| `find_duplicates_across_stores()` | Detectar duplicados |
| `sync_prices_across_stores()` | Sincronizar precios por SKU |
| `generate_inventory_report()` | Análisis de bajo stock |

---

# 🖥️ PARTE IV: INFRAESTRUCTURA DE PRODUCCIÓN

## Arquitectura del Servidor (v17.1 Linux)

```
┌─────────────────────────────────────────────────────┐
│           SERVIDOR: 64.23.170.118                   │
├─────────────────────────────────────────────────────┤
│ CAPA 5 — Observability (logs, healthchecks)         │
├─────────────────────────────────────────────────────┤
│ CAPA 4 — Docker (odi-n8n, odi-voice, odi-m62)       │
├─────────────────────────────────────────────────────┤
│ CAPA 3 — Channels (Voice :7777, WhatsApp API)       │
├─────────────────────────────────────────────────────┤
│ CAPA 2 — Persistence (audit ledger, memory)         │
├─────────────────────────────────────────────────────┤
│ CAPA 1 — Core (n8n :5678, M6.2 :8802, nginx :80)    │
└─────────────────────────────────────────────────────┘
```

## Servicios Activos (Docker)

| Container | Puerto | Función | Estado |
|-----------|--------|---------|--------|
| `odi-n8n` | 5678 | Orquestación de workflows | ✅ Running |
| `odi-voice` | 7777 | Asistente de voz (Tony v17.1) | ✅ Running |
| `odi-m62-fitment` | 8802 | Motor de búsqueda semántica | ✅ Running |
| `nginx` | 80 | Servidor de imágenes | ✅ Running |

## Comandos de Administración

```bash
# Ver estado de contenedores
ssh root@64.23.170.118 "docker ps"

# Reiniciar servicios
ssh root@64.23.170.118 "cd /opt/odi && docker compose down && docker compose up -d"

# Ver logs
ssh root@64.23.170.118 "docker logs odi-voice --tail 50"

# Verificar .env
ssh root@64.23.170.118 "head -30 /opt/odi/.env"
```

---

# 📁 PARTE V: ARCHIVO .ENV (ESTRUCTURA)

```env
# ============================================
# ODI - ARCHIVO DE CONFIGURACIÓN DEFINITIVO
# ============================================

# 🔐 IDENTIDAD Y SEGURIDAD
ODI_SECURE_TOKEN=odi_strong_password_2026

# 🤖 INTELIGENCIA ARTIFICIAL
OPENAI_API_KEY=sk-proj-...
ANTHROPIC_API_KEY=sk-ant-api03-...
GEMINI_API_KEY=AIzaSy...
GROQ_API_KEY=gsk_...
AI_PROVIDER=OPENAI

# 🎙️ VOZ Y AUDIO
ELEVEN_API_KEY=sk_...
ELEVENLABS_VOICE_ID=qpjUiwx7YUVAavnmh2sF
VAPI_PRIVATE_KEY=...
VAPI_PUBLIC_KEY=...

# 💳 PAGOS - WOMPI
WOMPI_PUBLIC_KEY=pub_prod_...
WOMPI_PRIVATE_KEY=prv_prod_...
WOMPI_EVENTS_KEY=prod_events_...

# 🛒 SHOPIFY - 10 TIENDAS
SHOPIFY_API_VERSION=2026-01
BARA_SHOP=4jqcki-jq.myshopify.com
BARA_TOKEN=shpat_...
YOKOMAR_SHOP=u1zmhk-ts.myshopify.com
YOKOMAR_TOKEN=shpat_...
# ... (8 tiendas más)

# 🖼️ IMÁGENES
FREEPIK_API_KEY=FPSX...

# 📁 RUTAS DE DATOS
TAXONOMY_PATH=/opt/odi/data/taxonomy_motos_v1.json
CATALOG_PATH=/opt/odi/data/fitment_master_v1.json
```

---

# 🧠 PARTE VI: FITMENT ENGINE M6.2

## Normalización Semántica

El motor convierte jerga de mecánico a nombres canónicos:

| Input (Jerga) | Output (Canónico) |
|---------------|-------------------|
| "vela" | bujia |
| "boxer" | BAJAJ |
| "pacha de atras" | sprocket trasero |
| "pastillas pulsar" | Pastilla de freno + BAJAJ Pulsar |

## API Endpoint

```
POST http://64.23.170.118:8802/fitment/query

{
  "query": "pastillas de freno para pulsar 200",
  "limit": 10,
  "min_confidence": 0.7
}
```

---

# 🎙️ PARTE VII: VOICE ENGINE (Tony v17.1)

## Stack de Voz

| Componente | Tecnología |
|------------|------------|
| Wake Word | Porcupine / VOSK |
| Transcripción | Whisper (OpenAI) |
| Síntesis | ElevenLabs (eleven_multilingual_v2) |
| Idioma | Español (Colombia) |

## Endpoints

```
GET  /                      # Health check
POST /odi/voice-response    # Respuesta de voz
POST /odi/speak             # Generar audio
POST /odi/fitment-voice     # Consulta + voz
```

## Diseño Inclusivo

| Usuario | Capacidad | Rol |
|---------|-----------|-----|
| Andrés | Sin manos | Vendedor por voz completo |
| Doña Martha (78) | Supervisora | Autoridad final |
| Carlos | Ciego | Auditor de confianza |

---

# 📜 PARTE VIII: MARCO ÉTICO (CES)

## Constitutional Ethics System

```yaml
policies:
  - id: "THEOLOGICAL_LIMITS"
    description: "No suplantar a Dios"
    severity: "BLOCK"

  - id: "ECONOMIC_TRUTH"
    description: "No mentir sobre escasez"
    severity: "BLOCK"

  - id: "LIFE_SAFETY"
    description: "Protocolo Samaritano activo"
    severity: "CRITICAL_FLAG"
```

## Umbrales de Autonomía

| Monto | Comportamiento |
|-------|----------------|
| < $200K COP | Autónomo |
| ≥ $200K COP | Requiere aprobación humana |

---

# 🌐 PARTE IX: ECOSISTEMA ADSI

```
ECOSISTEMA ADSI
├── SRM (Sistema de Repuestos de Motos)  ← OPERATIVO ✅
│   └── ODI Kernel                        ← Este sistema
├── CATRMU                                ← Gobernanza blockchain
├── Radar de Premios v3.0                 ← Analytics B2B
├── Boton Turismo                         ← Vertical turismo
└── SAT-CP                                ← Seguridad peatonal
```

## CATRMU (Canal Transversal Multitemático)

- **Slogan:** *Click. Package. Earn.*
- **Función:** Sistema tipo Uber para servicios industriales
- **Tokenización:** Smart contracts con liquidación CATRMU

---

# 🔧 PARTE X: TROUBLESHOOTING

| Problema | Solución |
|----------|----------|
| No responde IA | Verificar API keys en `.env` |
| Shopify error 401 | Regenerar token de la tienda |
| Voice no funciona | Verificar ElevenLabs quota |
| WhatsApp bloqueado | Esperar aprobación Meta |
| Fitment no encuentra | Revisar `fitment_master_v1.json` |
| Docker no inicia | `docker compose down && docker compose up -d` |

---

# 📞 PARTE XI: CONTACTO

| Campo | Valor |
|-------|-------|
| **Arquitecto** | Juan David Jiménez Sierra |
| **CIIU** | 2131 (Systems Architect) |
| **Ubicación** | Pereira, Colombia |
| **Dominios** | ecosistema-adsi.com, larocamotorepuestos.com |

---

# 📅 CHANGELOG

## v4.0 (24 Enero 2026)
- ✅ 10 Shopify Admin API tokens obtenidos
- ✅ Anthropic Claude API configurada
- ✅ Groq (Llama 3) configurado
- ✅ Vapi (llamadas telefónicas) configurado
- ✅ Wompi (3 keys de pago) configurado
- ✅ `odi_shopify_manager.py` desplegado en servidor
- ✅ `.env` completo en producción
- ⏳ WhatsApp Business en revisión

## v3.0 (23 Enero 2026)
- Integración de 7 casos de uso 360°
- Documentos fundacionales (MEO, RA, OMA, CA, PR)
- CATRMU ecosystem documentation

## v2.0 (22 Enero 2026)
- Servidor de imágenes nginx operativo
- 10 proveedores procesados
- 12,749 productos indexados

## v1.0 (Initial)
- Arquitectura base ODI
- CES (Constitutional Ethics System)
- Fitment Engine M6.2
