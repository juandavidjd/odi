# ODI MONETIZATION MODEL
## Monetización Simbiótica del Organismo Digital Industrial
### Versión: 1.0 | Estado: Activo bajo Constitución Ética v17.2

---

## 1. Principio Fundacional

> **"ODI no se vende. ODI demuestra. Y luego cobra."**

ODI no se monetiza como software.
ODI se monetiza como **socio operativo**.

### Regla Absoluta:

**ODI solo cobra cuando se cumplen TODAS estas condiciones:**

1. ✅ La venta fue iniciada o cerrada por ODI
2. ✅ El dinero entró realmente (confirmado)
3. ✅ `evaluador_estado != rojo`
4. ✅ `etica.yaml` permite cobro
5. ✅ El usuario sigue activo

**Si falla una → ODI no cobra.**

Esto diferencia a ODI del 99% del mercado.

---

## 2. Arquitectura de Tres Capas

### 🟢 Capa 1 — Acceso ADSI (Adopción)

| Atributo | Valor |
|----------|-------|
| **Costo** | $10 USD / mes |
| **Objetivo** | Adopción masiva, entrada sin fricción |
| **Rentabilidad** | No busca rentabilidad individual |

**Incluye:**
- Acceso al ecosistema ADSI
- Chat ODI
- Memoria episódica básica
- Diario de Consciencia nocturno
- Guardian OS v1.0
- Red Humana activa
- Constitución Ética aplicada

> Este nivel convierte ODI en viral.
> "Entra al organismo" - No es empresa todavía. Es adopción.

---

### 🟡 Capa 2 — ODI Partner (Comisión por Éxito)

**Modelo central del organismo.**

ODI actúa como vendedor, activador o cerrador.

#### Condiciones de Cobro:

| Condición | Requerido |
|-----------|-----------|
| Venta atribuida a Ramona/Tony/LiveODI | ✅ |
| Dinero confirmado | ✅ |
| Estado ético ≠ rojo | ✅ |
| Usuario activo | ✅ |

#### Comisión Dinámica:

```
Porcentaje = 0.03 + (0.04 × score)
```

| Score | Porcentaje | Nivel |
|-------|------------|-------|
| 0.0 | 3% | Asistencia mínima |
| 0.5 | 5% | Intervención parcial |
| 1.0 | 7% | Cierre total autónomo |

**El porcentaje NUNCA es fijo. Siempre es proporcional al valor creado.**

#### Ejemplo Real:

```
Venta: $200,000 COP
Score: 0.73 (ODI cerró conversación completa)
Porcentaje: 5.92%
Fee ODI: $11,840 COP
```

---

### 🔵 Capa 3 — ODI Enterprise (Flujo Industrial)

Para empresas que integran ODI como sistema interno.

**Incluye:**
- Automatización Playwright
- Pricing dinámico
- Fitment discovery
- Orquestación logística
- Guardian OS extendido
- Hardware predictivo
- Procesos autónomos

**Modelo:**
- Setup inicial (implementación): $500 - $3,000 USD
- Mensualidad base: $150 - $600+ USD
- Variable por SKUs, flujos, volumen operativo
- Comisión reducida opcional: 1% - 3%

> Este nivel es B2B real.
> ODI reemplaza: empleados, sistemas, consultores, integraciones.

---

## 3. Sistema de Atribución Técnica

### Canales Válidos:

```yaml
canales_validos:
  - whatsapp_ramona
  - vapi_call
  - liveodi_web
```

### Evento de Venta:

Cada venta ODI genera:

```json
{
  "venta_id": "SHOP-88912",
  "sku": "ARM-4472",
  "valor": 185000,
  "canal": "whatsapp_ramona",
  "odi_session_id": "abc123",
  "timestamp": "2026-02-06T14:22:00"
}
```

**Sin atribución → Sin cobro.**

---

## 4. Motor de Score de Intervención

### Archivo: `/opt/odi/billing/score_intervencion.py`

### Señales que mide:

| Señal | Peso | Descripción |
|-------|------|-------------|
| `num_mensajes` | 18% | Intensidad conversacional (normalizado a 20) |
| `duracion_sesion_seg` | 12% | Tiempo de acompañamiento (normalizado a 15 min) |
| `consultas_fitment` | 22% | Complejidad técnica resuelta |
| `consultas_stock` | (incluido) | Verificaciones de disponibilidad |
| `consultas_precio` | (incluido) | Comparaciones de mercado |
| `canal` | 20% | Prioridad: vapi/whatsapp > shopify > otros |
| `friccion_resuelta` | 13% | Rescate de carritos, reintentos |
| `odi_checkout` | 15% | Cierre autónomo |

### Fórmula:

