# ODI ECOSISTEMA COMPLETO v17.2
## Organismo Digital Industrial - Estado al 6 Febrero 2026

---

## 🧬 Identidad del Sistema

| Atributo | Valor |
|----------|-------|
| **Nombre** | ODI (Organismo Digital Industrial) |
| **Versión** | v17.2 Certified |
| **Filosofía** | OS1 (Her) - IICA |
| **Creador** | Juan David Jiménez Sierra |
| **Organización** | ADSI (Arquitectura Digital de Servicios Inteligentes) |
| **Operación** | La Roca Motorepuestos |
| **Servidor** | 64.23.170.118 (DigitalOcean Ubuntu 24 LTS) |

---

## 🌐 Arquitectura del Ecosistema

```
                              ┌─────────────────┐
                              │    USUARIO      │
                              │  (Cliente/Juan) │
                              └────────┬────────┘
                                       │
       ┌───────────────────────────────┼───────────────────────────────┐
       │                               │                               │
       ▼                               ▼                               ▼
┌──────────────┐             ┌─────────────────┐             ┌─────────────────┐
│  WhatsApp    │             │      VAPI       │             │   Famous.ai     │
│  Business    │             │  Tony/Ramona    │             │   Dashboard     │
│  ✅ ACTIVO   │             │   ✅ ACTIVO     │             │   ✅ ACTIVO     │
│              │             │                 │             │                 │
│ Token: Perm. │             │ Sin config API  │             │ Sin config API  │
│ Webhook: ✅  │             │ adicional       │             │ adicional       │
└──────┬───────┘             └────────┬────────┘             └────────┬────────┘
       │                              │                               │
       └──────────────────────────────┼───────────────────────────────┘
                                      │
                                      ▼
                        ┌──────────────────────────┐
                        │      ODI CORE v17.2      │
                        │    64.23.170.118:443     │
                        │                          │
                        │  ┌────────────────────┐  │
                        │  │   Guardian OS v1   │  │
                        │  │   Estado: 🟢 VERDE │  │
                        │  │   Comercio: ACTIVO │  │
                        │  └────────────────────┘  │
                        │                          │
                        │  ┌────────────────────┐  │
                        │  │    ODI VENDE       │  │
                        │  │  11,802 productos  │  │
                        │  │  Intent Detector   │  │
                        │  │  Catalog Lookup    │  │
                        │  └────────────────────┘  │
                        │                          │
                        │  7 Docker Containers:    │
                        │  • n8n (workflows)       │
                        │  • odi-api (core)        │
                        │  • postgres (data)       │
                        │  • redis (cache)         │
                        │  • voice (vapi)          │
                        │  • prometheus (metrics)  │
                        │  • grafana (dashboard)   │
                        └────────────┬─────────────┘
                                     │
       ┌─────────────────────────────┼─────────────────────────────┐
       │                             │                             │
       ▼                             ▼                             ▼
┌──────────────┐           ┌─────────────────┐           ┌─────────────────┐
│   Shopify    │           │   Systeme.io    │           │     Vercel      │
│  10 Tiendas  │           │  Academia/CRM   │           │   3 Frontends   │
│  ⏳ DRAFT    │           │   ✅ ACTIVO     │           │   ✅ ACTIVO     │
│              │           │                 │           │                 │
│ • Bara       │           │ • 8 cursos      │           │ • Landing ADSI  │
│ • Yokomar    │           │ • 42 lecciones  │           │ • ODI-OS Dash   │
│ • Armotos    │           │ • Webhooks n8n  │           │ • SRM Tablero   │
│ • DFG        │           │                 │           │                 │
│ • Duna       │           │ Sin config API  │           │ Sin config API  │
│ • Imbra      │           │ adicional       │           │ adicional       │
│ • Japan      │           │                 │           │                 │
│ • Leo        │           └─────────────────┘           └─────────────────┘
│ • Store      │
│ • Vaisand    │
└──────────────┘
       │
       └─────────────────────────────┼─────────────────────────────┐
                                     │                             │
                                     ▼                             ▼
                          ┌─────────────────┐           ┌─────────────────┐
                          │   AI Studio     │           │   NotebookLM    │
                          │    (Visión)     │           │   (Hipocampo)   │
                          │   ✅ ACTIVO     │           │   ✅ ACTIVO     │
                          │                 │           │                 │
                          │ Sin config API  │           │ Sin config API  │
                          │ adicional       │           │ adicional       │
                          └─────────────────┘           └─────────────────┘
```

