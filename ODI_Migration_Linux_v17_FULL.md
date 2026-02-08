# ODI v17 — ARQUITECTURA DE MIGRACIÓN LINUX

**Documento:** `ODI_Migration_Linux_v17.md`  
**Versión:** 1.0  
**Fecha:** 2026-01-11  
**Autor:** Claude (Arquitecto)  
**Ejecutor:** ChatGPT (Ingeniero)  
**Estado:** APROBADO PARA EJECUCIÓN  

---

## 📐 1. TOPOLOGÍA OBJETIVO

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     SERVIDOR LINUX (Ubuntu 22.04 LTS)                   │
│                         ThinkCentre / VPS / VM                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                        DOCKER NETWORK                            │   │
│  │                      (odi-network / bridge)                      │   │
│  │  ┌─────────────────┐         ┌─────────────────┐                │   │
│  │  │    n8n          │         │  odi_voice      │                │   │
│  │  │  (Container)    │ ──────► │  (Container)    │                │   │
│  │  │  Puerto: 5678   │  HTTP   │  Puerto: 7777   │                │   │
│  │  │                 │         │                 │                │   │
│  │  │  /data/n8n ───┐ │         │  /logs/odi ───┐ │                │   │
│  │  └───────────────│─┘         └───────────────│─┘                │   │
│  │                  │                           │                   │   │
│  └──────────────────│───────────────────────────│───────────────────┘   │
│                     │                           │                       │
│  ┌──────────────────▼───────────────────────────▼───────────────────┐   │
│  │                    VOLÚMENES PERSISTENTES                        │   │
│  │  /opt/odi/                                                       │   │
│  │  ├── data/                                                       │   │
│  │  │   ├── n8n/           # Workflows, credentials                 │   │
│  │  │   └── voice/         # Logs, estado                           │   │
│  │  ├── logs/                                                       │   │
│  │  │   ├── n8n/           # Logs n8n                               │   │
│  │  │   └── voice/         # Logs Flask                             │   │
│  │  ├── backups/                                                    │   │
│  │  │   └── daily/         # Rotación 7 días                        │   │
│  │  ├── config/                                                     │   │
│  │  │   └── .env           # Variables unificadas                   │   │
│  │  └── docker-compose.yml                                          │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                         FIREWALL (UFW)                           │   │
│  │  ALLOW: 22 (SSH) │ 5678 (n8n) │ 7777 (voice)                    │   │
│  │  DENY: everything else                                           │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 📋 2. ESPECIFICACIÓN DE SERVICIOS

| Servicio | Imagen/Runtime | Puerto Host | Puerto Container | Volúmenes | Restart |
|----------|----------------|-------------|------------------|-----------|---------|
| **n8n** | `n8nio/n8n:latest` | 5678 | 5678 | `/opt/odi/data/n8n:/home/node/.n8n` | `always` |
| **odi_voice** | `python:3.11-slim` | 7777 | 7777 | `/opt/odi/data/voice:/app/data`, `/opt/odi/logs/voice:/app/logs` | `always` |

---

## 📄 3. ARCHIVOS DE CONFIGURACIÓN

### 3.1 docker-compose.yml

```yaml
version: '3.8'

services:
  n8n:
    image: n8nio/n8n:latest
    container_name: odi-n8n
    restart: always
    ports:
      - "5678:5678"
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=${N8N_USER}
      - N8N_BASIC_AUTH_PASSWORD=${N8N_PASSWORD}
      - N8N_HOST=${N8N_HOST}
      - N8N_PORT=5678
      - N8N_PROTOCOL=http
      - WEBHOOK_URL=${WEBHOOK_URL}
      - GENERIC_TIMEZONE=America/Bogota
      - TZ=America/Bogota
    volumes:
      - /opt/odi/data/n8n:/home/node/.n8n
      - /opt/odi/logs/n8n:/home/node/logs
    networks:
      - odi-network
    healthcheck:
      test: ["CMD", "wget", "-q", "--spider", "http://localhost:5678/healthz"]
      interval: 30s
      timeout: 10s
      retries: 3

  odi_voice:
    build:
      context: ./voice
      dockerfile: Dockerfile
    container_name: odi-voice
    restart: always
    ports:
      - "7777:7777"
    environment:
      - ODI_SECURE_TOKEN=${ODI_SECURE_TOKEN}
      - FLASK_ENV=production
      - TZ=America/Bogota
    volumes:
      - /opt/odi/data/voice:/app/data
      - /opt/odi/logs/voice:/app/logs
    networks:
      - odi-network
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:7777/"]
      interval: 30s
      timeout: 10s
      retries: 3
    depends_on:
      - n8n

networks:
  odi-network:
    driver: bridge
    name: odi-network
```

