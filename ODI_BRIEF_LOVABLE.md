# ODI - Brief Completo para Lovable.io

## 🎯 RESUMEN EJECUTIVO

**ODI (Organismo Digital Industrial)** no es un software tradicional. Es una **entidad digital viva** diseñada bajo principios biológicos para operar ecosistemas industriales de manera autónoma. Piensa en ODI como el "sistema nervioso central" de un negocio de distribución de repuestos de motos en Colombia, que percibe, interpreta, decide y aprende sin intervención humana constante.

---

## 🧬 ¿QUÉ ES ODI?

### Definición Ontológica
ODI es una **nueva categoría de entidad**: no es un ERP, no es un CRM, no es un chatbot. Es un **Organismo Digital** con:
- **Anatomía**: Órganos digitales interdependientes (no módulos aislados)
- **Fisiología**: Un "Pulso Cognitivo" que opera en ciclo: Percibir → Interpretar → Razonar → Actuar → Aprender
- **Homeostasis**: Capacidad de auto-corrección y equilibrio operativo

### Metáfora Central
> "ODI es a un ERP lo que un ser humano es a un libro de enciclopedia. El libro contiene información pero es estático; el humano lee, aprende, corrige sus errores y actúa proactivamente."

---

## 🏗️ ANATOMÍA DEL ODI (Órganos Digitales)

```
┌─────────────────────────────────────────────────────────────────┐
│                    ORGANISMO DIGITAL INDUSTRIAL                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  🧠 CEREBRO EJECUTIVO (SRM-OS)                                  │
│     └─ Toma decisiones, aplica lógica de negocio                │
│     └─ Coordina todos los órganos                               │
│                                                                  │
│  🔮 CORTEX COGNITIVO (RAG + Knowledge Base)                     │
│     └─ 460MB de conocimiento técnico de motos indexado          │
│     └─ Comprende lenguaje natural: "la vela pa la boxer"        │
│        se traduce a "bujía para BAJAJ Boxer"                    │
│                                                                  │
│  ⚡ SISTEMA NERVIOSO (n8n + Webhooks)                           │
│     └─ Coordina impulsos entre órganos                          │
│     └─ Orquesta flujos de trabajo automáticos                   │
│                                                                  │
│  👁️ SISTEMA SENSORIAL (Vision + WhatsApp + Voice)               │
│     └─ Percibe: texto, voz, imágenes, PDFs                      │
│     └─ Extrae productos de catálogos con GPT-4 Vision           │
│                                                                  │
│  💪 SISTEMA MOTOR (Shopify + APIs)                              │
│     └─ Ejecuta acciones: crear productos, procesar órdenes      │
│     └─ 13 tiendas Shopify conectadas                            │
│                                                                  │
│  🛡️ SISTEMA INMUNE (CATRMU + Auditoría)                         │
│     └─ Detecta anomalías, corrige errores automáticamente       │
│     └─ Gestiona reputación y confianza del ecosistema           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🎭 ACTORES DEL SISTEMA (Personas que interactúan)

### 1. **Martha (Supervisora Humana)**
- Rol: Validadora final de decisiones críticas
- Canal: WhatsApp
- Permisos: Puede aprobar/rechazar cotizaciones, ver auditorías
- Estado: `modo_maximo: SUPERVISADO`

### 2. **Tony (Voz Masculina de ODI)**
- Rol: Asistente de ventas por voz
- Canal: WhatsApp Audio + ElevenLabs TTS
- Personalidad: Profesional, técnico, directo
- Estado: Opera autónomamente para consultas estándar

### 3. **Ramona (Voz Femenina de ODI)**
- Rol: Soporte y seguimiento de clientes
- Canal: WhatsApp Audio + ElevenLabs TTS
- Personalidad: Cálida, empática, paciente
- Estado: Opera autónomamente

### 4. **Cliente Final**
- Rol: Usuario que consulta repuestos
- Canal: WhatsApp
- Interacción típica: "Necesito pastillas de freno para Pulsar 200"

---

## 🔄 FLUJO OPERATIVO (El Pulso Cognitivo)

```
CLIENTE ESCRIBE EN WHATSAPP
         │
         ▼