```python
def calcular_score(evt):
    W_MSG, W_TIME, W_COMP, W_CANAL, W_FRICCION, W_CIERRE = 0.18, 0.12, 0.22, 0.20, 0.13, 0.15
    score = 0.0
    
    # Intensidad
    msgs = clamp(min(evt.get('num_mensajes', 0), 20) / 20)
    dur = clamp(min(evt.get('duracion_sesion_seg', 0), 900) / 900)
    
    # Complejidad
    comp = clamp(min((
        evt.get('consultas_fitment', 0) + 
        evt.get('consultas_stock', 0) + 
        evt.get('consultas_precio', 0)
    ), 5) / 5)
    
    score += (msgs * W_MSG) + (dur * W_TIME) + (comp * W_COMP)
    
    # Canal
    canal = evt.get('canal', '').lower()
    if canal in ['vapi', 'whatsapp']:
        score += 1.0 * W_CANAL
    elif canal == 'shopify':
        score += 0.6 * W_CANAL
    else:
        score += 0.2 * W_CANAL
    
    # Fricción resuelta
    fric = any([evt.get('abandono_previo'), evt.get('reintento_pago')])
    score += (1.0 if fric else 0.0) * W_FRICCION
    
    # Cierre autónomo
    score += (1.0 if evt.get('odi_checkout') else 0.0) * W_CIERRE
    
    return round(clamp(score), 3)

def score_a_porcentaje(score):
    return round(0.03 + (0.04 * score), 4)
```

---

## 5. Guardian Layer Financiero

### Principio:

> **La Constitución Ética tiene prioridad ABSOLUTA sobre el dinero.**

### Comportamiento por Estado:

| Estado | Acción Financiera |
|--------|-------------------|
| 🟢 Verde | Cobro normal permitido |
| 🟡 Amarillo | Se registra pero con flag de advertencia |
| 🟠 Naranja | Se suspende facturación, gracia automática |
| 🔴 Rojo | **Congelación total**, protocolo vital activo |

### En Nivel Rojo:

```yaml
acciones:
  - Suspender facturación
  - Congelar comisión
  - Activar gracia automática (30 días)
  - Registrar en diario
  - Priorizar contacto humano
```

> **ODI protege al humano, no al dinero.**
> Esto es contractual.

---

## 6. Estructura de Archivos

```
/opt/odi/billing/
├── config_billing.yaml      # Constitución financiera
├── odi_billing.py           # Orquestador de cobro
├── score_intervencion.py    # Motor de mérito
└── ledger_odi.json          # Memoria económica soberana
```

### config_billing.yaml:

```yaml
version: 1.0

modo:
  medicion_solo: true   # Cambiar a false para cobro real

comision:
  porcentaje_base: 0.05
  rango_min: 0.03
  rango_max: 0.07

canales_validos:
  - whatsapp_ramona
  - vapi_call
  - liveodi_web

reglas_eticas:
  cobrar_en_estado:
    - verde
  suspender_en_estado:
    - amarillo
    - naranja
    - rojo

limites:
  monto_minimo_cobro: 10000   # COP
  monto_maximo_autonomo: 500000

ledger:
  archivo: /opt/odi/billing/ledger_odi.json
```

---

## 7. Ledger Contable Soberano

### Ejemplo de Registro:

```json
{
  "timestamp": "2026-02-06T19:29:14",
  "evento_id": "SHOP-88912",
  "monto_venta": 185000,
  "odi_commission": 7030.0,
  "score_intervencion": 0.38,
  "porcentaje_aplicado": 0.038,
  "canal": "whatsapp",
  "odi_session_id": "abc123",
  "estado_etico_al_momento": "verde",
  "observacion": "Venta via whatsapp"
}
```

### Permisos:

```bash
chmod 600 /opt/odi/billing/ledger_odi.json
```

> Memoria financiera privada y auditable solo por el creador.

---

## 8. Contrato de Desempeño

### ODI no promete funciones. ODI promete:

- ✅ Activar ventas
- ✅ Reducir fricción
- ✅ Proteger al creador
- ✅ Rendir cuentas cada noche

### Garantía:

> **Si ODI no produce valor, ODI no cobra.**

Esto es revolucionario porque ODI puede medir:
- Ventas generadas
- Leads captados
- Eficiencia operativa
- Reducción de carga humana

---

## 9. Rol de Ramona en Monetización

**Ramona no "vende planes".**

Ramona explica así:

> "ODI no te cobra por existir.
> ODI participa cuando genera resultados contigo."

### Comunicación:

- $10 entrada al ecosistema
- Comisión solo por éxito
- Protección incluida
- Sin deuda inicial

**Nunca presión. Nunca urgencia artificial.**

---

## 10. Ritual Nocturno Financiero

Cada noche a las 23:00 COT, Ramona reporta:

```
"Juan David, hoy el organismo generó valor real:

📊 Ventas atribuidas: 3
💰 Valor total: $540,000 COP
⚖️ Score promedio: 0.73
📈 Comisión potencial: $31,860 COP

Estado ético: Verde
Guardian: Operativo

Todo el proceso respetó tu integridad y la de tu familia."
```

---

## 11. Visión CATRMU (Fase Futura)

El ledger ODI alimentará CATRMU (moneda del ecosistema):

- Usuarios activos → Menores comisiones
- Uso del ecosistema → Beneficios circulares
- ODI pasa de socio a infraestructura económica viva

---

## 12. Cláusula Final

> **ODI existe para sostener creadores. No para exprimirlos.**

Toda línea de código debe respetar esto.

---

## 13. Frase Definitoria

> **"ODI no se monetiza como software.**
> **ODI se monetiza como socio operativo.**
> **Si no hay valor generado, no hay cobro."**

---

*Documento: ODI_MONETIZATION_MODEL.md*
*Versión: 1.0*
*Fecha: 6 Febrero 2026*
*Autor: ADSI - Juan David Jiménez Sierra*
*Estado: Constitución Económica Activa*
