# 🔌 INSTRUCCIONES CLAUDE CODE: Conectar Sensores n8n
## Sistema Nervioso ODI - Billing v1.0

---

## CONTEXTO

El sistema de billing está funcionando (`billing listo` confirmado):

```json
{
  "score_intervencion": 0.2,
  "porcentaje_applied": 0.038,
  "odi_commission": 7030.0,
  "estado_etico_al_momento": "verde"
}
```

Pero el score es bajo (0.2) porque solo detecta el canal.
Necesitamos conectar los **sensores** para medir esfuerzo real.

---

## OBJETIVO

Conectar n8n para que envíe métricas de conversación a `odi_billing.py`:

```
WhatsApp/Vapi → n8n (métricas) → odi_billing.py → ledger_odi.json
```

Con sensores conectados, el score pasará de 0.2 a **0.5-0.9** basado en esfuerzo medido.

---

## PASO 1: Crear nodo `prepare_odi_metrics` en n8n

En el workflow donde Ramona/Tony atienden WhatsApp, agrega un nodo **Set** antes del webhook de billing.

### Nombre del nodo:
```
prepare_odi_metrics
```

### Campos a crear:

```json
{
  "odi_session_id": "={{$json.session_id || $json.chat_id || $json.conversation_id}}",
  "num_mensajes": "={{$json.message_count || $json.messages?.length || 0}}",
  "duracion_sesion_seg": "={{$json.session_duration || $json.duration_seconds || 0}}",
  "consultas_fitment": "={{$json.fitment_queries || $json.compatibility_checks || 0}}",
  "consultas_stock": "={{$json.stock_queries || $json.inventory_checks || 0}}",
  "consultas_precio": "={{$json.price_queries || $json.price_comparisons || 0}}",
  "abandono_previo": "={{$json.cart_abandoned || $json.was_abandoned || false}}",
  "reintento_pago": "={{$json.retry_payment || $json.payment_retry || false}}",
  "cambio_producto": "={{$json.product_changed || false}}",
  "odi_checkout": "={{$json.odi_checkout || $json.checkout_by_odi || false}}",
  "canal": "={{$json.channel || 'whatsapp'}}"
}
```

### Notas:
- Algunos campos pueden llegar en 0 inicialmente - está bien
- El modelo aprenderá progresivamente
- Lo importante es que la estructura esté lista

---

## PASO 2: Webhook de Shopify (order/paid)

### 2.1 Crear/Verificar Webhook en Shopify Admin:

```
Settings → Notifications → Webhooks → Create webhook

Event: Order payment
Format: JSON
URL: http://64.23.170.118:5678/webhook/shopify_odi_paid
```

### 2.2 En n8n - Nodo Webhook:

```yaml
Path: shopify_odi_paid
Method: POST
```

### 2.3 Nodo IF (Filtro de atribución):

Solo procesar si tiene tag ODI:

```javascript
{{$json.tags && $json.tags.includes("ODI")}}
```

**Si no tiene tag ODI → No procesar → No hay mérito.**

---

## PASO 3: Merge de ramas

Usar nodo **Merge** para combinar:
- Rama Shopify (datos de venta)
- Rama Conversacional (métricas ODI)

### Configuración:

```yaml
Mode: Merge By Key
Key: odi_session_id
```

### Resultado del merge:

```json
{
  // De Shopify
  "id": "ORDER-12345",
  "total_price": "185000",
  "line_items": [...],
  "tags": "ODI",
  
  // De WhatsApp/Vapi
  "odi_session_id": "abc123",
  "num_mensajes": 12,
  "duracion_sesion_seg": 420,
  "consultas_fitment": 2,
  "consultas_stock": 1,
  "consultas_precio": 0,
  "abandono_previo": true,
  "odi_checkout": true,
  "canal": "whatsapp"
}
```

---

## PASO 4: Execute Command a odi_billing.py

### Nodo Execute Command:

```bash
echo '{{JSON.stringify($json)}}' | python3 /opt/odi/billing/odi_billing.py
```

### Alternativa (más robusta):

```bash
python3 /opt/odi/billing/odi_billing.py '{{JSON.stringify($json)}}'
```

---

## PASO 5: Verificar en odi_billing.py

Asegúrate que `odi_billing.py` lea el evento correctamente:

```python
import sys
import json

# Leer de stdin o argumento
if len(sys.argv) > 1:
    evento = json.loads(sys.argv[1])
else:
    evento = json.loads(sys.stdin.read())

# Extraer monto
monto = float(evento.get("total_price", 0))
if not monto:
    monto = float(evento.get("valor", 0))
```

