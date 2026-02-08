# GUÍA RÁPIDA: CREAR PLANTILLAS EN WHATSAPP MANAGER
## ODI v5.3 — Plantillas UTILITY Aprobadas

---

## 📋 ACCESO

**URL:** https://business.facebook.com/wa/manage/message-templates/

**Cuenta:** Test WhatsApp Business Account (ADSI)

---

## 🔧 PROCESO PASO A PASO

### 1. Click "Crear plantilla"

### 2. Configurar cada plantilla:

---

## 📝 PLANTILLA 1: `odi_saludo`

| Campo | Valor |
|-------|-------|
| Nombre | `odi_saludo` |
| Categoría | **Utility** |
| Idioma | Español |

**Cuerpo (copiar exacto):**
```
Hola {{1}}.

Este es un mensaje de confirmación del canal oficial de ADSI.
A partir de ahora recibirás aquí notificaciones relacionadas con tus solicitudes, pedidos o soporte.

Si no reconoces este contacto, ignora este mensaje.
```

**Variables:**
- `{{1}}` = nombre del usuario

---

## 📝 PLANTILLA 2: `odi_order_confirm`

| Campo | Valor |
|-------|-------|
| Nombre | `odi_order_confirm` |
| Categoría | **Utility** |
| Idioma | Español |

**Cuerpo (copiar exacto):**
```
Confirmación de pedido.

Número de orden: {{1}}
Tienda: {{2}}
Total: {{3}} COP
Fecha estimada: {{4}}

Este mensaje confirma que tu pedido fue registrado correctamente.
```

**Variables:**
- `{{1}}` = número de orden
- `{{2}}` = tienda
- `{{3}}` = total
- `{{4}}` = fecha estimada

---

## 📝 PLANTILLA 3: `odi_order_status`

| Campo | Valor |
|-------|-------|
| Nombre | `odi_order_status` |
| Categoría | **Utility** |
| Idioma | Español |

**Cuerpo (copiar exacto):**
```
Actualización del estado de tu pedido.

Número de orden: {{1}}
Estado actual: {{2}}

Puedes responder a este mensaje si necesitas soporte adicional.
```

**Variables:**
- `{{1}}` = número de orden
- `{{2}}` = estado

---

## 📝 PLANTILLA 4: `odi_shipping_update`

| Campo | Valor |
|-------|-------|
| Nombre | `odi_shipping_update` |
| Categoría | **Utility** |
| Idioma | Español |

**Cuerpo (copiar exacto):**
```
Notificación de envío.

Número de orden: {{1}}
Transportadora: {{2}}
Guía: {{3}}
Fecha estimada de entrega: {{4}}

Este mensaje corresponde al seguimiento de tu pedido.
```

**Variables:**
- `{{1}}` = número de orden
- `{{2}}` = transportadora
- `{{3}}` = guía
- `{{4}}` = fecha entrega

---

## 📝 PLANTILLA 5: `odi_contract_approval` ⚠️ (CES)

| Campo | Valor |
|-------|-------|
| Nombre | `odi_contract_approval` |
| Categoría | **Utility** |
| Idioma | Español |

**Cuerpo (copiar exacto):**
```
Solicitud de aprobación.

Contrato: {{1}}
Descripción: {{2}}
Monto: {{3}} COP

Responde seleccionando una opción para continuar.
```

**Variables:**
- `{{1}}` = contrato_id
- `{{2}}` = descripción
- `{{3}}` = monto

**Botones (Quick Reply):**
- Botón 1: `APROBAR`
- Botón 2: `RECHAZAR`

---

## ⏱️ TIEMPOS

| Acción | Tiempo |
|--------|--------|
| Crear plantillas | 15-20 min |
| Aprobación Meta | 24-48 horas |
| Total | ~2 días |

---

## ✅ CHECKLIST

- [ ] odi_saludo creada
- [ ] odi_order_confirm creada
- [ ] odi_order_status creada
- [ ] odi_shipping_update creada
- [ ] odi_contract_approval creada (con botones)
- [ ] Todas enviadas a revisión
- [ ] Todas aprobadas por Meta

---

## ⚠️ ERRORES A EVITAR

| ❌ NO hacer | ✅ SÍ hacer |
|-------------|-------------|
| Agregar emojis | Mantener texto limpio |
| Cambiar "Confirmación" por "¡Listo!" | Usar texto exacto |
| Agregar "Gracias por tu compra" | Solo info transaccional |
| Modificar estructura | Copiar/pegar exacto |

---

## 🔜 POST-APROBACIÓN

1. Actualizar `BUSINESS_STATUS = VERIFIED` en:
   - `/opt/odi/config/whatsapp_mapping.py`

2. Configurar en `.env`:
   ```
   META_WHATSAPP_TOKEN=tu_token
   META_PHONE_NUMBER_ID=tu_phone_id
   META_BUSINESS_ID=tu_business_id
   ```

3. Activar flujo n8n

---

*ODI v5.3 — WhatsApp Integration*
*Fecha: 2026-01-24*
