# CHECKLIST_CES_VERIFICATION.md
# ODI — Verificación de Simetría Código ↔ Documentación
# Versión: 5.2 | Fecha: 2026-01-24
# Estado: PRE-CORRECCIÓN MASIVA

---

## 🎯 Objetivo

Garantizar que **CADA umbral, constante y comportamiento** definido en CLAUDE.md v5.2
esté implementado **exactamente igual** en el código, sin defaults silenciosos.

---

## ✅ SECCIÓN 1: Umbrales CES (Control de Ejecución Segura)

### Archivo: `connectors/decorators/require_human_confirmation.py`

| Línea | Variable | CLAUDE.md | Código | Estado |
|-------|----------|-----------|--------|--------|
| 69 | `order_auto_approve` | $200,000 COP | `200000` | ✅ MATCH |
| 70 | `payment_auto_approve` | $100,000 COP | `100000` | ✅ MATCH |
| 71 | `price_change_auto_approve` | 10% | `0.10` | ✅ MATCH |
| 72 | `inventory_bulk_threshold` | 50 items | `50` | ✅ MATCH |

### Verificación de Código (Exacto):

```python
# Líneas 68-73 de require_human_confirmation.py
CES_THRESHOLDS = {
    "order_auto_approve": 200000,      # ← $200,000 COP
    "payment_auto_approve": 100000,    # ← $100,000 COP
    "price_change_auto_approve": 0.10, # ← 10%
    "inventory_bulk_threshold": 50,    # ← 50 items
}
```

### ⚠️ Punto Crítico de Uso:

```python
# Línea 175-180: Evaluación de umbral de órdenes
if action_type in [ActionType.SHOPIFY_CREATE_ORDER]:
    threshold = self.thresholds["order_auto_approve"]  # ← USA LA KEY CORRECTA
    if cost > threshold:
        # ... requiere confirmación
```

**RIESGO MITIGADO:** Si alguien escribe `"auto_approve_order"` en lugar de `"order_auto_approve"`, 
Python lanzará `KeyError` en tiempo de ejecución → falla rápida, no silenciosa.

---

## ✅ SECCIÓN 2: Margen Mayorista (Filtro de Precios)

### Archivo: `connectors/shopify_connector.py`

| Línea | Variable | CLAUDE.md | Código | Estado |
|-------|----------|-----------|--------|--------|
| 64 | `MIN_MARGIN_PERCENT` | 15% | `0.15` | ✅ MATCH |

### Verificación de Código (Exacto):

```python
# Línea 64 de shopify_connector.py
MIN_MARGIN_PERCENT = 0.15  # ← 15%
```

### Uso en PriceValidator:

```python
# Línea 187-188
class PriceValidator:
    def __init__(self, min_margin: float = MIN_MARGIN_PERCENT):
        self.min_margin = min_margin  # ← Usa constante, no hardcoded
```

### Cálculo de Precio Mínimo:

```python
# Línea 214-215
def validate(self, new_price, cost_per_item, product_id):
    min_price = cost_per_item * (1 + self.min_margin)  # ← cost × 1.15
    if new_price < min_price:
        raise PriceValidationError(...)
```

**RIESGO MITIGADO:** El margen se calcula dinámicamente desde la constante.
Si alguien cambia `MIN_MARGIN_PERCENT`, el cambio se propaga automáticamente.

---

## ✅ SECCIÓN 3: Acciones que SIEMPRE Requieren Confirmación

### Archivo: `connectors/decorators/require_human_confirmation.py`

| Línea | Acción | CLAUDE.md | Código | Estado |
|-------|--------|-----------|--------|--------|
| 77 | `SHOPIFY_CREATE_ORDER` | Siempre confirmar | ✅ En lista | ✅ MATCH |
| 78 | `SHOPIFY_CANCEL_ORDER` | Siempre confirmar | ✅ En lista | ✅ MATCH |
| 79 | `WOMPI_REFUND` | Siempre confirmar | ✅ En lista | ✅ MATCH |
| 80 | `VERCEL_DEPLOY` | Siempre confirmar | ✅ En lista | ✅ MATCH |

### Verificación de Código:

```python
# Líneas 76-81
ALWAYS_CONFIRM_ACTIONS = [
    ActionType.SHOPIFY_CREATE_ORDER,
    ActionType.SHOPIFY_CANCEL_ORDER,
    ActionType.WOMPI_REFUND,
    ActionType.VERCEL_DEPLOY,
]
```

---

## ✅ SECCIÓN 4: Acciones READ-ONLY (Nunca Requieren Confirmación)

### Archivo: `connectors/decorators/require_human_confirmation.py`

| Línea | Acción | CLAUDE.md | Código | Estado |
|-------|--------|-----------|--------|--------|
| 85 | `SHOPIFY_GET_PRODUCTS` | Read-only | ✅ En lista | ✅ MATCH |
| 86 | `SHOPIFY_GET_PRODUCT` | Read-only | ✅ En lista | ✅ MATCH |

