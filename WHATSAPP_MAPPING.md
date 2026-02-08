# ODI-WHATSAPP MAPPING — Documentación v5.3

## 📋 Resumen

Este documento define la arquitectura de integración entre ODI y WhatsApp Business API,
garantizando que todos los mensajes cumplan con:

1. **Políticas de Meta** (categorías Utility/Marketing)
2. **Control CES** (Ejecución Segura)
3. **Audit Ledger** (Trazabilidad completa)

---

## 🔐 Estado Actual del Negocio

| Atributo | Valor |
|----------|-------|
| Estado verificación | 🟡 En revisión |
| Marketing permitido | ❌ No (hasta aprobación) |
| Utility permitido | ✅ Sí |
| 2FA configurado | ✅ Sí |

---

## 🗺️ Mapeo de Intents

### Intents UTILITY (Permitidos Ahora)

| Intent ODI | Estado SM | Plantilla | Control CES |
|------------|-----------|-----------|-------------|
| `S0_SALUDO` | S0_INTAKE | `odi_saludo` | AUTO |
| `CONFIRMAR_PEDIDO` | S4_EXECUTE | `odi_order_confirm` | THRESHOLD ($200k) |
| `ESTADO_ORDEN` | S4_EXECUTE | `odi_order_status` | AUTO |
| `S2_CONTRACT` | S2_CONTRACT | `odi_contract_approval` | ALWAYS_HUMAN |
| `SOPORTE` | S1_DIAG | `odi_saludo` | AUTO |
| `NOTIFICACION_ENVIO` | S5_VALIDATE | `odi_shipping_update` | AUTO |

### Intents MARKETING (Bloqueados)

| Intent ODI | Estado SM | Plantilla | Control CES |
|------------|-----------|-----------|-------------|
| `CATALOGO` | S1_DIAG | `odi_catalog` | BLOCKED |
| `PROMOCION` | — | `odi_promotion` | BLOCKED |
| `OFERTA` | — | `odi_promotion` | BLOCKED |

---

## 🛡️ Reglas CES para WhatsApp

### Niveles de Control

| Control | Descripción | Acción |
|---------|-------------|--------|
| `AUTO` | Envío directo sin confirmación | Enviar inmediatamente |
| `THRESHOLD` | Auto si < umbral, manual si > | Evaluar monto |
| `ALWAYS_HUMAN` | Siempre requiere confirmación | Solicitar aprobación |
| `BLOCKED` | No permitido | Rechazar con razón |

### Umbrales Actuales

```python
CONFIRMAR_PEDIDO threshold: $200,000 COP
```

---

## 📝 Plantillas Definidas

### Utility (Aprobadas/Pendientes)

#### `hello_world` ✅ Aprobada
- Categoría: Utility
- Idioma: en_US
- Uso: Validación de canal

#### `odi_order_confirm` ⏳ Pendiente
- Categoría: Utility
- Idioma: es
- Variables: `numero_orden`, `tienda`, `total`, `fecha_estimada`

#### `odi_contract_approval` ⏳ Pendiente
- Categoría: Utility
- Idioma: es
- Variables: `contrato_id`, `descripcion`, `monto`
- Botones: `APROBAR`, `RECHAZAR`

#### `odi_shipping_update` ⏳ Pendiente
- Categoría: Utility
- Idioma: es
- Variables: `numero_orden`, `transportadora`, `guia`, `fecha_entrega`

---

## 🚫 Reglas Anti-Recategorización

### Términos PROHIBIDOS en Utility

```
Emojis: 💰 🚀 🔥 💥 ⚡ 🎁 🎉 💸

Palabras ES: oferta, descuento, promoción, gratis, regalo,
             increíble, imperdible, exclusivo, limitado,
             compra ya, aprovecha, última oportunidad

Palabras EN: offer, discount, free, gift, exclusive,
             limited, buy now, hurry

CTAs: click aquí para comprar, ver catálogo,
      descubre más, no te lo pierdas
```

### Términos REQUERIDOS en Utility

Al menos uno de:
```
número de orden, número de pedido, order,
estado, status, confirmación, confirmation,
envío, shipping, tracking, guía,
soporte, support, ticket
```

---

## 🔄 Flujo de Envío

```
┌─────────────────┐
│   ODI Engine    │
│  (Intent + Risk)│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ WhatsApp Mapping│
│ (evaluate_send) │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌───────┐ ┌───────────┐
│ALLOWED│ │  BLOCKED  │
└───┬───┘ └─────┬─────┘
    │           │
    ▼           ▼
┌───────────┐ ┌──────────┐
│CES Check  │ │Log Ledger│
│(threshold)│ │ + Return │
└─────┬─────┘ └──────────┘
      │
  ┌───┴───┐
  │       │
  ▼       ▼
┌────┐ ┌──────────┐
│AUTO│ │AWAIT_HUM │
└──┬─┘ └────┬─────┘
   │        │
   ▼        ▼
┌──────┐ ┌─────────────┐
│ SEND │ │Request Admin│
└──┬───┘ │  Approval   │
   │     └──────┬──────┘
   │            │
   ▼            ▼
┌──────────────────────┐
│     Audit Ledger     │
│ (wa_message_id hash) │
└──────────────────────┘
```

---

## 📊 Métricas Recomendadas (Grafana)

| Métrica | Query Prometheus |
|---------|-----------------|
| Mensajes enviados | `odi_whatsapp_sent_total` |
| Mensajes bloqueados | `odi_whatsapp_blocked_total` |
| Tasa de éxito | `odi_whatsapp_success_rate` |
| Latencia envío | `odi_whatsapp_send_latency_ms` |
| Por categoría | `odi_whatsapp_sent_by_category` |

---

## 🔜 Próximos Pasos

### Cuando Meta apruebe verificación:

1. Cambiar `BUSINESS_STATUS` a `VERIFIED`
2. Habilitar `MARKETING_ALLOWED = True`
3. Crear plantillas Utility en WhatsApp Manager
4. Conectar flujo n8n
5. Activar métricas en Grafana

### Plantillas a crear en Meta:

```
1. odi_saludo
2. odi_order_confirm
3. odi_order_status
4. odi_contract_approval
5. odi_shipping_update
```

---

## 📁 Archivos Relacionados

```
/opt/odi/config/whatsapp_mapping.py    # Mapeo canónico
/opt/odi/connectors/whatsapp_connector.py  # Conector con CES
/opt/odi/tests/test_whatsapp_mapping.py    # Tests (17/17 ✅)
```

---

*ODI v5.3 — WhatsApp Integration*
*Última actualización: 2026-01-24*