### 3.2 voice/Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Código
COPY odi_voice_assistant.py .

# Crear directorios
RUN mkdir -p /app/data /app/logs

# Puerto
EXPOSE 7777

# Ejecutar
CMD ["python", "odi_voice_assistant.py"]
```

### 3.3 voice/requirements.txt

```
flask==3.0.0
gunicorn==21.2.0
```

### 3.4 config/.env

```bash
# ═══════════════════════════════════════════════════════════════
# ODI v17 — CONFIGURACIÓN UNIFICADA
# ═══════════════════════════════════════════════════════════════

# ─── N8N ───────────────────────────────────────────────────────
N8N_USER=admin
N8N_PASSWORD=<CAMBIAR_POR_PASSWORD_SEGURO>
N8N_HOST=0.0.0.0
WEBHOOK_URL=http://<IP_SERVIDOR>:5678

# ─── ODI VOICE ─────────────────────────────────────────────────
ODI_SECURE_TOKEN=odi_strong_password_2026

# ─── GOOGLE SHEETS ─────────────────────────────────────────────
GOOGLE_SHEETS_DOC_ID=1KK-aUJbKvUut9K5ySDmzIkGBi6mhY62C2xxP2XVG8aY

# ─── TIMEZONE ──────────────────────────────────────────────────
TZ=America/Bogota
```

---

## 🔧 4. CHECKLIST DE EJECUCIÓN

### FASE 0: Preparación (Windows → exportar)

```
□ 0.1  Exportar workflow n8n actual como JSON
       → Archivo: ODI_v16_9_2_SHEETS_FIX.json
       
□ 0.2  Exportar credentials n8n (Google Sheets OAuth)
       → n8n UI → Settings → Credentials → Export
       
□ 0.3  Copiar odi_voice_assistant.py

□ 0.4  Documentar variables .env actuales
       → Especialmente tokens y IDs
```

### FASE 1: Servidor Linux Base

```
□ 1.1  Instalar Ubuntu 22.04 LTS (o confirmar existente)

□ 1.2  Crear usuario no-root
       $ sudo adduser odi
       $ sudo usermod -aG sudo odi
       $ sudo usermod -aG docker odi

□ 1.3  Configurar SSH keys (deshabilitar password auth)
       $ ssh-keygen -t ed25519
       $ ssh-copy-id odi@<servidor>
       
□ 1.4  Instalar Docker + Docker Compose
       $ curl -fsSL https://get.docker.com | sh
       $ sudo apt install docker-compose-plugin
       
□ 1.5  Configurar firewall
       $ sudo ufw default deny incoming
       $ sudo ufw default allow outgoing
       $ sudo ufw allow 22/tcp
       $ sudo ufw allow 5678/tcp
       $ sudo ufw allow 7777/tcp
       $ sudo ufw enable
```

### FASE 2: Estructura de Directorios

```
□ 2.1  Crear estructura
       $ sudo mkdir -p /opt/odi/{data/{n8n,voice},logs/{n8n,voice},backups/daily,config,voice}
       $ sudo chown -R odi:odi /opt/odi
       $ chmod 700 /opt/odi/config

□ 2.2  Copiar archivos de configuración
       → docker-compose.yml → /opt/odi/
       → .env → /opt/odi/config/
       → Dockerfile → /opt/odi/voice/
       → requirements.txt → /opt/odi/voice/
       → odi_voice_assistant.py → /opt/odi/voice/