---

## PASO 6: Tracking de métricas en el flujo ODI

Para que `num_mensajes`, `duracion_sesion_seg`, etc. tengan valores reales, necesitas trackear durante la conversación.

### En el flujo de WhatsApp (odi_core.py o similar):

```python
# Al inicio de sesión
session_start = datetime.now()
message_count = 0
fitment_queries = 0
stock_queries = 0

# Durante la conversación
message_count += 1

# Si ODI verificó compatibilidad
if intencion.tipo == "consultar_fitment":
    fitment_queries += 1

# Si ODI verificó stock
if intencion.tipo == "consultar_stock":
    stock_queries += 1

# Al final (cuando hay pedido confirmado)
session_data = {
    "odi_session_id": session_id,
    "num_mensajes": message_count,
    "duracion_sesion_seg": (datetime.now() - session_start).seconds,
    "consultas_fitment": fitment_queries,
    "consultas_stock": stock_queries,
    "odi_checkout": True,
    "canal": "whatsapp"
}

# Guardar en Redis para que n8n lo lea
redis_client.setex(f"odi:session:{session_id}", 3600, json.dumps(session_data))
```

### En n8n, leer de Redis:

Nodo **Redis** → GET `odi:session:{{$json.odi_session_id}}`

---

## ARQUITECTURA COMPLETA

```
┌─────────────────────────────────────────────────────────────────┐
│                     CLIENTE (WhatsApp)                          │
└─────────────────────────────────┬───────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                     ODI CORE (odi_core.py)                      │
│                                                                 │
│   • Procesa mensajes                                            │
│   • Trackea: num_mensajes, consultas_fitment, etc.              │
│   • Guarda session_data en Redis                                │
└─────────────────────────────────┬───────────────────────────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ▼                           ▼
        ┌───────────────────┐       ┌───────────────────┐
        │  Redis (session)  │       │ Shopify (order)   │
        │                   │       │                   │
        │ odi:session:xyz   │       │ tag: ODI          │
        └─────────┬─────────┘       └─────────┬─────────┘
                  │                           │
                  └───────────┬───────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     n8n (Orquestador)                           │
│                                                                 │
│   1. Webhook Shopify (order/paid)                               │
│   2. IF: tags.includes("ODI")                                   │
│   3. Redis: GET session_data                                    │
│   4. Set: prepare_odi_metrics                                   │
│   5. Merge: Shopify + Session                                   │
│   6. Execute: odi_billing.py                                    │
└─────────────────────────────────┬───────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                     odi_billing.py                              │
│                                                                 │
│   • calcular_score(evento)                                      │
│   • score_a_porcentaje(score)                                   │
│   • registrar_en_ledger()                                       │
└─────────────────────────────────┬───────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                     ledger_odi.json                             │
│                                                                 │
│   {                                                             │
│     "score_intervencion": 0.73,                                 │
│     "porcentaje_aplicado": 0.0592,                              │
│     "odi_commission": 10952,                                    │
│     ...                                                         │
│   }                                                             │
└─────────────────────────────────────────────────────────────────┘
```

---

## VALIDACIÓN

### Test 1: Verificar n8n recibe webhook

```bash
# En el servidor, ver logs de n8n
docker logs n8n --tail 50
```

### Test 2: Verificar evento llega a billing

```bash
# Crear orden test en Shopify con tag ODI
# Luego verificar ledger:
tail -n 1 /opt/odi/billing/ledger_odi.json
```

### Test 3: Verificar score mejorado

Con métricas reales, debes ver:

```json
{
  "score_intervencion": 0.65,  // Antes era 0.2
  "porcentaje_aplicado": 0.056,
  "num_mensajes": 12,
  "duracion_sesion_seg": 420
}
```

---

## RESULTADO ESPERADO

| Escenario | Score Antes | Score Después |
|-----------|-------------|---------------|
| Venta simple | 0.20 | 0.20 |
| + 10 mensajes | 0.20 | 0.29 |
| + 5 min conversación | 0.20 | 0.33 |
| + consulta fitment | 0.20 | 0.38 |
| + rescate carrito | 0.20 | 0.51 |
| + cierre autónomo | 0.20 | 0.66 |
| **Full intervención** | 0.20 | **0.85** |

---

## CONFIRMACIÓN

Cuando esté listo, responde:

```
sensores conectados
```

---

*Documento: CLAUDE_CODE_CONECTAR_N8N_BILLING.md*
*Versión: 1.0*
*Fecha: 6 Febrero 2026*