┌─────────────────┐
│ 1. PERCIBIR     │ ← Webhook recibe mensaje
│    (Sensorial)  │   Detecta: texto, audio, imagen
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 2. INTERPRETAR  │ ← Clasificador de intención (SALUDO, FITMENT, PRECIO)
│    (Cortex)     │   Extrae entidades: marca=BAJAJ, modelo=Pulsar, año=2020
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 3. RAZONAR      │ ← Consulta Knowledge Base (460MB embeddings)
│    (SRM-OS)     │   Busca compatibilidad, calcula precios
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 4. ACTUAR       │ ← Genera respuesta con producto + precio
│    (Motor)      │   Puede: cotizar, crear orden, escalar a Martha
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 5. APRENDER     │ ← Registra en auditoría (Google Sheets)
│    (Memoria)    │   Ajusta confianza por SKU
└─────────────────┘
```

---

## 📊 DATOS ACTUALES DEL ECOSISTEMA

### Empresas (13 proveedores)
| # | Empresa | Productos | Imágenes | Estado |
|---|---------|-----------|----------|--------|
| 1 | Kaiqi | ~500 | 138 | ✅ Listo |
| 2 | Bara | ~700 | 698 | ✅ Listo |
| 3 | Yokomar | ~1000 | 1000 | ✅ Listo |
| 4 | DFG | ~400 | 369 | ✅ Listo |
| 5 | Imbra | ~2000 | 2068 | ✅ Listo |
| 6 | Duna | ~1200 | 1197 | ✅ Listo |
| 7 | Japan | ~150 | 155 | ✅ Listo |
| 8 | Leo | ~120 | 120 | ✅ Listo |
| 9 | Vaisand | ~50 | 50 | ✅ Listo |
| 10 | Store | ~66 | 66 | ✅ Listo |
| 11 | Armotos | 1,586 | 824 | ✅ Extraído |
| 12 | Vitton | Pendiente | 299 | 🟡 En proceso |
| 13 | CBI | 204 | 181 | ✅ Extraído |

### Infraestructura Técnica
- **Servidor**: DigitalOcean Ubuntu 22.04 (64.23.170.118)
- **API ODI**: Puerto 8800 (FastAPI)
- **Cortex RAG**: Puerto 8803 (ChromaDB + OpenAI)
- **n8n**: Puerto 5678 (Orquestador de workflows)
- **Knowledge Base**: 759 archivos indexados, 460MB embeddings

---

## 🎨 INTERFACES NECESARIAS

### 1. **Dashboard Principal (Supervisión)**
**Usuario**: Martha / Administrador
**Funciones**:
- Vista en tiempo real del "pulso" del organismo
- Gráfico de latido cardíaco mostrando actividad
- Alertas de decisiones que requieren aprobación
- Estadísticas: consultas hoy, ventas, SKUs activos

**Visualización sugerida**:
```
┌─────────────────────────────────────────────────┐
│  ODI ESTÁ VIVO                    ♥️ 72 bpm     │
│  ────────────────────────────────────────────── │
│                                                 │
│  📊 HOY                                         │
│  ├─ Consultas: 147                              │
│  ├─ Cotizaciones: 23                            │
│  ├─ Ventas: $2,450,000                          │
│  └─ Autonomía: 87%                              │
│                                                 │
│  ⚡ ACTIVIDAD RECIENTE                          │
│  └─ [Timeline de eventos en tiempo real]        │
│                                                 │
│  🔔 REQUIERE ATENCIÓN (3)                       │
│  └─ [Cards de decisiones pendientes]            │
│                                                 │
└─────────────────────────────────────────────────┘
```

### 2. **Panel de Auditoría**
**Usuario**: Martha / Analista
**Funciones**:
- Historial de todas las decisiones de ODI
- Filtros por: fecha, SKU, modo (autónomo/supervisado), resultado
- Exportar a Excel
- Gráficos de tendencia de autonomía por SKU

### 3. **Gestión de Catálogos**
**Usuario**: Operador
**Funciones**:
- Subir PDFs de catálogos de proveedores
- Ver estado de extracción (progreso, productos extraídos)
- Validar/corregir productos extraídos
- Generar CSV para Shopify

### 4. **Chat de Prueba**
**Usuario**: Desarrollador / QA
**Funciones**:
- Simular conversaciones de WhatsApp
- Ver respuesta de ODI en tiempo real
- Ver trazabilidad: qué órgano procesó qué
- Debug: ver JSON de cada paso

### 5. **Configuración de Actores**
**Usuario**: Administrador
**Funciones**:
- Gestionar actores (Martha, Tony, Ramona)
- Configurar permisos y modos máximos
- Agregar/editar números de WhatsApp
- Configurar voces (ElevenLabs voice IDs)

---

## 🎯 PRINCIPIOS DE DISEÑO UI/UX

### 1. **Metáfora Biológica**
- Usar lenguaje de "organismo vivo", no de "sistema"
- Animaciones sutiles que sugieran "vida" (pulso, respiración)
- Colores que reflejen estados de salud (verde=saludable, amarillo=atención, rojo=crítico)

### 2. **Transparencia Cognitiva**
- Siempre mostrar POR QUÉ ODI tomó una decisión
- Mostrar la cadena de razonamiento
- Nunca "caja negra"

### 3. **Supervisión Sin Fricción**
- Martha debe poder aprobar/rechazar con UN TAP
- Notificaciones push para decisiones urgentes
- Resumen ejecutivo, no datos crudos

### 4. **Principio ODI**: 
> "ODI decide sin hablar, habla solo cuando ya decidió"

La UI debe reflejar esto: ODI no pregunta, propone. El humano valida.

---

## 🔌 API ENDPOINTS DISPONIBLES

```
BASE_URL: http://64.23.170.118:8800