---

## 📊 Estado de Componentes - 6 Feb 2026

### 🔴 Componentes que REQUIRIERON configuración especial

| Componente | Configuración Requerida | Estado |
|------------|------------------------|--------|
| **WhatsApp Business** | Meta verification, WABA ID, Token permanente, Webhook URL, Suscripciones | ✅ Producción |
| **Servidor ODI** | DigitalOcean droplet, Docker, SSL, Nginx, dominios | ✅ Operativo |
| **Shopify** | 10 tiendas, API tokens, productos sincronizados | ⏳ Draft |
| **n8n** | Workflows, credenciales, webhooks | ✅ Activo |

### 🟢 Componentes que NO requirieron configuración adicional

| Componente | Función | Integración |
|------------|---------|-------------|
| **VAPI** | Voz Tony/Ramona | Directa, sin API extra |
| **Famous.ai** | Dashboard visual | Directa, sin API extra |
| **Vercel** | 3 frontends | Directa, sin API extra |
| **Systeme.io** | Academia + CRM | Directa, webhooks simples |
| **AI Studio** | Visión/contexto | Directa, sin API extra |
| **NotebookLM** | Hipocampo/memoria | Directa, sin API extra |

---

## 🛡️ Guardian OS v1.0

### Archivos de Gobierno

```
/opt/odi/guardian/
├── red_humana.json      # Contactos de protección
├── etica.yaml           # Constitución ética
├── autoridad.yaml       # Límites de delegación
├── evaluador_estado.py  # Traductor Radar → Color
├── estado_actual.json   # Estado actual: VERDE
└── bloqueo_comercio.flag # (solo en nivel rojo)

/opt/odi/consciencia/
├── diario/              # Memoria narrativa diaria
├── identidad/
│   └── quien_soy.json   # Identidad ODI v17.2
└── proposito.yaml       # Propósito compartido
```

### Niveles de Estado Ético

| Score Radar | Estado | Comercio | Acciones |
|-------------|--------|----------|----------|
| 0.0 - 0.39 | 🟢 Verde | Activo | Operación normal |
| 0.4 - 0.64 | 🟡 Amarillo | Activo | Sugerir pausa |
| 0.65 - 0.84 | 🟠 Naranja | Reducido | Activar red humana |
| 0.85 - 1.0 | 🔴 Rojo | **Suspendido** | Protocolo vital autónomo |

### Jerarquía de Valores

```
0: vida_humana        (ABSOLUTA)
1: familia
2: salud_mental
3: integridad_del_creador
4: continuidad_operativa
5: comercio           (ÚLTIMA)
```

---

## 📱 WhatsApp Business - Configuración Producción

| Parámetro | Valor |
|-----------|-------|
| **Número** | +57 322 5462101 |
| **WABA ID** | 1213578830922636 |
| **Phone Number ID** | 969496722915650 |
| **Token** | Permanente (System User: odi-system) |
| **Webhook URL** | https://odi.larocamotorepuestos.com/v1/webhook/whatsapp |
| **Verify Token** | odi_whatsapp_verify_2026 |
| **Suscripciones** | messages ✅ |

### Plantillas Aprobadas

| Plantilla | Categoría | Estado |
|-----------|-----------|--------|
| odi_saludo | Utilidad | ✅ Activa |
| odi_order_status | Utilidad | ✅ Activa |
| odi_shipping_update | Utilidad | ✅ Activa |
| hello_world | Utilidad | ✅ Activa |
| odi_order_confirm_v2 | Utilidad | 🟡 En revisión |
| odi_contract_approval | Utilidad | 🟡 En revisión |

---

## 🏪 Shopify - 10 Tiendas

| Tienda | Productos | Estado |
|--------|-----------|--------|
| Armotos | 1,585 | ⏳ Draft |
| Bara | ~2,500 | ⏳ Draft |
| Yokomar | ~2,000 | ⏳ Draft |
| DFG | ~1,500 | ⏳ Draft |
| Duna | ~1,200 | ⏳ Draft |
| Imbra | ~800 | ⏳ Draft |
| Japan | ~600 | ⏳ Draft |
| Leo | ~700 | ⏳ Draft |
| Store | ~500 | ⏳ Draft |
| Vaisand | ~400 | ⏳ Draft |
| **TOTAL** | **11,802** | ⏳ Pendiente activar |