□ 2.3  Crear symlink para .env
       $ ln -s /opt/odi/config/.env /opt/odi/.env
```

### FASE 3: Migración de Datos

```
□ 3.1  Copiar workflow n8n
       → Importar ODI_v16_9_2_SHEETS_FIX.json vía UI después de arrancar
       
□ 3.2  Copiar credentials Google Sheets
       → Importar vía n8n UI → Settings → Credentials
       → Reautenticar OAuth si es necesario

□ 3.3  Actualizar URL de webhook en workflow
       → Cambiar: host.docker.internal → odi-voice
       → Nuevo URL: http://odi-voice:7777/odi/voice-response
```

### FASE 4: Arranque

```
□ 4.1  Arrancar servicios
       $ cd /opt/odi
       $ docker compose up -d

□ 4.2  Verificar contenedores
       $ docker ps
       → Debe mostrar: odi-n8n (healthy), odi-voice (healthy)

□ 4.3  Verificar logs
       $ docker logs odi-n8n --tail 50
       $ docker logs odi-voice --tail 50

□ 4.4  Verificar healthchecks
       $ curl http://localhost:5678/healthz
       $ curl http://localhost:7777/
```

### FASE 5: Validación Funcional

```
□ 5.1  Test webhook manual
       $ curl -X POST http://localhost:5678/webhook/odi-v16-5-action \
         -H "Content-Type: application/json" \
         -d '{
           "sku": "TEST-001",
           "producto": "Producto de Prueba",
           "intent": "VENTA_CONFIRMADA",
           "origen": "test_linux",
           "precio_catalogo": 50000,
           "precio_final": 45000
         }'

□ 5.2  Verificar Google Sheets
       → ¿Apareció el registro en ODI_AUDITORIA_2026__AUDITORIA?
       → ¿IDs generados correctamente?

□ 5.3  Verificar voz
       $ docker logs odi-voice --tail 10
       → ¿Mensaje generado?

□ 5.4  Test de reinicio
       $ docker compose restart
       $ docker ps
       → ¿Ambos healthy?
```

### FASE 6: Backups

```
□ 6.1  Crear script de backup
       → /opt/odi/scripts/backup.sh

□ 6.2  Contenido backup.sh:

#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR=/opt/odi/backups/daily

# Backup n8n data
tar -czf $BACKUP_DIR/n8n_$DATE.tar.gz -C /opt/odi/data n8n

# Backup voice data
tar -czf $BACKUP_DIR/voice_$DATE.tar.gz -C /opt/odi/data voice

# Rotación: mantener últimos 7 días
find $BACKUP_DIR -name "*.tar.gz" -mtime +7 -delete

echo "[$(date)] Backup completado: $DATE"

□ 6.3  Programar cron
       $ chmod +x /opt/odi/scripts/backup.sh
       $ crontab -e
       → Agregar: 0 3 * * * /opt/odi/scripts/backup.sh >> /opt/odi/logs/backup.log 2>&1
```

---

## ⏪ 5. PLAN DE ROLLBACK

```
ROLLBACK INMEDIATO:

1. Detener servicios Linux
   $ cd /opt/odi && docker compose down

2. Volver a Windows
   → Los servicios originales siguen ahí
   → Reactivar n8n Windows
   → Reactivar Flask Windows

3. Verificar funcionamiento
   → Mismo test de humo que antes

ROLLBACK PARCIAL (solo un servicio):

Si n8n Linux falla pero voice funciona:
   → Mantener n8n Windows
   → Apuntar n8n Windows → voice Linux (IP:7777)

Si voice Linux falla pero n8n funciona:
   → Mantener voice Windows
   → Apuntar n8n Linux → voice Windows (host.docker.internal:7777)
```

---

## 🔄 6. CAMBIO EN WORKFLOW n8n

**ÚNICO CAMBIO REQUERIDO:**

En el nodo "Voz ODI" (HTTP Request):

| Campo | Valor Actual (Windows) | Valor Nuevo (Linux) |
|-------|------------------------|---------------------|
| URL | `http://host.docker.internal:7777/odi/voice-response` | `http://odi-voice:7777/odi/voice-response` |