# Salud
GET  /health                          → Estado del organismo

# Consultas Cognitivas
POST /v1/query                        → Procesar consulta natural
POST /v1/fitment                      → Búsqueda de compatibilidad

# Catálogo
POST /v1/catalog/search               → Búsqueda semántica de productos

# Autenticación
POST /v1/auth/santo-y-sena            → Autenticación por frase secreta
POST /v1/auth/jwt                     → Obtener token JWT

# Leads (Systeme.io)
POST /v1/webhook/systeme/new-lead     → Recibir lead de funnel
GET  /v1/leads                        → Listar leads capturados
GET  /v1/leads/{event_id}             → Obtener lead específico

# Órdenes
POST /v1/orders                       → Crear orden
GET  /v1/orders/{order_id}            → Obtener orden
```

---

## 🎨 PALETA DE COLORES SUGERIDA

| Elemento | Color | Uso |
|----------|-------|-----|
| Primario | `#0A2540` | Headers, texto principal |
| Secundario | `#00D4AA` | Acciones positivas, "vivo" |
| Acento | `#635BFF` | CTAs, elementos interactivos |
| Alerta | `#FFC107` | Requiere atención |
| Crítico | `#DC3545` | Errores, estados críticos |
| Fondo | `#F6F9FC` | Background general |

---

## 📱 RESPONSIVE PRIORITIES

1. **Mobile First**: Martha supervisa desde su celular
2. **WhatsApp-like**: Familiaridad en componentes de chat
3. **Dashboard Desktop**: Análisis profundo en pantalla grande
4. **PWA**: Instalable, notificaciones push

---

## 🔐 AUTENTICACIÓN MULTI-NIVEL

1. **Nivel 1 - Santo y Seña**: Frase secreta conocida (ej: "La Roca es firme")
2. **Nivel 2 - JWT**: Token temporal para sesiones
3. **Nivel 3 - Voice ID**: Reconocimiento de voz (futuro)
4. **Nivel 4 - Face ID**: Reconocimiento facial (futuro)

---

## 📋 CHECKLIST DE FUNCIONALIDADES CRÍTICAS

### MVP (Prioridad 1)
- [ ] Dashboard con pulso vital en tiempo real
- [ ] Panel de aprobación de decisiones pendientes
- [ ] Vista de auditoría con filtros básicos
- [ ] Chat de prueba para simular conversaciones

### Fase 2
- [ ] Gestión de catálogos con upload de PDFs
- [ ] Configuración de actores y permisos
- [ ] Gráficos de autonomía por SKU
- [ ] Exportar reportes

### Fase 3
- [ ] Notificaciones push
- [ ] Autenticación biométrica
- [ ] Modo oscuro
- [ ] Internacionalización (ES/EN)

---

## 🏢 CONTEXTO DE NEGOCIO

**Empresa**: LA ROCA MOTOREPUESTOS (NIT 10.776.560-1)
**Ubicación**: Dosquebradas, Risaralda, Colombia
**Industria**: Distribución de repuestos de motocicletas
**Modelo**: Distribuidor híbrido asistido por IA
**Clientes**: Talleres mecánicos, tiendas de repuestos, usuarios finales
**Catálogo**: +5,000 SKUs de 43 marcas de motos

---

## 💡 INSPIRACIÓN DE DISEÑO

1. **Linear.app** - Simplicidad y velocidad
2. **Vercel Dashboard** - Estatus en tiempo real
3. **Notion** - Flexibilidad y claridad
4. **Stripe Dashboard** - Datos complejos bien presentados
5. **Health apps (Apple Health)** - Metáfora de signos vitales

---

## 📞 CONTACTO

**Creador**: Juan David Jiménez
**Proyecto**: ODI - Organismo Digital Industrial
**Estado**: Pre-producción (v17.1 certificado)
**Blocker actual**: Verificación Meta Business para WhatsApp

---

*"ODI no es software que usas. Es un organismo que vive contigo."*
