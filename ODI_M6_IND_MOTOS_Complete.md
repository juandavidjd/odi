# ODI M6.x — DISEÑO COMPLETO: IND_MOTOS DATA LAYER

**Documento:** `ODI_M6_IND_MOTOS_Complete.md`  
**Versión:** 1.0  
**Fecha:** 2026-01-11  
**Autor:** Claude (Arquitecto)  
**Ejecutor:** ChatGPT (Ingeniero)  
**Estado:** DISEÑO APROBADO — PENDIENTE IMPLEMENTACIÓN

---

## 📋 ÍNDICE

1. Definición y Alcance
2. Contratos de Datos
3. Workflows n8n (5 módulos)
4. Integración con ODI Core
5. Checklist de Implementación
6. Casos de Prueba
7. Modificaciones Requeridas a Código Existente

---

## 1. DEFINICIÓN Y ALCANCE

### 1.1 ¿Qué es M6.x?

M6.x es el **Data Layer** de la industria "Repuestos de Motos" dentro del ecosistema ODI. NO es un sistema independiente — es una extensión gobernada por ODI Core.

### 1.2 Responsabilidades de M6.x

| SÍ hace | NO hace |
|---------|---------|
| Carga y normaliza catálogos | Decide sobre ventas |
| Responde consultas de compatibilidad | Registra transacciones financieras |
| Sincroniza productos a Shopify | Bypasea gobernanza ODI |
| Onboarding de usuarios | Genera IDs de venta |
| Enriquece datos con taxonomía | Aplica umbrales o modos |

### 1.3 Fuentes de Datos

```
C:\IND_MOTOS\                      → /opt/odi/data/ind_motos/ (post-migración)
├── taxonomy_motos_v1.json         → Ontología de componentes
├── fitment_master_v1.json         → Catálogo unificado (~4,000+ productos)
├── Catalogos/                     → 111 documentos fuente
├── Imagenes/                      → 6,861 fotos por proveedor
│   ├── Bara/                      → 698 imágenes
│   ├── Imbra/                     → 2,068 imágenes
│   ├── Yokomar/                   → 1,000 imágenes
│   └── ...
└── Manuales/                      → 48 documentos técnicos
```

---

## 2. CONTRATOS DE DATOS

### 2.1 Producto Canónico (fitment_master item)

```json
{
  "sku_ref": "string",
  "title": "string",
  "client": "Bara|DFG|Duna|Imbra|Japan|Kaiqi|Leo|Store|Vaisand|Yokomar",
  "taxonomy": {
    "system": "Frenos|Transmisión|Motor|Suspensión|Iluminación|Carrocería|...",
    "subsystem": "string",
    "component": "string"
  },
  "fitment": {
    "canonical": [
      {
        "marca": "HONDA|YAMAHA|SUZUKI|BAJAJ|AKT|TVS|GENERICA|...",
        "modelo": "string",
        "cilindraje": "string",
        "posicion": "Delantero|Trasero|N/A",
        "lado": "Izquierdo|Derecho|Ambos|N/A"
      }
    ],
    "source": "canonico_json|manual|ocr|ai_inferred"
  },
  "confidence": 0.0-1.0,
  "price": number,
  "currency": "COP",
  "price_method": "catalog|manual|inferred|none"
}
```

### 2.2 Query de Compatibilidad (input M6.2)

```json
{
  "marca": "string (requerido o inferido)",
  "modelo": "string (opcional)",
  "cilindraje": "string (opcional)",
  "sistema": "string (opcional, filtra taxonomía)",
  "componente": "string (opcional, búsqueda fuzzy)",
  "canal": "whatsapp|voz|web",
  "user_id": "string (opcional)"
}
```

### 2.3 Respuesta de Compatibilidad (output M6.2)

```json
{
  "status": "ok|error",
  "query_id": "M6-YYYYMMDD-XXXXXX",
  "query": { ... },
  "results_count": number,
  "results": [
    {
      "sku_ref": "string",
      "title": "string",
      "price": number,
      "client": "string",
      "confidence": number,
      "image_url": "string|null"
    }
  ],
  "response_text": "string (humanizado para voz/chat)"
}
```

### 2.4 Evento de Auditoría M6 (log en Sheets)

```json
{
  "event_id": "M6-YYYYMMDD-XXXXXX",
  "timestamp": "ISO8601",
  "action": "CATALOG_UPLOAD|FITMENT_QUERY|SYNC_SHOPIFY|USER_PUBLISH",
  "client": "string|null",
  "items_processed": number,
  "source": "manual|automated|api",
  "operator": "string|null"
}
```

---

## 3. WORKFLOWS N8N

### 3.1 M6.1 — Carga de Catálogo

**Trigger:** `POST /webhook/catalog-upload`

**Input:**
```json
{
  "client": "Bara",
  "file_type": "csv|json|image_batch",
  "data": "base64 o array de items",
  "operator": "juan.david"
}
```

**Proceso:**
1. Validar cliente existe en lista de proveedores
2. Parsear contenido según file_type
3. Normalizar cada item al contrato de producto
4. Enriquecer con taxonomía (matching fuzzy)
5. Asignar SKU si no existe
6. Append a fitment_master_v1.json
7. Log en Sheets (hoja M6_AUDITORIA)

