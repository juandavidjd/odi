# ODI — GUÍA COMPLETA WHATSAPP CLOUD API

**Documento:** `ODI_WhatsApp_Setup_Guide.md`  
**Versión:** 1.0  
**Fecha:** 2026-01-11  
**Estado:** LISTO PARA EJECUCIÓN

---

## 📋 REQUISITOS PREVIOS

### Lo que necesitas antes de empezar:

| Requisito | Descripción | ¿Lo tienes? |
|-----------|-------------|-------------|
| **Cuenta Facebook personal** | Para crear cuenta Business | □ |
| **Cuenta Meta Business** | business.facebook.com | □ |
| **Número de teléfono** | Dedicado para WhatsApp (no puede estar en WA personal) | □ |
| **Servidor con IP pública** | Para webhook (Linux migrado o ngrok temporal) | □ |
| **Tarjeta de crédito/débito** | Para verificar cuenta y pagos | □ |

---

## 🚀 PASO A PASO

### PASO 1: Crear cuenta Meta Business (si no existe)

```
1. Ir a: https://business.facebook.com
2. Click "Crear cuenta"
3. Ingresar:
   - Nombre del negocio: "Somos Repuestos Motos" (o tu nombre comercial)
   - Tu nombre
   - Email de negocio
4. Verificar email
5. Completar información del negocio
```

### PASO 2: Crear App en Meta Developers

```
1. Ir a: https://developers.facebook.com
2. Click "Mis apps" → "Crear app"
3. Seleccionar tipo: "Empresa"
4. Nombre de la app: "ODI WhatsApp"
5. Asociar a tu cuenta Business
6. Click "Crear app"
```

### PASO 3: Agregar WhatsApp a la App

```
1. En el dashboard de tu app
2. Buscar "WhatsApp" en productos
3. Click "Configurar"
4. Aceptar términos de WhatsApp Business
```

### PASO 4: Configurar número de teléfono

```
1. En WhatsApp → Configuración → Números de teléfono
2. Click "Agregar número de teléfono"
3. Ingresar número (formato internacional: +57XXXXXXXXXX)
4. Verificar por SMS o llamada
5. Crear perfil de negocio:
   - Nombre: "ODI - Somos Repuestos Motos"
   - Categoría: "Venta de productos"
   - Descripción: "Asistente inteligente de repuestos de motos"
```

### PASO 5: Obtener credenciales

```
En WhatsApp → Configuración → Primeros pasos:

1. Token de acceso temporal (para pruebas):
   - Click "Generar token"
   - Guardar el token (expira en 24h)

2. Phone Number ID:
   - Se muestra en la misma página
   - Formato: números largos

3. WhatsApp Business Account ID:
   - En Configuración → Cuentas de WhatsApp Business
```

### PASO 6: Configurar Webhook

```
1. En WhatsApp → Configuración → Configuración de webhook

2. URL del webhook:
   https://TU_SERVIDOR:5678/webhook/whatsapp-incoming
   (O usar ngrok para pruebas: https://XXXX.ngrok.io/webhook/whatsapp-incoming)

3. Token de verificación:
   odi_whatsapp_verify_2026

4. Suscribirse a:
   ✓ messages
   ✓ message_status (opcional)
```

---

## 💰 COSTOS Y PAGOS

### Modelo de precios WhatsApp Cloud API

| Tipo de conversación | Precio aprox. (Colombia) |
|---------------------|--------------------------|
| **Iniciada por usuario** | ~$0.005 USD |
| **Iniciada por negocio (utilidad)** | ~$0.008 USD |
| **Iniciada por negocio (marketing)** | ~$0.025 USD |
| **Servicio al cliente (24h)** | Gratis dentro de ventana |

### Dónde cargar saldo

```
1. Ir a: https://business.facebook.com
2. Click: Configuración del negocio → Pagos
3. Agregar método de pago (tarjeta)
4. Los cargos son automáticos según uso
```

### Créditos gratuitos

- **1,000 conversaciones gratis** por mes (iniciadas por usuario)
- Suficiente para pruebas iniciales

---

## 📄 VARIABLES DE ENTORNO (.env)

Agregar a tu `.env`:

```bash
# ===== WHATSAPP CLOUD API =====
WHATSAPP_ACCESS_TOKEN=EAAxxxxxxxxxxxxxxx
WHATSAPP_PHONE_NUMBER_ID=1234567890
WHATSAPP_BUSINESS_ACCOUNT_ID=9876543210
WHATSAPP_VERIFY_TOKEN=odi_whatsapp_verify_2026
WHATSAPP_API_VERSION=v18.0
```

---

## 🔧 WORKFLOW N8N: WHATSAPP INCOMING