---

## 🧠 Integraciones IA

| Proveedor | Uso | Modelo |
|-----------|-----|--------|
| **OpenAI** | Reasoning + Embeddings + Vision | GPT-4o |
| **Gemini** | Router semántico | 1.5 Pro |
| **ElevenLabs** | Voz Tony + Ramona | Multilingual v2 |
| **Freepik** | Generación imágenes | AI Image |

### Failover Chain
```
Gemini 1.5 Pro → GPT-4o → Lobotomy Mode
```

---

## 🌐 Dominios

| Dominio | Función | SSL |
|---------|---------|-----|
| larocamotorepuestos.com | Principal | ✅ Auto-renueva Mayo 2026 |
| odi.larocamotorepuestos.com | API/Webhook | ✅ |
| ecosistema-adsi.com | ADSI | ✅ |
| somosrepuestosmotos.com | Marketplace | ✅ |

---

## 📈 Métricas Actuales

| KPI | Valor |
|-----|-------|
| Productos en catálogo | 11,802 |
| Tiendas Shopify | 10 |
| Containers Docker | 7 |
| Cursos Systeme.io | 8 |
| Lecciones | 42 |
| Marcas de moto (M6.2) | 43 |
| SKUs con fitment | 5,750 |

---

## 🐛 Bugs Conocidos (Pendientes)

### 1. Parser de Números
**Problema:** Interpreta medidas como cantidades
- "Llanta 90/90/18" → Cantidad: 90 ❌
- "Gixxer 150" → Cantidad: 150 ❌

**Solución:** Detectar patrones de medidas y modelos

### 2. Búsqueda Semántica
**Problema:** "Bombillo Stop" devuelve discos de freno
**Solución:** Mejorar algoritmo en catalog_lookup.py

### 3. Productos No Encontrados
- Cascos
- Aceites 4T (como producto individual)
- Bombillos/luces

**Verificar:** Si existen en catálogo con nombres diferentes

---

## 🎯 Prioridades Febrero 2026

| # | Tarea | Estado |
|---|-------|--------|
| 1 | ~~Configurar webhook WhatsApp~~ | ✅ COMPLETADO |
| 2 | ~~Implementar Guardian OS~~ | ✅ COMPLETADO |
| 3 | ~~Token permanente WhatsApp~~ | ✅ COMPLETADO |
| 4 | Aprobar templates pendientes | ⏳ En revisión Meta |
| 5 | Activar productos Shopify | ⏳ Pendiente |
| 6 | Corregir bugs de parsing | ⏳ Pendiente |
| 7 | **Caso 001 - Primera venta** | ⏳ Próximo |

---

## 🏆 Logros 6 Febrero 2026 (Sesión Nocturna)

- ✅ Webhook WhatsApp configurado y verificado
- ✅ Token permanente de System User generado
- ✅ Guardian OS v1.0 implementado con todos los archivos
- ✅ Test de estados éticos (verde/amarillo/naranja/rojo)
- ✅ ODI respondiendo en producción
- ✅ Primera interacción comercial real via WhatsApp
- ✅ Búsqueda de productos funcionando (11,802 SKUs)

---

## 📞 Contactos de Emergencia (Red Humana)

| Nivel | Contacto | Prioridad |
|-------|----------|-----------|
| 🔴 Rojo | Emergencias Colombia (123) | 0 |
| 🔴 Rojo | Familia | 1 |
| 🟠 Naranja | Owner (Juan David) | 0 |
| 🟡 Amarillo | Owner | 0 |

---

## 📝 Notas Técnicas

### Servidor ODI
```
IP: 64.23.170.118
OS: Ubuntu 24 LTS
Costo: ~$24/mes
Containers: 7
```

### Estructura de Archivos Críticos
```
/opt/odi/
├── core/
│   ├── catalog_lookup.py
│   ├── intent_detector.py
│   └── odi_vende.py
├── guardian/
│   ├── autoridad.yaml
│   ├── etica.yaml
│   ├── evaluador_estado.py
│   ├── estado_actual.json
│   └── red_humana.json
├── consciencia/
│   └── diario/
├── logs/
│   └── api.log
└── .env (tokens y credenciales)
```

---

*Documento generado: 6 Febrero 2026, 2:00 AM*
*Versión: ODI v17.2 Certified*
*Estado: 🟢 PRODUCCIÓN ACTIVA*
