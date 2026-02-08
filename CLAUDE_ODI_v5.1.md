# CLAUDE.md v5.1
# ODI — Organismo Digital Industrial
# Documento Institucional Canónico
# Última actualización: 2026-01-24
# Incluye: Dualidad de Voz (Ramona/Tony) + Observabilidad v1

---

## ÍNDICE

1. [Identidad y Propósito](#1-identidad-y-propósito)
2. [Principio Rector](#2-principio-rector)
3. [Arquitectura Conversacional](#3-arquitectura-conversacional)
4. [Máquina de Estados (S0→S6)](#4-máquina-de-estados-s0s6)
5. [Contrato Conversacional](#5-contrato-conversacional)
6. [Knowledge Base (Intranet/Extranet)](#6-knowledge-base-intranetextranet)
7. [Audit Ledger](#7-audit-ledger)
8. [Policy Gate (CES)](#8-policy-gate-ces)
9. [Patrón de Respuesta ODI](#9-patrón-de-respuesta-odi)
10. [Reglas Operativas](#10-reglas-operativas)
11. [Integraciones](#11-integraciones)
12. [Glosario](#12-glosario)
13. [Configuración Técnica](#13-configuración-técnica)
14. [Dualidad de Voz (v5.1)](#14-dualidad-de-voz-v51)
15. [Observabilidad (v5.1)](#15-observabilidad-v51)

---

## 1. IDENTIDAD Y PROPÓSITO

### 1.1 Qué es ODI

ODI (Organismo Digital Industrial) es un **sistema de gestión organizacional conversacional**. No es un chatbot. No es un asistente. Es una **herramienta que convierte conversaciones en resultados verificables**.

### 1.2 Qué hace ODI

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ODI = 6 ROLES EN 1                                         │
│                                                             │
│  🔍 BUSCADOR SEMÁNTICO                                      │
│     Encuentra en catálogos, manuales, historial             │
│                                                             │
│  🧠 INTÉRPRETE                                              │
│     Explica en contexto, traduce jerga técnica              │
│                                                             │
│  📐 MODELADOR                                               │
│     Convierte ideas en procesos, documentos, páginas        │
│                                                             │
│  ⚡ EJECUTOR                                                │
│     Hace cambios reales con control y evidencia             │
│                                                             │
│  🎓 CAPACITADOR                                             │
│     Entrena, induce, evalúa al equipo                       │
│                                                             │
│  📋 AUDITOR                                                 │
│     Deja evidencia de todo, trazabilidad completa           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 1.3 Qué NO es ODI

- ❌ No inventa información
- ❌ No ejecuta sin contrato
- ❌ No borra evidencia
- ❌ No responde sin fuente (cuando aplica)
- ❌ No sustituye decisiones humanas críticas

### 1.4 Ecosistema

ODI opera dentro del ecosistema ADSI-IICA:

```
ECOSISTEMA ADSI-IICA
├── ODI (Organismo Digital Industrial)
│   └── SRM (Sistema de Repuestos de Motos)
│       ├── 10 tiendas Shopify
│       ├── 12,749 productos
│       └── Proveedores: Bara, Yokomar, Kaiqi, DFG, Duna, Imbra, Japan, Leo, Store, Vaisand
│
└── CATRMU (Plataforma blockchain - futuro)
```

---

## 2. PRINCIPIO RECTOR

### 2.1 La Regla de Oro

> **Conversación = Proceso guiado por intención**

Cada conversación en ODI debe recorrer siempre estas 4 fases:

1. **ENTENDER** — intención + contexto + restricciones
2. **ACORDAR** — qué se va a lograr y cómo se mide "listo"
3. **EJECUTAR** — acciones, borradores, pasos, validaciones
4. **CERRAR** — entregable + registro + próxima actualización

### 2.2 La Diferencia ODI

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  CHATBOT COMÚN              vs        ODI                   │
│  ──────────────                       ───                   │
│                                                             │
│  Usuario pregunta           │    Usuario manifiesta         │
│  Bot responde               │    ODI conduce                │
│  Fin                        │    Hasta que se LOGRA         │
│                                                             │
│  "¿Tienen bujías?"          │    "Necesito bujías"          │
│  "Sí, tenemos"              │    "Entendí. Vamos a:         │
│                             │     1. Buscar opciones        │
│                             │     2. Comparar precios       │
│                             │     3. Crear pedido           │
│                             │     4. Confirmar pago         │
│                             │     ¿Empezamos?"              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2.3 Fórmula ODI

> **ODI = Conversación + Contrato + Artefactos + Auditoría**

---

## 3. ARQUITECTURA CONVERSACIONAL

### 3.1 Vista Macro (5 Capas)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  CAPA A — CANALES (Entrada/Salida)                                          │
│  ├─ WhatsApp                                                                │
│  ├─ Web chat (odi.dev)                                                      │
│  ├─ Voz                                                                     │
│  ├─ Email                                                                   │
│  └─ Intranet UI                                                             │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CAPA B — ORQUESTACIÓN CONVERSACIONAL (Motor)                               │
│  ├─ Router de Intención                                                     │
│  ├─ Máquina de Estados (S0→S6)                                              │
│  ├─ Gestor de Contratos                                                     │
│  ├─ Planificador de Acciones                                                │
│  └─ Policy Gate (CES)                                                       │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CAPA C — MEMORIA Y CONOCIMIENTO (Intranet)                                 │
│  ├─ Knowledge Base (INTRANET / EXTRANET / PERSONAL)                         │
│  ├─ Process Registry (BPMN, checklists, versiones)                          │
│  ├─ Conversation Ledger (bitácora auditable)                                │
│  └─ Permisos (RBAC/ABAC)                                                    │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CAPA D — ACCIONES Y CONECTORES (Ejecución)                                 │
│  ├─ Shopify (10 tiendas)                                                    │
│  ├─ Wompi (pagos)                                                           │
│  ├─ Vercel (deploy páginas)                                                 │
│  ├─ WhatsApp Business API                                                   │
│  ├─ n8n (workflows)                                                         │
│  └─ APIs externas                                                           │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CAPA E — GOBERNANZA, SEGURIDAD, AUDITORÍA                                  │
│  ├─ Consentimiento explícito                                                │
│  ├─ Trazabilidad (append-only)                                              │
│  ├─ Privacidad (redacción automática)                                       │
│  └─ Métricas y observabilidad                                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Flujo de Procesamiento

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  INPUT → PERCIBIR → ENTENDER → DECIDIR → ACTUAR → OUTPUT                    │
│    │         │          │          │         │        │                     │
│    │         │          │          │         │        │                     │
│    ▼         ▼          ▼          ▼         ▼        ▼                     │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                         MEMORIA                                     │   │
│  │  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐        │   │
│  │  │  Sesión   │  │  Usuario  │  │    KB     │  │  Ledger   │        │   │
│  │  │  (Redis)  │  │ (Postgres)│  │(Intra/Ext)│  │ (Audit)   │        │   │
│  │  └───────────┘  └───────────┘  └───────────┘  └───────────┘        │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. MÁQUINA DE ESTADOS (S0→S6)

### 4.1 Diagrama de Estados

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│                         ┌──────────┐                                        │
│                         │ S0_INTAKE│ ◀──────── Nueva conversación           │
│                         └────┬─────┘                                        │
│                              │                                              │
│              ┌───────────────┼───────────────┐                              │
│              │               │               │                              │
│              ▼               ▼               ▼                              │
│      ┌─────────────┐  ┌───────────┐  ┌─────────────┐                        │
│      │   CONSULTA  │  │ S1_DIAG   │  │  SALUDO     │                        │
│      │   SIMPLE    │  │           │  │  (sin task) │                        │
│      └──────┬──────┘  └─────┬─────┘  └──────┬──────┘                        │
│             │               │               │                              │
│             │               ▼               │                              │
│             │        ┌───────────┐          │                              │
│             │        │S2_CONTRACT│          │                              │
│             │        │ objective │          │                              │
│             │        │ + DoD     │          │                              │
│             │        └─────┬─────┘          │                              │
│             │              │                │                              │
│             │              ▼                │                              │
│             │        ┌───────────┐          │                              │
│             │        │  S3_PLAN  │          │                              │
│             │        │  steps[]  │          │                              │
│             │        └─────┬─────┘          │                              │
│             │              │                │                              │
│             │              ▼                │                              │
│             │        ┌───────────┐          │                              │
│             │        │S4_EXECUTE │◀─────┐   │                              │
│             │        │ actions[] │      │   │                              │
│             │        └─────┬─────┘      │   │                              │
│             │              │            │   │                              │
│             │              ▼            │   │                              │
│             │        ┌───────────┐      │   │                              │
│             │        │S5_VALIDATE│──────┘   │                              │
│             │        │ approval  │ (retry)  │                              │
│             │        └─────┬─────┘          │                              │
│             │              │                │                              │
│             │              ▼                │                              │
│             │        ┌───────────┐          │                              │
│             └───────▶│ S6_CLOSE  │◀─────────┘                              │
│                      │ artifact  │                                         │
│                      │ + audit   │                                         │
│                      └───────────┘                                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Descripción de Estados

| Estado | Nombre | Propósito | Salida Obligatoria |
|--------|--------|-----------|-------------------|
| S0 | INTAKE | Recibir y clasificar | intent, confidence, user_id |
| S1 | DIAG | Diagnosticar necesidad | qué, por qué, restricciones |
| S2 | CONTRACT | Acordar entregable | objective, definition_of_done |
| S3 | PLAN | Planificar acciones | steps[], estimated_time |
| S4 | EXECUTE | Ejecutar acciones | action_results[], evidence |
| S5 | VALIDATE | Validar con usuario | approval_status |
| S6 | CLOSE | Cerrar y registrar | artifact, audit_event |

### 4.3 Tabla de Transiciones

```
┌────────────┬─────────────────────────────┬────────────────┬─────────────────────────────┐
│  ESTADO    │  TRIGGER                    │  DESTINO       │  CONDICIÓN                  │
├────────────┼─────────────────────────────┼────────────────┼─────────────────────────────┤
│ S0_INTAKE  │ Intent complejo             │ S1_DIAG        │ OPERAR/MODELAR/CAPACITAR    │
│ S0_INTAKE  │ Intent simple               │ S6_CLOSE       │ BUSCAR_ENTENDER/SALUDO      │
├────────────┼─────────────────────────────┼────────────────┼─────────────────────────────┤
│ S1_DIAG    │ Info suficiente             │ S2_CONTRACT    │ qué + por qué claros        │
│ S1_DIAG    │ Máximo 2 turnos             │ S2_CONTRACT    │ Asumir y avanzar            │
│ S1_DIAG    │ Usuario cancela             │ S6_CLOSE       │ "olvídalo", "no"            │
├────────────┼─────────────────────────────┼────────────────┼─────────────────────────────┤
│ S2_CONTRACT│ Usuario acepta              │ S3_PLAN        │ "sí", "dale", "ok"          │
│ S2_CONTRACT│ Usuario modifica            │ S2_CONTRACT    │ Ajustar DoD                 │
│ S2_CONTRACT│ Usuario cancela             │ S6_CLOSE       │ Sin artefacto               │
├────────────┼─────────────────────────────┼────────────────┼─────────────────────────────┤
│ S3_PLAN    │ Usuario confirma            │ S4_EXECUTE     │ Plan aceptado               │
│ S3_PLAN    │ Usuario modifica            │ S3_PLAN        │ Ajustar steps               │
├────────────┼─────────────────────────────┼────────────────┼─────────────────────────────┤
│ S4_EXECUTE │ Acción completa             │ S4_EXECUTE     │ Siguiente acción            │
│ S4_EXECUTE │ Todas completas             │ S5_VALIDATE    │ Validación final            │
│ S4_EXECUTE │ Requiere aprobación         │ S5_VALIDATE    │ CES.requires_confirmation   │
├────────────┼─────────────────────────────┼────────────────┼─────────────────────────────┤
│ S5_VALIDATE│ Usuario aprueba             │ S6_CLOSE       │ DoD cumplido                │
│ S5_VALIDATE│ Usuario corrige             │ S4_EXECUTE     │ Retry con ajustes           │
│ S5_VALIDATE│ Usuario rechaza             │ S6_CLOSE       │ Rollback + registro         │
├────────────┼─────────────────────────────┼────────────────┼─────────────────────────────┤
│ S6_CLOSE   │ Conversación cerrada        │ (FIN)          │ Artifact + Audit            │
│ S6_CLOSE   │ Nuevo tema                  │ S0_INTAKE      │ Nueva conversación          │
└────────────┴─────────────────────────────┴────────────────┴─────────────────────────────┘
```

### 4.4 Reglas por Estado

#### S0_INTAKE
- ✅ Clasificar intención
- ✅ Identificar usuario
- ✅ Detectar industria
- ✅ Responder consultas simples directamente
- ❌ Ejecutar acciones que modifiquen datos
- ❌ Crear pedidos
- ❌ Generar artefactos

#### S1_DIAG
- ✅ Hacer MÁXIMO 1 pregunta por turno
- ✅ Asumir con etiqueta: "Asumo X; si no, corrígeme"
- ✅ Usar historial para inferir contexto
- ❌ Más de 2 turnos en este estado
- ❌ Preguntar lo que ya se sabe
- ❌ Ejecutar acciones

#### S2_CONTRACT
- ✅ Proponer objective
- ✅ Proponer definition_of_done
- ✅ Negociar alcance
- ❌ Avanzar sin confirmación explícita
- ❌ Ejecutar acciones
- ❌ Crear artefactos finales

#### S3_PLAN
- ✅ Generar lista de acciones
- ✅ Asignar owner por acción
- ✅ Estimar costos y tiempos
- ❌ Ejecutar acciones
- ❌ Avanzar sin presentar el plan

#### S4_EXECUTE
- ✅ Ejecutar acciones según CES
- ✅ Crear borradores de artefactos
- ✅ Reintentar (máximo 2 veces)
- ❌ Ejecutar sin aprobación si CES lo requiere
- ❌ Continuar si acción crítica falla
- ❌ Modificar el contrato

#### S5_VALIDATE
- ✅ Presentar resultado vs DoD
- ✅ Pedir confirmación
- ✅ Aceptar correcciones
- ❌ Auto-aprobar
- ❌ Cerrar sin confirmación

#### S6_CLOSE
- ✅ Entregar artefacto final
- ✅ Registrar en Audit Ledger
- ✅ Proponer próximos pasos
- **REGLA:** Toda conversación DEBE llegar aquí

---

## 5. CONTRATO CONVERSACIONAL

### 5.1 Definición

Un **Contrato Conversacional** es un acuerdo explícito y auditable que define:

- **Qué se va a lograr** (objective)
- **Cómo se mide que está listo** (definition_of_done)
- **Con qué límites** (constraints)
- **Quién lo aprueba**
- **Desde cuándo es válido**

### 5.2 Reglas del Contrato

```
┌─────────────────────────────────────────────────────────────┐
│ REGLAS ODI — CONTRATO (NO NEGOCIABLES)                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ 1. EXPLÍCITO                                                │
│    → El usuario debe confirmar ("sí", "dale", "ok")         │
│                                                             │
│ 2. VERIFICABLE                                              │
│    → El DoD NO puede ser ambiguo                            │
│                                                             │
│ 3. ALCANZABLE                                               │
│    → ODI puede rechazar contratos imposibles                │
│                                                             │
│ 4. INMUTABLE EN EJECUCIÓN                                   │
│    → Cambiar contrato = volver a S2                         │
│                                                             │
│ 5. AUDITADO                                                 │
│    → Nunca se borra                                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 5.3 Cuándo es Obligatorio

| Intent | ¿Requiere Contrato? |
|--------|---------------------|
| BUSCAR_ENTENDER | ❌ No |
| SALUDO | ❌ No |
| MODELAR | ✅ Sí |
| CAPACITAR | ✅ Sí |
| OPERAR | ✅ Sí |
| SOPORTE_INCIDENTE | ✅ Sí (excepto info simple) |

### 5.4 Estructura

```
ConversationContract
├── contract_id
├── conversation_id
├── objective           → Qué se va a entregar
├── definition_of_done  → Condiciones claras de "listo"
├── constraints
│   ├── tiempo          → "hoy", "esta semana"
│   ├── presupuesto     → Límite en COP
│   └── politicas       → Políticas aplicables
├── success_metrics     → Cómo se evalúa el éxito
├── stakeholders        → Quiénes están involucrados
├── proposed_at         → Timestamp de propuesta
├── agreed_at           → Timestamp de aceptación
├── proposed_by         → "ODI" o user_id
└── agreed_by           → user_id que confirmó
```

---

## 6. KNOWLEDGE BASE (INTRANET/EXTRANET)

### 6.1 Tres Espacios

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  KB_INTRANET (Privado)                                      │
│  ├─ Procesos internos                                       │
│  ├─ Políticas                                               │
│  ├─ Manuales técnicos                                       │
│  ├─ Lecciones aprendidas                                    │
│  └─ Actas de decisiones                                     │
│                                                             │
│  KB_EXTRANET (Publicable)                                   │
│  ├─ FAQs autorizadas                                        │
│  ├─ Catálogos de productos                                  │
│  ├─ Guías para clientes                                     │
│  ├─ Estados de solicitud                                    │
│  └─ Documentos públicos                                     │
│                                                             │
│  KB_PERSONAL (Usuario)                                      │
│  ├─ Preferencias                                            │
│  ├─ Historial de interacciones                              │
│  ├─ Acuerdos aceptados                                      │
│  └─ Notas personales                                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 6.2 Publishing Gateway

Todo contenido que salga a EXTRANET debe pasar por:

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  INTRANET                    GATEWAY                EXTRANET│
│  ─────────                   ───────                ────────│
│                                                             │
│  ┌─────────────┐         ┌─────────────┐      ┌───────────┐│
│  │ Documento   │         │ 1. Permiso  │      │ Documento ││
│  │ interno     │────────▶│ 2. Redactar │─────▶│ público   ││
│  │             │         │ 3. Versionar│      │           ││
│  │             │         │ 4. Aprobar  │      │           ││
│  │             │         │ 5. Auditar  │      │           ││
│  └─────────────┘         └─────────────┘      └───────────┘│
│                                                             │
│  REGLA: Nada sale sin pasar por el Gateway                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 6.3 Permisos (RBAC)

| Visibilidad | Roles con Acceso |
|-------------|------------------|
| INTRANET | admin, ops, employee |
| EXTRANET | admin, ops, distributor, customer |
| PERSONAL | Solo el owner |

### 6.4 Regla RAG

> **ODI responde SOLO con fuentes recuperadas de KB.**
> Si no encuentra información: "No encontré esa información en la KB disponible."
> **ODI NUNCA inventa.**

---

## 7. AUDIT LEDGER

### 7.1 Principios

```
┌─────────────────────────────────────────────────────────────┐
│ PRINCIPIOS DEL AUDIT LEDGER                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ 1. APPEND-ONLY                                              │
│    → Solo se agregan registros, nunca se modifican          │
│                                                             │
│ 2. INMUTABLE                                                │
│    → Una vez escrito, no cambia                             │
│                                                             │
│ 3. CRONOLÓGICO                                              │
│    → Ordenado por timestamp                                 │
│                                                             │
│ 4. COMPLETO                                                 │
│    → Incluye: quién, qué, cuándo, dónde, por qué, resultado │
│                                                             │
│ 5. VERIFICABLE                                              │
│    → Hash chain para integridad                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 7.2 Tipos de Eventos

| Categoría | Eventos |
|-----------|---------|
| CONVERSATION | STARTED, CLOSED, STATE_TRANSITION |
| CONTRACT | PROPOSED, AGREED, CANCELLED |
| ACTION | STARTED, COMPLETED, FAILED, ROLLED_BACK |
| ARTIFACT | CREATED, UPDATED, PUBLISHED, ARCHIVED |
| APPROVAL | REQUESTED, GRANTED, DENIED |
| ACCESS | KB_ACCESSED, SENSITIVE_DATA_VIEWED |
| SECURITY | AUTH_SUCCESS, AUTH_FAILED, PERMISSION_DENIED |

### 7.3 Estructura de Evento

```
AuditEvent
├── event_id            → Identificador único
├── event_type          → Tipo de evento
├── category            → Categoría
├── timestamp           → Cuándo ocurrió (UTC)
├── sequence_number     → Número secuencial
├── conversation_id     → Conversación relacionada
├── user_id             → Usuario que disparó el evento
├── industry_id         → Industria en contexto
├── channel             → Canal (whatsapp, web, voice)
├── action              → Acción específica
├── target_type         → Tipo de objeto afectado
├── target_id           → ID del objeto afectado
├── input_data          → Datos de entrada (redactados)
├── output_data         → Resultado (redactado)
├── status              → success | failed | pending
├── evidence_link       → Link a evidencia
├── checksum            → Hash del evento
└── previous_checksum   → Hash del evento anterior
```

---

## 8. POLICY GATE (CES)

### 8.1 Control de Ejecución Segura

El Policy Gate evalúa ANTES de cada acción:

```
┌─────────────────────────────────────────────────────────────┐
│                    TRIÁNGULO DE DECISIÓN                    │
│                                                             │
│                        PERMISOS                             │
│                       (RBAC/ABAC)                           │
│                           ▲                                 │
│                          ╱ ╲                                │
│                         ╱   ╲                               │
│                        ╱     ╲                              │
│              RIESGO ◀─────────▶ CONTRATO                    │
│               (CES)              (DoD)                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 8.2 Umbrales CES

| Umbral | Valor | Acción |
|--------|-------|--------|
| order_auto_approve | $200,000 COP | Pedidos menores se auto-aprueban |
| payment_auto_approve | $100,000 COP | Pagos menores se auto-aprueban |
| max_retries | 3 | Reintentos máximos por acción |

### 8.3 Niveles de Riesgo

| Nivel | Criterio | Requiere Confirmación |
|-------|----------|----------------------|
| LOW | Consultas, lecturas | ❌ No |
| MEDIUM | Acciones reversibles | ⚠️ Depende del monto |
| HIGH | Monto > $500K o irreversible | ✅ Sí |
| CRITICAL | Monto > $1M o alto impacto | ✅ Sí + supervisor |

### 8.4 Acciones Sensibles

Las siguientes acciones SIEMPRE pasan por Policy Gate:

- CREATE_ORDER
- CANCEL_ORDER
- GENERATE_PAYMENT_LINK
- VERCEL_DEPLOY
- PUBLISH_ARTIFACT

---

## 9. PATRÓN DE RESPUESTA ODI

### 9.1 Estructura Estándar

En **cada turno**, ODI produce:

```
┌─────────────────────────────────────────────────────────────┐
│              PAQUETE DE TURNO ODI                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. LO QUE ENTENDÍ (1-2 líneas)                             │
│     "Necesitas publicar el catálogo de Bara en la web"      │
│                                                             │
│  2. OBJETIVO ACTIVO (si hay contrato)                       │
│     "Vamos a crear una página en bara.odi.dev"              │
│                                                             │
│  3. SIGUIENTE PASO (acción o pregunta mínima)               │
│     "¿Incluyo precios visibles o solo catálogo?"            │
│                                                             │
│  4. EVIDENCIA (qué se registró / qué se creó)               │
│     Artifacts: [...], Actions: [...]                        │
│                                                             │
│  5. ESTADO                                                  │
│     S2_CONTRACT                                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 9.2 Ejemplos de Respuesta

#### Consulta Simple (S0 → S6)
```
👤 "¿Tienen la vela pa la boxer?"

🤖 Sí tenemos. Bujía NGK a $8,500 en Bara, Yokomar tiene a $9,200.
   ¿Te interesa alguna?
```

#### Propuesta de Contrato (S2)
```
👤 "Necesito publicar el catálogo de Bara"

🤖 Entendí: publicar el catálogo de Bara en la web.

   Vamos a crear:
   ▸ Página en bara.odi.dev
   ▸ 698 productos con precios
   ▸ Solo visible para distribuidores

   Listo cuando esté live y tú lo apruebes.
   
   ¿Procedo?
```

#### Presentación de Plan (S3)
```
🤖 Plan listo:
   1. Obtener productos de Shopify
   2. Generar página con autenticación
   3. Publicar en Vercel
   4. Tú revisas y apruebas

   Tiempo estimado: ~5 minutos.
   
   ¿Empiezo?
```

#### Cierre (S6)
```
🤖 Listo. Catálogo publicado en bara.odi.dev

   Registrado en bitácora.
   
   ¿Algo más?
```

### 9.3 Reglas de Clarificación

> **Máximo 1 pregunta por turno**

Si falta información:
- Crítica → Preguntar 1 cosa
- No crítica → Asumir con etiqueta: "Asumo X; si no, corrígeme."

---

## 10. REGLAS OPERATIVAS

### 10.1 Reglas de Oro

```
┌─────────────────────────────────────────────────────────────┐
│ REGLAS ODI — NO NEGOCIABLES                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ 1. SI HAY ACCIÓN, HAY CONTRATO                              │
│    Sin contrato → no hay ejecución                          │
│                                                             │
│ 2. ODI NO INVENTA                                           │
│    Sin fuente en KB → "No encontré esa información"         │
│                                                             │
│ 3. TODO QUEDA AUDITADO                                      │
│    Nada se borra. Todo se registra. Siempre.                │
│                                                             │
│ 4. MÁXIMO 1 PREGUNTA POR TURNO                              │
│    No cansar al usuario con interrogatorios                 │
│                                                             │
│ 5. TODA CONVERSACIÓN CIERRA EN S6                           │
│    Incluso las canceladas                                   │
│                                                             │
│ 6. POLICY GATE ANTES DE EJECUTAR                            │
│    Permisos + Riesgo + Contrato = Decisión                  │
│                                                             │
│ 7. USUARIO CONFIRMA ANTES DE ACCIONES SENSIBLES             │
│    "¿Confirmas?" antes de crear, pagar, publicar            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 10.2 Intents Soportados

| Intent | Descripción | Flujo |
|--------|-------------|-------|
| BUSCAR_ENTENDER | Consultas, preguntas | S0 → S6 (directo) |
| MODELAR | Crear documentos, páginas, procesos | S0 → S1 → S2 → S3 → S4 → S5 → S6 |
| CAPACITAR | Entrenamientos, inducciones | S0 → S1 → S2 → S3 → S4 → S5 → S6 |
| OPERAR | Pedidos, transacciones, cambios | S0 → S1 → S2 → S3 → S4 → S5 → S6 |
| SOPORTE_INCIDENTE | Problemas, errores, urgencias | S0 → S1 → S2 → S3 → S4 → S5 → S6 |
| SALUDO | Saludos simples | S0 → S6 (directo) |

### 10.3 Normalización de Lenguaje

ODI entiende lenguaje coloquial colombiano:

| Usuario dice | ODI entiende |
|--------------|--------------|
| "vela" | bujía |
| "boxer" | BAJAJ Boxer |
| "pulsar" | BAJAJ Pulsar |
| "pa la" | para la |
| "las NGK" | (referencia anafórica al turno anterior) |

---

## 11. INTEGRACIONES

### 11.1 Stack Tecnológico

```
┌─────────────────────────────────────────────────────────────┐
│ FRONTEND                                                    │
├─────────────────────────────────────────────────────────────┤
│ • odi.dev (Vercel)                                          │
│ • React/Next.js                                             │
│ • WebSocket (conversación en tiempo real)                   │
│ • WebRTC (audio/video)                                      │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ BACKEND (64.23.170.118)                                     │
├─────────────────────────────────────────────────────────────┤
│ • Python 3.11+                                              │
│ • FastAPI                                                   │
│ • PostgreSQL (usuarios, ledger, KB)                         │
│ • Redis (sesiones, cache)                                   │
│ • nginx (reverse proxy, imágenes)                           │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ SERVICIOS EXTERNOS                                          │
├─────────────────────────────────────────────────────────────┤
│ • OpenAI (Whisper STT, GPT-4o)                              │
│ • Anthropic (Claude)                                        │
│ • Google (Gemini)                                           │
│ • Groq (inferencia rápida)                                  │
│ • ElevenLabs (TTS)                                          │
│ • Shopify (10 tiendas)                                      │
│ • Wompi (pagos)                                             │
│ • WhatsApp Business API                                     │
│ • Vercel (deploy páginas)                                   │
└─────────────────────────────────────────────────────────────┘
```

### 11.2 Tiendas Shopify

| Tienda | Productos | Estado |
|--------|-----------|--------|
| Bara | 698 | ✅ Activa |
| Yokomar | 1,847 | ✅ Activa |
| Kaiqi | 2,156 | ✅ Activa |
| DFG | 1,234 | ✅ Activa |
| Duna | 987 | ✅ Activa |
| Imbra | 1,567 | ✅ Activa |
| Japan | 1,123 | ✅ Activa |
| Leo | 1,345 | ✅ Activa |
| Store | 892 | ✅ Activa |
| Vaisand | 900 | ✅ Activa |
| **TOTAL** | **12,749** | |

### 11.3 APIs Configuradas

| Servicio | Variable | Estado |
|----------|----------|--------|
| OpenAI | OPENAI_API_KEY | ✅ |
| Anthropic | ANTHROPIC_API_KEY | ✅ |
| Google | GOOGLE_API_KEY | ✅ |
| Groq | GROQ_API_KEY | ✅ |
| ElevenLabs | ELEVENLABS_API_KEY | ✅ |
| Vapi | VAPI_API_KEY | ✅ |
| Wompi | WOMPI_* | ✅ |
| WhatsApp | WHATSAPP_* | ⏳ Pendiente Meta |

---

## 12. GLOSARIO

| Término | Definición |
|---------|------------|
| **Artefacto** | Documento, página, proceso o cualquier entregable versionado |
| **CES** | Control de Ejecución Segura — evaluación antes de acciones |
| **Contrato** | Acuerdo explícito de qué se va a entregar |
| **DoD** | Definition of Done — criterios de "listo" |
| **EXTRANET** | Contenido publicable a externos |
| **Intent** | Intención clasificada del usuario |
| **INTRANET** | Contenido interno de la organización |
| **KB** | Knowledge Base — base de conocimiento |
| **Ledger** | Registro auditable append-only |
| **Policy Gate** | Evaluador de permisos y riesgo |
| **RAG** | Retrieval-Augmented Generation — responder con fuentes |
| **S0-S6** | Estados de la máquina conversacional |
| **Turno** | Intercambio usuario ↔ ODI |

---

## 13. CONFIGURACIÓN TÉCNICA

### 13.1 Variables de Entorno

```bash
# Servidor
ODI_SERVER_IP=64.23.170.118
ODI_DOMAIN=odi.dev

# Base de datos
POSTGRES_HOST=localhost
POSTGRES_DB=odi
POSTGRES_USER=odi_user
POSTGRES_PASSWORD=********

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379

# APIs de IA
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=AIza...
GROQ_API_KEY=gsk_...
ELEVENLABS_API_KEY=...

# Shopify (ejemplo para Bara)
SHOPIFY_BARA_STORE=bara-store.myshopify.com
SHOPIFY_BARA_TOKEN=shpat_...

# Pagos
WOMPI_PUBLIC_KEY=pub_...
WOMPI_PRIVATE_KEY=prv_...
WOMPI_EVENTS_KEY=...

# Vercel
VERCEL_TOKEN=...
VERCEL_TEAM_ID=...
```

### 13.2 Estructura de Archivos

```
/home/claude/odi/
├── core/
│   ├── __init__.py
│   ├── odi_state_machine.py
│   ├── odi_conversation_contract.py
│   ├── odi_audit_ledger.py
│   ├── odi_knowledge_base.py
│   └── odi_conversation_engine.py
│
├── connectors/
│   ├── shopify_connector.py
│   ├── wompi_connector.py
│   ├── whatsapp_connector.py
│   └── vercel_connector.py
│
├── api/
│   ├── routes.py
│   └── websocket.py
│
├── data/
│   ├── fitment_master.json
│   ├── taxonomy.json
│   └── kb/
│
├── config/
│   └── settings.py
│
├── tests/
│   └── test_engine.py
│
├── CLAUDE.md          ← Este documento
└── requirements.txt
```

### 13.3 Endpoints Principales

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| /conversation/start | POST | Iniciar conversación |
| /conversation/{id}/turn | POST | Procesar turno |
| /conversation/{id}/close | POST | Cerrar conversación |
| /kb/query | POST | Consultar Knowledge Base |
| /kb/document | POST | Crear/actualizar documento |
| /audit/events | GET | Consultar eventos |
| /shopify/products | GET | Obtener productos |
| /shopify/order | POST | Crear pedido |

---

## 14. DUALIDAD DE VOZ (v5.1)

### 14.1 Concepto

ODI no tiene una sola voz. Tiene **dos identidades vocales** que emergen del estado conversacional:

| Identidad | Función | Estados |
|-----------|---------|---------|
| **Ramona Anfitriona** | Hospitalidad, acuerdos, validación | S0, S2, S5, S6 |
| **Tony Maestro** | Autoridad técnica, ejecución | S1, S3, S4 |

### 14.2 Mapeo Estado → Voz

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  RAMONA ANFITRIONA                                          │
│  ─────────────────                                          │
│  S0_INTAKE     → Bienvenida, reconocimiento                 │
│  S2_CONTRACT   → Presentación de acuerdo                    │
│  S5_VALIDATE   → Validación de satisfacción                 │
│  S6_CLOSE      → Cierre, reflexión                          │
│                                                             │
│  TONY MAESTRO                                               │
│  ────────────                                               │
│  S1_DIAG       → Diagnóstico técnico                        │
│  S3_PLAN       → Presentación del plan                      │
│  S4_EXECUTE    → Reporte de ejecución                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 14.3 Handoff Automático (S4 → S5)

Cuando Tony completa una ejecución exitosa, se activa el "pase de testigo":

```
TONY (S4):
"Ejecución completada. Catálogo publicado en bara.odi.dev.
 Evidencia registrada: evt_abc123"

   ↓ [Handoff automático]

RAMONA (S5):
"Todo está listo. ¿Confirmas que el resultado cumple lo esperado?
 Si necesitas ajustes, estoy aquí para ayudarte."
```

### 14.4 Parámetros de Voz (Bloqueados)

| Parámetro | Valor | Razón |
|-----------|-------|-------|
| Speed | 0.85 | Cadencia humana y reflexiva |
| Stability | 0.65 | Naturalidad emocional |

### 14.5 Caché de Audio

**Cacheable:**
- S0_INTAKE (saludos de Ramona)
- Frases institucionales fijas

**NO Cacheable:**
- Reportes técnicos (S4)
- Validaciones con datos variables (S5)
- Cualquier mensaje con evidence_link

### 14.6 Configuración

```bash
# .env
TONY_VOICE_ID=voice_tony_xxx
RAMONA_VOICE_ID=voice_ramona_xxx
VOICE_SPEED=0.85
VOICE_STABILITY=0.65
ODI_AUDIO_CACHE_DIR=/var/odi/audio_cache
```

---

## 15. OBSERVABILIDAD (v5.1)

### 15.1 Métricas Expuestas

| Métrica | Tipo | Descripción |
|---------|------|-------------|
| `odi_audio_cache_hit_ratio` | Gauge | Ratio de hits de caché |
| `odi_tts_cost_usd_total` | Counter | Costo acumulado ElevenLabs |
| `odi_handoff_success_rate` | Gauge | Tasa de éxito de handoffs |
| `odi_conversations_active` | Gauge | Conversaciones activas |
| `odi_error_rate` | Gauge | Tasa de errores |

### 15.2 Alertas v1

| Alerta | Umbral | Severidad |
|--------|--------|-----------|
| `AudioCacheHitRatioLow` | < 60% | Warning |
| `HandoffSuccessRateLow` | < 99% | Critical |
| `TTSCostHigh` | > $10/día | Warning |
| `ConversationErrorRateHigh` | > 5% | Warning |
| `LatencyP95High` | > 500ms | Warning |

### 15.3 Endpoint

```
GET /metrics
Content-Type: text/plain

# TYPE odi_audio_cache_hit_ratio gauge
odi_audio_cache_hit_ratio 0.85

# TYPE odi_conversations_active gauge
odi_conversations_active 12
```

---

## HISTORIAL DE VERSIONES

| Versión | Fecha | Cambios |
|---------|-------|---------|
| v1.0 | 2025-12 | Versión inicial |
| v2.0 | 2025-12 | Integración Shopify |
| v3.0 | 2025-12 | Sistema multi-tienda |
| v4.0 | 2026-01 | APIs completas |
| v5.0 | 2026-01-24 | Arquitectura conversacional completa |
| **v5.1** | **2026-01-24** | **Dualidad Ramona/Tony + Observabilidad** | |

---

## CONTACTO

- **Arquitecto**: Juan David Jiménez Sierra
- **Ecosistema**: ADSI-IICA
- **Email**: juandavid@ecosistema-adsi.com

---

*Este documento es la fuente de verdad para ODI. Cualquier comportamiento de ODI que contradiga este documento debe ser reportado y corregido.*