```json
{
  "name": "ODI WhatsApp Incoming",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "whatsapp-incoming",
        "options": {}
      },
      "name": "WhatsApp Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [-400, 0],
      "webhookId": "whatsapp-incoming"
    },
    {
      "parameters": {
        "conditions": {
          "options": {"caseSensitive": true, "leftValue": "", "typeValidation": "loose"},
          "conditions": [
            {
              "leftValue": "={{ $json.body?.entry?.[0]?.changes?.[0]?.value?.messages?.[0]?.type }}",
              "rightValue": "text",
              "operator": {"type": "string", "operation": "equals"}
            }
          ],
          "combinator": "and"
        }
      },
      "name": "¿Es mensaje de texto?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2,
      "position": [-200, 0]
    },
    {
      "parameters": {
        "keepOnlySet": true,
        "values": {
          "string": [
            {"name": "from", "value": "={{ $json.body.entry[0].changes[0].value.messages[0].from }}"},
            {"name": "message", "value": "={{ $json.body.entry[0].changes[0].value.messages[0].text.body }}"},
            {"name": "message_id", "value": "={{ $json.body.entry[0].changes[0].value.messages[0].id }}"},
            {"name": "timestamp", "value": "={{ new Date().toISOString() }}"},
            {"name": "canal", "value": "whatsapp"}
          ]
        }
      },
      "name": "Extraer Datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [0, -100]
    },
    {
      "parameters": {
        "functionCode": "// Analizar intención del mensaje\nconst message = items[0].json.message.toLowerCase();\nlet intent = 'CONSULTA_GENERAL';\nlet producto = '';\nlet accion = 'informar';\n\n// Detectar intención de compra\nif (message.includes('comprar') || message.includes('quiero') || message.includes('necesito')) {\n  intent = 'INTENCION_COMPRA';\n  accion = 'vender';\n}\n\n// Detectar consulta de producto\nif (message.includes('tienen') || message.includes('hay') || message.includes('precio')) {\n  intent = 'CONSULTA_PRODUCTO';\n  accion = 'buscar';\n}\n\n// Detectar marcas de motos\nconst marcas = ['honda', 'yamaha', 'suzuki', 'bajaj', 'akt', 'pulsar', 'cb', 'fz'];\nmarcas.forEach(marca => {\n  if (message.includes(marca)) {\n    producto = marca.toUpperCase();\n  }\n});\n\nreturn [{\n  json: {\n    ...items[0].json,\n    intent: intent,\n    producto: producto,\n    accion: accion\n  }\n}];"
      },
      "name": "Analizar Intención",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [200, -100]
    },
    {
      "parameters": {
        "conditions": {
          "options": {"caseSensitive": true, "leftValue": "", "typeValidation": "loose"},
          "conditions": [
            {
              "leftValue": "={{ $json.intent }}",
              "rightValue": "CONSULTA_PRODUCTO",
              "operator": {"type": "string", "operation": "equals"}
            }
          ],
          "combinator": "and"
        }
      },
      "name": "¿Consulta de producto?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2,
      "position": [400, -100]
    },
    {
      "parameters": {
        "method": "POST",
        "url": "http://localhost:5678/webhook/fitment-query",
        "sendBody": true,
        "specifyBody": "json",
        "jsonBody": "={\n  \"marca\": \"{{ $json.producto }}\",\n  \"canal\": \"whatsapp\",\n  \"user_phone\": \"{{ $json.from }}\"\n}"
      },
      "name": "Buscar en Fitment",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [600, -200]
    },
    {
      "parameters": {
        "method": "POST",
        "url": "https://graph.facebook.com/v18.0/{{$env.WHATSAPP_PHONE_NUMBER_ID}}/messages",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "sendBody": true,
        "specifyBody": "json",
        "jsonBody": "={\n  \"messaging_product\": \"whatsapp\",\n  \"to\": \"{{ $('Extraer Datos').item.json.from }}\",\n  \"type\": \"text\",\n  \"text\": {\n    \"body\": \"{{ $json.response_text ?? 'Gracias por tu mensaje. Un asesor te contactará pronto.' }}\"\n  }\n}"
      },
      "name": "Enviar Respuesta WhatsApp",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [800, 0],
      "credentials": {
        "httpHeaderAuth": {
          "id": "whatsapp-auth",
          "name": "WhatsApp Auth"
        }
      }
    },
    {
      "parameters": {
        "operation": "append",
        "documentId": {"__rl": true, "value": "{{$env.GSHEET_DOC_ID}}", "mode": "id"},
        "sheetName": {"__rl": true, "value": "WHATSAPP_LOG", "mode": "name"},
        "columns": {
          "mappingMode": "autoMapInputData",
          "value": {}
        }
      },
      "name": "Log WhatsApp",
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [1000, 0]
    }
  ],
  "connections": {
    "WhatsApp Webhook": {
      "main": [[{"node": "¿Es mensaje de texto?", "type": "main", "index": 0}]]
    },
    "¿Es mensaje de texto?": {
      "main": [
        [{"node": "Extraer Datos", "type": "main", "index": 0}],
        []
      ]
    },
    "Extraer Datos": {
      "main": [[{"node": "Analizar Intención", "type": "main", "index": 0}]]
    },
    "Analizar Intención": {
      "main": [[{"node": "¿Consulta de producto?", "type": "main", "index": 0}]]
    },
    "¿Consulta de producto?": {
      "main": [
        [{"node": "Buscar en Fitment", "type": "main", "index": 0}],
        [{"node": "Enviar Respuesta WhatsApp", "type": "main", "index": 0}]
      ]
    },
    "Buscar en Fitment": {
      "main": [[{"node": "Enviar Respuesta WhatsApp", "type": "main", "index": 0}]]
    },
    "Enviar Respuesta WhatsApp": {
      "main": [[{"node": "Log WhatsApp", "type": "main", "index": 0}]]
    }
  },
  "active": false,
  "settings": {"executionOrder": "v1"},
  "versionId": "whatsapp-v1"
}
```