**Todo lo demás permanece IGUAL.**

---

## 📊 7. MATRIZ DE VALIDACIÓN POST-MIGRACIÓN

| Test | Comando | Resultado Esperado | ✓ |
|------|---------|-------------------|---|
| n8n responde | `curl localhost:5678/healthz` | `{"status":"ok"}` | □ |
| voice responde | `curl localhost:7777/` | `{"status":"ok","service":"ODI Voice Assistant"}` | □ |
| webhook procesa | POST a `/webhook/odi-v16-5-action` | `200 OK` + registro en Sheets | □ |
| voz genera mensaje | revisar logs voice | mensaje en consola | □ |
| IDs soberanos | revisar Sheets | `order_id` y `odi_event_id` únicos | □ |
| modo correcto | SKU conocido vs desconocido | AUTOMATICO vs SUPERVISADO | □ |
| umbral funciona | precio > 200K | modo SUPERVISADO | □ |
| reinicio sobrevive | `docker compose restart` | ambos healthy | □ |
| backup ejecuta | `/opt/odi/scripts/backup.sh` | archivos en `/backups/daily/` | □ |

---

## 📝 8. DEUDA TÉCNICA v16.9.2

```markdown
# ODI — Deuda Técnica v16.9.2
Fecha: 2026-01-11
Estado: DOCUMENTADA (no bloqueante para migración)

## Gaps Identificados

### DT-001: Ontología OMA Incompleta
- Implementado: intent, sku, producto, precio, modo, order_id, odi_event_id
- Faltante: actor (OMA Átomo 1), contexto (OMA Átomo 4), outcome formal (OMA Átomo 5)
- Severidad: Media
- Plan: v17.1 — Módulo M1.3

### DT-002: Cost-Gate No Implementado
- Referencia: RA-ODI #5
- Estado: No existe bloqueo de acciones con costo
- Severidad: Alta (para v2.0+)
- Plan: v17.2 — Módulo M1.8

### DT-003: Kill Switch No Implementado
- Referencia: MEO Pilar 1 (Soberanía del Usuario)
- Estado: No existe exportación ni borrado
- Severidad: Alta (ético/legal)
- Plan: v17.2 — Módulo M2.5

### DT-004: Throttler Emocional No Implementado
- Referencia: RA-ODI #4
- Estado: No hay ajuste de ritmo por estrés
- Severidad: Media (UX)
- Plan: v18.x — No bloqueante

### DT-005: Backups Rotativos Básicos
- Referencia: CA-V2.0
- Estado: Solo Sheets, sin local atómico
- Severidad: Media
- Plan: v17.0 — Incluido en migración Linux (FASE 6)

### DT-006: Logs Solo Consola
- Referencia: CA-V2.0
- Estado: Sin persistencia estructurada
- Severidad: Media
- Plan: v17.1 — Módulo M5.1

### DT-007: Dedupe No Implementado
- Referencia: Bloque E
- Estado: No hay ventana temporal ni idempotencia
- Severidad: Media
- Plan: v17.1 — Módulo M1.9
```

---

## 🎯 PROMPT PARA CHATGPT

```
CONTEXTO:
ODI v16.9.2 en producción temprana sobre Windows.
Migración aprobada a Linux (Ubuntu 22.04 LTS).

OBJETIVO:
Implementar migración Linux según especificación adjunta.

RESTRICCIONES:
- Ejecutar FASE por FASE
- Reportar resultado de cada checkbox antes de avanzar
- NO modificar lógica de negocio
- ÚNICO cambio en workflow: URL de voz (host.docker.internal → odi-voice)
- Mantener Windows funcional como rollback

ENTREGABLES POR FASE:
- Comandos ejecutados
- Output obtenido
- Checkbox marcado (✓ o ✗)
- Bloqueantes encontrados (si aplica)

CRITERIO DE ÉXITO:
- 9/9 tests de matriz de validación pasando
- Backup ejecutándose sin errores
- Ambos containers healthy después de restart
```

---

**FIN DEL DOCUMENTO**