**Output:**
```json
{
  "status": "ok",
  "event_id": "M6-20260111-ABC123",
  "items_processed": 150,
  "items_success": 148,
  "items_error": 2,
  "errors": [{ "item": "...", "reason": "..." }]
}
```

---

### 3.2 M6.2 — Fitment Engine

**Trigger:** `POST /webhook/fitment-query`

**Input:** Ver contrato 2.2

**Proceso:**
1. Normalizar query (uppercase marca, trim espacios)
2. Cargar fitment_master_v1.json
3. Filtrar por marca → modelo → cilindraje → sistema → componente
4. Rankear por confidence y relevancia
5. Limitar a 10 resultados
6. Formatear response_text según canal
7. Si canal == "voz", enviar a ODI Voice

**Output:** Ver contrato 2.3

---

### 3.3 M6.3 — Sync Shopify

**Trigger:** Cron (diario 3am) o `POST /webhook/sync-shopify`

**Proceso:**
1. Leer fitment_master_v1.json (status: active)
2. GET productos actuales de Shopify
3. Comparar por SKU:
   - Nuevo → Shopify POST product
   - Existente con cambios → Shopify PUT product
   - Discontinuado → Shopify PUT status=draft
4. Subir imágenes nuevas a Shopify CDN
5. Crear metafields con fitment canónico
6. Log de operaciones

**Mapeo Shopify:**
| Shopify | fitment_master |
|---------|----------------|
| title | title |
| vendor | client |
| product_type | taxonomy.system |
| tags | taxonomy.subsystem + marcas |
| variants[0].sku | sku_ref |
| variants[0].price | price |
| metafields.fitment | fitment.canonical (JSON) |

---

### 3.4 M6.4 — Voz + Fitment

NO es workflow separado. Es extensión de M6.2 que:
- Detecta `canal == "voz"`
- Formatea mensaje coloquial
- Envía a `http://localhost:7777/odi/voice-response`
- Usa intent `FITMENT_QUERY` (requiere modificación a voice assistant)

---

### 3.5 M6.5 — Publicación de Usuario

**Trigger:** `POST /webhook/user-publish`

**Input:**
```json
{
  "user_id": "user_123",
  "business_name": "Repuestos El Tigre",
  "industry": "motos",
  "offering_type": "product|service|package",
  "items": [...],
  "wants_store": true
}
```

**Proceso:**
1. Validar/crear usuario
2. Clasificar items con taxonomía
3. Generar landing con template industria
4. Si wants_store → crear subtienda Shopify
5. Conectar con ODI para eventos de venta
6. Notificar URLs al usuario

---

## 4. INTEGRACIÓN CON ODI CORE

### 4.1 Eventos que pasan a ODI Core

| Evento | ¿Pasa a ODI? | Razón |
|--------|--------------|-------|
| FITMENT_QUERY | ❌ No | Solo informativo |
| CATALOG_UPLOAD | ❌ No | Solo data |
| SYNC_SHOPIFY | ❌ No | Solo publicación |
| USER_PUBLISH | ❌ No | Solo onboarding |
| VENTA desde Shopify | ✅ SÍ | Transacción financiera |
| Intención de compra detectada | ✅ SÍ | Requiere gobernanza |

### 4.2 Cómo M6 detecta intención de compra

Cuando usuario dice: "Quiero ese" / "Me lo llevo" / "Regístralo"

M6 envía a ODI Core:
```json
POST http://localhost:5678/webhook/odi-v16-5-action
{
  "sku": "SKU del producto",
  "producto": "Nombre del producto",
  "intent": "VENTA_CONFIRMADA",
  "origen": "M6_FITMENT",
  "precio_catalogo": 6100,
  "precio_final": 6100
}
```

ODI Core aplica:
- Gobernanza SKU
- Umbral $200K
- Modo AUTO/SUPER
- Auditoría Sheets
- Voz de confirmación

---

## 5. CHECKLIST DE IMPLEMENTACIÓN

### Fase 1: Preparación (antes de implementar)

```
□ 1.1  Verificar fitment_master_v1.json es válido JSON
       $ python -m json.tool < fitment_master_v1.json > /dev/null

□ 1.2  Verificar taxonomy_motos_v1.json es válido JSON
       $ python -m json.tool < taxonomy_motos_v1.json > /dev/null

□ 1.3  Contar productos por proveedor
       $ grep -o '"client": "[^"]*"' fitment_master_v1.json | sort | uniq -c

□ 1.4  Crear hoja M6_AUDITORIA en Google Sheets (mismo doc ODI)
       Columnas: event_id, timestamp, action, client, items_processed, operator
```

### Fase 2: Estructura de Archivos (post-migración Linux)

```
□ 2.1  Crear directorio
       $ mkdir -p /opt/odi/data/ind_motos

□ 2.2  Copiar archivos
       $ cp taxonomy_motos_v1.json /opt/odi/data/ind_motos/
       $ cp fitment_master_v1.json /opt/odi/data/ind_motos/

□ 2.3  Permisos
       $ chown -R odi:odi /opt/odi/data/ind_motos
       $ chmod 644 /opt/odi/data/ind_motos/*.json
```