---

## 🔧 WORKFLOW N8N: VERIFICACIÓN WEBHOOK

Meta envía una verificación GET antes de activar el webhook:

```json
{
  "name": "WhatsApp Verify Webhook",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "GET",
        "path": "whatsapp-incoming",
        "responseMode": "responseNode",
        "options": {}
      },
      "name": "Verify Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [-200, 0]
    },
    {
      "parameters": {
        "respondWith": "text",
        "responseBody": "={{ $json.query['hub.challenge'] }}",
        "options": {}
      },
      "name": "Respond Challenge",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1,
      "position": [0, 0]
    }
  ],
  "connections": {
    "Verify Webhook": {
      "main": [[{"node": "Respond Challenge", "type": "main", "index": 0}]]
    }
  }
}
```

---

## 📝 CHECKLIST DE IMPLEMENTACIÓN

### Fase 1: Configuración Meta (Antes de n8n)

```
□ 1.1  Crear/verificar cuenta Meta Business
       URL: https://business.facebook.com

□ 1.2  Crear app en Meta Developers
       URL: https://developers.facebook.com

□ 1.3  Agregar producto WhatsApp a la app

□ 1.4  Configurar número de teléfono
       ⚠️ IMPORTANTE: Número NO puede estar en WhatsApp personal

□ 1.5  Obtener credenciales:
       - WHATSAPP_ACCESS_TOKEN
       - WHATSAPP_PHONE_NUMBER_ID
       - WHATSAPP_BUSINESS_ACCOUNT_ID

□ 1.6  Agregar método de pago (tarjeta)
```

### Fase 2: Configuración Servidor

```
□ 2.1  Verificar Linux migrado con IP pública
       O configurar ngrok temporal:
       $ ngrok http 5678

□ 2.2  Obtener URL pública del webhook
       Ejemplo: https://abc123.ngrok.io/webhook/whatsapp-incoming

□ 2.3  Actualizar .env con credenciales WhatsApp
```

### Fase 3: Configuración n8n

```
□ 3.1  Importar workflow "WhatsApp Verify Webhook"

□ 3.2  Activar workflow de verificación

□ 3.3  Configurar webhook en Meta:
       URL: tu_url_publica/webhook/whatsapp-incoming
       Verify Token: odi_whatsapp_verify_2026

□ 3.4  Verificar que Meta valide el webhook (✓ verde)

□ 3.5  Importar workflow "ODI WhatsApp Incoming"

□ 3.6  Crear credencial HTTP Header Auth:
       Header: Authorization
       Value: Bearer {WHATSAPP_ACCESS_TOKEN}

□ 3.7  Activar workflow principal
```

### Fase 4: Pruebas

```
□ 4.1  Enviar mensaje de prueba desde tu WhatsApp personal
       Al número configurado

□ 4.2  Verificar que n8n reciba el webhook
       → Revisar ejecuciones

□ 4.3  Verificar respuesta automática
       → Debe llegar mensaje de vuelta

□ 4.4  Verificar log en Sheets
       → Hoja WHATSAPP_LOG

□ 4.5  Probar consulta de producto:
       "¿Tienen pastillas para Honda CB150?"
```

---

## 🧪 CASOS DE PRUEBA

### Test 1: Mensaje simple
```
Input: "Hola"
Expected: Respuesta de bienvenida
```

### Test 2: Consulta de producto
```
Input: "¿Tienen pastillas para Pulsar?"
Expected: Búsqueda en fitment + respuesta con productos
```

### Test 3: Intención de compra
```
Input: "Quiero comprar pastillas de freno"
Expected: Detecta INTENCION_COMPRA + ofrece productos
```

---

## ⚠️ NOTAS IMPORTANTES

### Limitaciones del token temporal
- **Expira en 24 horas**
- Para producción: generar token permanente con permisos

### Ventana de 24 horas
- Solo puedes enviar mensajes de plantilla después de 24h sin interacción
- Dentro de 24h: mensajes libres

### Templates de mensajes
- Para marketing: requieren aprobación de Meta
- Para servicio: más flexibles

### Rate limits
- 80 mensajes por segundo (cuenta nueva)
- Escala con uso y calidad

---

## 🔗 RECURSOS

| Recurso | URL |
|---------|-----|
| Meta Business Suite | https://business.facebook.com |
| Meta Developers | https://developers.facebook.com |
| WhatsApp Business API Docs | https://developers.facebook.com/docs/whatsapp/cloud-api |
| Precios WhatsApp | https://developers.facebook.com/docs/whatsapp/pricing |

---

**FIN DEL DOCUMENTO**