### Verificación de Código:

```python
# Líneas 84-87
READ_ONLY_ACTIONS = [
    ActionType.SHOPIFY_GET_PRODUCTS,
    ActionType.SHOPIFY_GET_PRODUCT,
]
```

---

## ✅ SECCIÓN 5: Parámetros de Voz (Dualidad)

### Archivo: `core/odi_voice_dispatcher.py`

| Variable | CLAUDE.md | Código | Línea | Estado |
|----------|-----------|--------|-------|--------|
| `speed` | 0.85 | `0.85` | ~45 | ✅ MATCH |
| `stability` | 0.65 | `0.65` | ~46 | ✅ MATCH |

### Archivo: `config/settings.py`

| Variable | CLAUDE.md | Código | Estado |
|----------|-----------|--------|--------|
| `VOICE_SPEED` | 0.85 | `0.85` | ✅ MATCH |
| `VOICE_STABILITY` | 0.65 | `0.65` | ✅ MATCH |

---

## ✅ SECCIÓN 6: Mapeo Estado → Voz

### Archivo: `core/odi_voice_dispatcher.py`

| Estado | Voz Esperada | Código | Estado |
|--------|--------------|--------|--------|
| S0_INTAKE | Ramona | `RAMONA_STATES` | ✅ MATCH |
| S1_DIAG | Tony | `TONY_STATES` | ✅ MATCH |
| S2_CONTRACT | Ramona | `RAMONA_STATES` | ✅ MATCH |
| S3_PLAN | Tony | `TONY_STATES` | ✅ MATCH |
| S4_EXECUTE | Tony | `TONY_STATES` | ✅ MATCH |
| S5_VALIDATE | Ramona | `RAMONA_STATES` | ✅ MATCH |
| S6_CLOSE | Ramona | `RAMONA_STATES` | ✅ MATCH |

---

## ✅ SECCIÓN 7: Alertas v1 (Observabilidad)

### Archivo: `docker/prometheus/alerts.yml`

| Alerta | Umbral CLAUDE.md | Umbral Código | Estado |
|--------|------------------|---------------|--------|
| `LowAudioCacheHitRatio` | < 60% | `< 0.60` | ✅ MATCH |
| `HandoffSuccessRateLow` | < 99% | `< 0.99` | ✅ MATCH |
| `TTSCostHighDaily` | > $10 USD | `> 10` | ✅ MATCH |
| `ConversationErrorRateHigh` | > 5% | `> 0.05` | ✅ MATCH |
| `HighPriceAnomalyRate` | > 5% | `> 0.05` | ✅ MATCH |

---

## ⚠️ SECCIÓN 8: Puntos de Riesgo Identificados

### 8.1 Defaults Silenciosos Potenciales

| Archivo | Función | Riesgo | Mitigación |
|---------|---------|--------|------------|
| `shopify_connector.py:187` | `PriceValidator.__init__` | Default param | ✅ Usa `MIN_MARGIN_PERCENT` |
| `require_human_confirmation.py:130` | `CESEvaluator.__init__` | Default thresholds | ✅ Usa `CES_THRESHOLDS` |

### 8.2 Variables de Entorno No Configuradas

| Variable | Default | Producción Requerida |
|----------|---------|---------------------|
| `ODI_MIN_MARGIN` | 0.15 (hardcoded) | ⚠️ Considerar env var |
| `ODI_ORDER_THRESHOLD` | 200000 (hardcoded) | ⚠️ Considerar env var |

**RECOMENDACIÓN:** Para v5.3, mover umbrales CES a `.env` para flexibilidad sin redeploy.

---

## 📋 RESUMEN EJECUTIVO

```
╔══════════════════════════════════════════════════════════════╗
║  VERIFICACIÓN CES v5.2 — RESULTADO FINAL                    ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  Umbrales CES:           4/4 verificados  ✅                 ║
║  Margen mayorista:       1/1 verificado   ✅                 ║
║  Acciones ALWAYS_CONFIRM: 4/4 verificadas ✅                 ║
║  Acciones READ_ONLY:     2/2 verificadas  ✅                 ║
║  Parámetros de voz:      2/2 verificados  ✅                 ║
║  Mapeo estado→voz:       7/7 verificados  ✅                 ║
║  Alertas v1:             5/5 verificadas  ✅                 ║
║                                                              ║
║  TOTAL: 25/25 puntos verificados                             ║
║  ESTADO: ✅ LISTO PARA CORRECCIÓN MASIVA                     ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

## 🔐 FIRMA DE VERIFICACIÓN

- **Verificador:** ODI Engine v5.2
- **Fecha:** 2026-01-24 12:51 UTC
- **Hash de verificación:** SHA256(checklist) = [calculado en runtime]
- **Próximo paso autorizado:** Corrección SRM Store (Opción B)

---

*Este documento certifica la alineación 1:1 entre CLAUDE.md v5.2 y el código de producción.*