### Fase 3: Workflows n8n

```
□ 3.1  Importar M6.2 Fitment Engine
       → Archivo: M6_2_Fitment_Engine.json
       → n8n UI → Import → Activate

□ 3.2  Probar M6.2
       $ curl -X POST http://localhost:5678/webhook/fitment-query \
         -H "Content-Type: application/json" \
         -d '{"marca": "HONDA", "modelo": "CB150", "sistema": "Frenos"}'

□ 3.3  Implementar M6.1 (Carga Catálogo) - ChatGPT

□ 3.4  Implementar M6.3 (Sync Shopify) - ChatGPT

□ 3.5  Implementar M6.5 (User Publish) - ChatGPT
```

### Fase 4: Modificación Voice Assistant

```
□ 4.1  Agregar handler para FITMENT_QUERY en odi_voice_assistant.py
       Ver sección 7 de este documento

□ 4.2  Probar integración voz
       $ curl -X POST http://localhost:5678/webhook/fitment-query \
         -H "Content-Type: application/json" \
         -d '{"marca": "HONDA", "modelo": "CB150", "canal": "voz"}'
```

### Fase 5: Validación Final

```
□ 5.1  Test completo M6.2 con datos reales
□ 5.2  Verificar log en Sheets M6_AUDITORIA
□ 5.3  Verificar voz responde correctamente
□ 5.4  Test de carga: 100 queries en 1 minuto
```

---

## 6. CASOS DE PRUEBA

### Test 1: Búsqueda por marca exacta
```json
// Input
{"marca": "HONDA", "canal": "web"}

// Expected
- results_count > 0
- Todos los resultados tienen marca HONDA o GENERICA
```

### Test 2: Búsqueda por marca + modelo
```json
// Input
{"marca": "HONDA", "modelo": "CB150", "canal": "web"}

// Expected
- results_count > 0
- Todos los resultados compatibles con CB150
```

### Test 3: Búsqueda sin resultados
```json
// Input
{"marca": "FERRARI", "canal": "web"}

// Expected
- results_count == 0
- response_text contiene "No encontré"
```

### Test 4: Canal voz
```json
// Input
{"marca": "HONDA", "modelo": "CB150", "canal": "voz"}

// Expected
- Llamada exitosa a localhost:7777
- Voice assistant genera audio
```

### Test 5: Búsqueda por componente
```json
// Input
{"marca": "HONDA", "componente": "pastilla", "canal": "web"}

// Expected
- results_count > 0
- Todos los resultados son pastillas de freno
```

---

## 7. MODIFICACIONES A CÓDIGO EXISTENTE

### 7.1 odi_voice_assistant.py — Agregar FITMENT_QUERY

Agregar en `generate_response_message()`:

```python
def generate_response_message(intent, modo, producto, precio, mensaje_custom=None):
    """
    Genera el mensaje apropiado según la intención y modo de operación.
    """
    # NUEVO: Soporte para mensaje custom (fitment queries)
    if mensaje_custom:
        return mensaje_custom
    
    if modo == "AUTOMATICO" and intent == "VENTA_CONFIRMADA":
        return f"Listo. Registré {producto} por {precio:,} pesos.".replace(",", ".")
    elif intent == "VENTA_DESCONOCIDA":
        return "Eso no me cuadra. Lo dejé registrado para que lo revisen."
    elif intent == "FITMENT_QUERY":  # NUEVO
        return f"Consulta registrada para {producto}."
    elif modo == "SUPERVISADO":
        return f"El {producto} pasó a supervisión por seguridad."
    else:
        return f"Operación registrada: {producto}."
```

Agregar en `voice_response()`:

```python
# Extraer campos del payload (con defaults seguros)
intent = data.get("intent", "VENTA_DESCONOCIDA")
modo = data.get("modo", "SUPERVISADO")
producto = data.get("producto", "el producto")
precio = data.get("precio_final", 0)
odi_event_id = data.get("odi_event_id", "")
mensaje_custom = data.get("mensaje_custom")  # NUEVO

# Generar mensaje apropiado
mensaje = generate_response_message(intent, modo, producto, precio, mensaje_custom)
```

---

## 8. NOTAS FINALES

### Orden de Implementación Recomendado

1. **M6.2** (Fitment Engine) — Más útil inmediatamente
2. **Modificación Voice** — Habilita canal voz
3. **M6.1** (Carga Catálogo) — Para actualizar datos
4. **M6.3** (Sync Shopify) — Para publicar en tienda
5. **M6.5** (User Publish) — Para onboarding

### Dependencias

- M6.x requiere Linux (P0) completado para paths correctos
- M6.x NO toca M1.x (ODI Core)
- M6.x usa misma instancia n8n que ODI

### Restricción Crítica

```
╔═══════════════════════════════════════════════════════════════════════════╗
║  M6.x NUNCA bypasea ODI Core para transacciones financieras.             ║
║  Toda venta pasa por webhook /odi-v16-5-action existente.                ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

**FIN DEL DOCUMENTO**
