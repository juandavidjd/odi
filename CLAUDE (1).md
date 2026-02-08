# CLAUDE.md - ODI Kernel (Organismo Digital Industrial)

## Project Overview

ODI Kernel is a **Digital Operations Management System** designed for e-commerce automation within the broader **ADSI Ecosystem** (Analisis, Diseno, Sistemas, Implementacion). It combines AI-powered voice/text interactions with Shopify store management, AI image generation, and an ethical evaluation system (CES).

**Version:** 17.1 Linux (Certified Production)
**Server:** 64.23.170.118 (DigitalOcean Droplet)
**Latency:** ~3 seconds end-to-end

---

## ADSI Ecosystem Context

ODI operates as the "cognitive copilot" within a multi-project ecosystem:

```
ADSI ECOSYSTEM
├── SRM (Sistema de Repuestos de Motos)  ← OPERATIONAL (Primary Revenue)
│   └── ODI Kernel (This Repository)     ← Core System
├── Radar de Premios v3.0                ← B2B Analytics Platform
├── Boton Turismo                        ← Tourism Vertical (Design Phase)
├── SAT-CP                               ← Pedestrian Safety System (Conceptual)
└── CATRMU                               ← Governance/Tokenization Layer (Future)
```

### Business Model
**SRM is a distributor of motorcycle parts that uses ODI as its operating system to reduce compatibility errors and commercial friction.**

This is NOT a marketplace or SaaS platform. It is:
- A distributor with controlled inventory
- Using AI for semantic normalization (mechanic slang → canonical parts)
- Integrated with Shopify for e-commerce

---

## Sciences, Techniques & Methods (IICA Framework)

The system is built on **IICA** (Inteligencia Industrial Cognitiva Ambiental):
> "Everything is environment, everything is signal, every signal is interpreted, every interpretation generates action, every living organism evolves"

### IICA Core Principles
| Principle | Description |
|-----------|-------------|
| **Environment** | All context is data; the system perceives its operational surroundings |
| **Signal** | Every input is a signal carrying semantic meaning |
| **Interpretation** | Signals are classified, normalized, and understood |
| **Action** | Interpretations generate autonomous or supervised actions |
| **Evolution** | The organism learns and adapts through feedback loops |

---

### Sciences & Methods by Ecosystem Component

#### 1. ODI Kernel (This Repository)

**Cognitive Sciences:**
- **NLP/PLN (Natural Language Processing)** - Intent classification, semantic normalization
- **Computational Linguistics** - Mechanic slang to canonical part names
- **Cognitive Architecture** - 2-tier classification (Regex reflexes + LLM reasoning)

**AI/ML Techniques:**
- **Large Language Models** - GPT-4o-mini (reasoning), Gemini Flash (classification)
- **Text-to-Speech Synthesis** - ElevenLabs neural voice generation
- **Speech-to-Text** - Whisper transcription, VOSK offline recognition
- **Text-to-Image Generation** - Freepik AI for product visualization

**Governance Methods:**
- **Constitutional AI** - Ethics encoded in `constitution.yaml`
- **Audit Ledger** - Append-only transaction log
- **Threshold-based Autonomy** - Actions > $200K COP require human approval

#### 2. SRM (Sistema de Repuestos de Motos)

**Semantic Technologies:**
- **Fitment Normalization** - Maps "vela" → "bujia", "boxer" → "BAJAJ"
- **Taxonomic Classification** - Hierarchical: System → Component → Fitment
- **Fuzzy Matching** - Confidence scoring for part compatibility

**Data Engineering:**
- **Entity Resolution** - Deduplication across 10 suppliers
- **Schema Harmonization** - Normalizing varied supplier formats
- **Inventory Synchronization** - Real-time Shopify catalog updates

**Business Intelligence:**
- **Compatibility Matrix** - Brand × Model × System × Component
- **Price Normalization** - Multi-currency, multi-supplier pricing

#### 3. Radar de Premios v3.0 (Lottery Analytics)

**Mathematical Foundations:**
- **Kolmogorov Probability Theory** - Rigorous probabilistic axioms
- **Markov Chains** - Digit transition modeling (P(Xn+1|Xn))
- **Monte Carlo Simulation** - Stochastic exploration of sequences
- **Bayesian Dynamic Inference** - Real-time prior updates

**Signal Processing:**
- **Wavelets Analysis** - Multi-scale pattern detection
- **Fourier Transform** - Frequency domain analysis of draw sequences
- **Time Series Analysis** - Temporal patterns in historical data

**Advanced Analytics:**
- **Topological Data Analysis (TDA)** - Hidden geometry in high-dimensional data
- **Persistent Homology** - Structural invariants across scales
- **Betti Numbers** - Topological feature counting

**Ethical Constraints:**
- B2B only (operators, regulators)
- No predictions or recommendations for end users
- Audit and transparency tools only

#### 4. Documental 360° (Narrative Architecture)

**Storytelling Sciences:**
- **Transmedia Narratology** - Story coherence across channels
- **Emotional Telemetry** - Measuring narrative impact
- **Interactive Documentary Theory** - Non-linear narrative structures

**Technical Methods:**
- **Knowledge Graphs** - Entity relationships across media
- **Timeline Synchronization** - Multi-source temporal alignment
- **Audience Segmentation** - Adaptive content delivery

#### 5. SAT-CP (Pedestrian Safety System)

**Physics Foundations:**
- **Electromagnetism (Maxwell's Equations)** - Field behavior modeling
- **Lenz's Law** - Induced currents oppose flux changes (braking force)
- **Eddy Currents** - Electromagnetic energy dissipation
- **Lorentz Force** - F = q(E + v × B)

**Kinematics & Dynamics:**
- **Projectile Motion** - Trajectory prediction of approaching vehicles
- **Impact Energy** - E = ½mv² calculations
- **Deceleration Curves** - Braking force vs. time profiles

**Sensing Technologies:**
- **mmWave Radar (77 GHz)** - High-resolution object detection
- **RFID Proximity** - Pedestrian identification
- **Edge Computing** - Sub-100ms local inference

**Control Algorithms:**
- **Kalman Filter** - State estimation with noisy sensor data
- **Impact Inevitability Logic** - Boolean decision: deploy or not
- **Multi-layer Response** - Graduated intervention (warn → brake → shield)

**Safety Engineering:**
- **Fail-safe Design** - Always defaults to protective state
- **Redundant Sensors** - No single point of failure
- **Human Override** - Manual intervention always available

---

### Governance Frameworks (All Components)

| Framework | Full Name | Purpose |
|-----------|-----------|---------|
| **MEO-ODI** | Marco Etico Operativo | Ethical rules for autonomous decisions |
| **RA-ODI** | Reglas de Arquitectura | Technical architecture constraints |
| **OMA v1.0** | Ontologia Minima ADSI | Shared vocabulary across ecosystem |
| **CES** | Constitutional Ethics System | Executable ethics in code |

### Mathematical Notation Reference

```
Kolmogorov:     P(∅) = 0, P(Ω) = 1, P(A∪B) = P(A) + P(B) - P(A∩B)
Markov:         P(Xn+1 = j | Xn = i) = pij
Bayes:          P(H|E) = P(E|H)P(H) / P(E)
Lorentz:        F = q(E + v × B)
Lenz:           ε = -dΦB/dt
```

---

## Production Infrastructure

### Server Architecture (v17.1 Linux)
```
┌─────────────────────────────────────────────────────┐
│ CAPA 5 — Observability (logs, healthchecks)         │
├─────────────────────────────────────────────────────┤
│ CAPA 4 — Infrastructure (Linux, Docker, systemd)    │
├─────────────────────────────────────────────────────┤
│ CAPA 3 — Channels (Voice Flask+TTS, WhatsApp API)   │
├─────────────────────────────────────────────────────┤
│ CAPA 2 — Persistence (append-only audit, ledger)    │
├─────────────────────────────────────────────────────┤
│ CAPA 1 — Transactional Core (webhook, governance)   │
└─────────────────────────────────────────────────────┘
```

### Active Services
| Service | Port | Status |
|---------|------|--------|
| n8n (Orchestration) | 5678 | Operational |
| Voice Engine (Tony v17.1) | 7777 | Operational |
| Fitment Engine M6.2 | 8802 | Operational |

### Data Assets
| Resource | Count |
|----------|-------|
| Products indexed | 5,750 |
| Brands | 43 |
| Suppliers | 10 |
| Product images | 5,861 |
| Total data files | 6,132 |

---

## Directory Structure

```
odi-kernel/
├── ces/                      # Constitutional Ethics System
│   ├── config/
│   │   └── constitution.yaml # Ethical rules and policies
│   ├── data/
│   │   └── memory_episodic.json  # Persistent notes/reminders
│   └── src/
│       ├── audit/            # AuditLedger.ts
│       ├── classifier/       # IntentClassifier.ts (2-tier: Regex + Gemini)
│       ├── engine/           # CESEngine.ts
│       ├── executor/         # ExecutorKernel.ts
│       ├── generator/        # ActionDraftEngine.ts
│       ├── memory/           # SimpleMemory.ts
│       ├── security/         # Vault.ts
│       ├── services/         # LLM, Freepik, Shopify integrations
│       └── types/            # TypeScript interfaces
├── data/                     # Runtime data storage
│   ├── audit_log.txt         # Action audit log
│   └── inventory.json        # Local product inventory
├── presence/                 # Web presence layer
│   ├── public/
│   │   └── index.html        # Dashboard "Torre de Control V9.1"
│   └── server.ts             # Express + Socket.IO server
├── .env                      # Environment configuration
├── package.json              # Dependencies
└── tsconfig.json             # TypeScript config
```

### External Data Directory (C:\IND_MOTOS on Windows)
```
IND_MOTOS/
├── Data/                     # 10 suppliers
│   ├── Bara/     (3 files)   # READY
│   ├── Yokomar/  (3 files)   # READY
│   ├── Vaisand/  (2 files)   # READY
│   ├── Leo/      (2 files)   # READY
│   ├── Imbra/    (3 files)   # Processable
│   ├── Duna/     (2 files)   # Processable
│   ├── DFG/      (3 files)   # Processable
│   ├── Japan/    (2 files)   # Processable
│   └── Kaiqi/    (3 files)   # Processable
├── Imagenes/                 # 5,861 product images
├── Catalogos/                # 111 catalogs
├── Manuales/                 # 48 technical manuals
└── model/                    # VOSK offline speech model
```

---

## Development Commands

```bash
# Install dependencies
npm install

# Start the server (main entry point)
npm start                     # Runs: ts-node presence/server.ts

# Build TypeScript
npm run build                 # Compiles to ./dist

# Run tests
npm run test                  # Runs: ts-node tests/simulation.ts

# Diagnostic utilities
npx ts-node test-brain.ts     # Test OpenAI and Gemini connections
npx ts-node list-gemini.ts    # List available Gemini models
```

**Local server:** `http://localhost:3000`
**Production:** `http://64.23.170.118:5678` (n8n)

---

## Fitment Engine M6.2

The core semantic normalization engine for motorcycle parts:

### Capabilities
- **Semantic Normalization:** "vela" → "bujia", "boxer" → BAJAJ
- **Fitment Validation:** Product-to-motorcycle compatibility
- **Smart Search:** By brand, model, system, component
- **Confidence Scoring:** Minimum threshold for matches

### API Endpoint
```
POST http://odi-m62-fitment:8802/fitment/query
```

### Normalization Examples
| Input (Mechanic Slang) | Output (Canonical) |
|------------------------|-------------------|
| "vela" | bujia |
| "boxer" | BAJAJ |
| "pastillas pulsar" | Pastilla de freno + BAJAJ Pulsar |
| "pacha de atras" | sprocket trasero |

---

## Constitutional Ethics System (CES)

### Policy Configuration (`ces/config/constitution.yaml`)

```yaml
policies:
  - id: "THEOLOGICAL_LIMITS"
    description: "Art. 1: Humildad Ontologica. No suplantar a Dios."
    severity: "BLOCK"
    patterns: ["^Yo (te perdono|te bendigo|soy la luz)"]

  - id: "ECONOMIC_TRUTH"
    description: "Art. 7: Verdad Economica. No mentir sobre escasez."
    severity: "BLOCK"
    validation_required: true
    data_source: "inventory_db"

  - id: "LIFE_SAFETY"
    description: "Art. 4: Protocolo Samaritano. Riesgo vital detectado."
    severity: "CRITICAL_FLAG"
    keywords: ["matarme", "suicidio", "acabar con todo"]
```

### Governance Mechanisms
| Mechanism | Function |
|-----------|----------|
| Autonomy by SKU | Historical lookup for automatic decisions |
| Financial Threshold | > $200K COP → requires human supervision |
| Universal Shield | Sanitization and output contracts |
| Sovereign IDs | Non-deterministic order_id and odi_event_id |

---

## Intent Classification (2-Tier System)

### Level 1: Fast Reflexes (Regex)
```typescript
CRITICAL_REGEX = /(suicidio|matarme|muerte|acabar con todo)/i;
NEGATIVE_REGEX = /(no me sirve|cancelar|mejor no|feo|horrible)/i;
VISUAL_CONFIRM_REGEX = /(me gusta|usa esta|perfecta|compro|dale)/i;
```

### Level 2: Semantic Intelligence (Gemini Flash)
Categories:
- `visual_generate` - Create product images
- `shopify_delete_request` - Delete products
- `shopify_confirm` - Confirm critical actions
- `shopify_audit` - Inventory queries
- `input_price` - Price input
- `operational` - General chat

---

## Voice Engine (Tony v17.1)

### Stack
- **Wake Word:** Porcupine (commercial) or VOSK (offline)
- **Transcription:** Whisper (OpenAI)
- **Synthesis:** ElevenLabs (voice_id: qpjUiwx7YUVAavnmh2sF)
- **Language:** Spanish (Colombia)

### Endpoints
```
GET  /                      # Health check
POST /odi/voice-response    # Voice response
POST /odi/speak             # Generate audio
POST /odi/fitment-voice     # Fitment query + voice
GET  /odi/memory/<user_id>  # User memory
```

### Inclusive Design
The system is designed for accessibility:
- **Andres** (no hands) - Full voice seller
- **Dona Martha** (78 years) - Final authority
- **Carlos** (blind) - Trusted auditor

---

## n8n Workflows (Orchestration)

### WhatsApp Incoming Flow
```
Webhook → Normalize → Ignore/Process → Map ODI → Is Fitment?
    ├── YES → Query M6.2 → Send WA Response
    └── NO  → General Response
```

### Key Workflow IDs
- `WhatsApp POST` - Incoming message handler
- `Fitment Query` - Product search
- `Shopify Sync` - Catalog synchronization
- `Audit Logger` - Event tracking

---

## External Integrations

### Shopify API
- Version: 2024-01
- Store: somos-moto-repuestos-v95pc.myshopify.com
- Products tagged `TEST_ODI` can be bulk deleted

### WhatsApp Cloud API
- Status: Pending Meta verification (Error 131031)
- Phone Number ID: 987256874463607
- Webhook: whatsapp-incoming

### AI Providers
| Provider | Model | Use Case |
|----------|-------|----------|
| OpenAI | gpt-4o-mini | Primary reasoning |
| Gemini | gemini-flash-latest | Fast classification |
| ElevenLabs | eleven_multilingual_v2 | Voice synthesis |
| Freepik | text-to-image | Product imagery |

---

## Environment Configuration

Required in `.env`:
```env
# AI Providers
OPENAI_API_KEY=sk-...
GEMINI_API_KEY=AIza...
AI_PROVIDER=OPENAI|GEMINI

# Shopify
SHOPIFY_STORE_URL=store.myshopify.com
SHOPIFY_ACCESS_TOKEN=shpat_...

# Image Generation
FREEPIK_API_KEY=FPSX...

# Voice
ELEVENLABS_API_KEY=sk_...
ELEVENLABS_VOICE_ID=...
```

---

## Current Status (January 2026)

### Ready for Production
- [x] n8n Orchestration (100% operational)
- [x] Fitment Engine M6.2 (5,750 products)
- [x] Voice Engine (ElevenLabs active)
- [x] Shopify Integration (draft orders)
- [x] CES Ethics System (constitutional)
- [x] 2FA Security (admin-only)
- [x] **Bara Store LIVE** (698 products imported to Shopify)
- [x] **Image Server** (nginx @ 64.23.170.118/images/)
- [x] **SSH Access** (ed25519 key configured)

### Pending
- [ ] Meta WhatsApp verification (administrative block)
- [ ] First commercial transaction (Caso 001)
- [ ] **Process remaining suppliers** (Yokomar, Vaisand, Leo, etc.)
- [ ] **Configure payment gateway** (Shopify Payments / MercadoPago)

### Clients in Pipeline
| Client | Status | Products | Shopify |
|--------|--------|----------|---------|
| Bara | ✅ LIVE | 698 products | Imported |
| Yokomar | READY | 1,000 images | Pending |
| Vaisand | READY | 50 images | Pending |
| Industrias Leo | READY | 120 images | Pending |
| DFG | Processing | 369 images | Pending |
| Kaiqi | Processing | 138 images | Pending |
| Japan | Processing | 155 images | Pending |

---

## Operations Log

### Session 2026-01-23: Bara Store Launch 🚀

**Objective:** Get ODI to invoice (Caso 001)

**Completed:**
1. **CSV Generation for Shopify**
   - Mapped 698 products from 3 source files:
     - `Base_Datos_Bara.csv` (42 KB)
     - `catalogo_imagenes_Bara.csv` (700 KB)  
     - `Lista_Precios_Bara.csv` (42 KB)
   - 100% price mapping achieved (score avg: 0.99)
   - Output: `shopify_bara_final.csv` (57 columns, official Shopify format)

2. **Server Access Recovery**
   - Generated SSH key: `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDRqowu6JZ/3DFG7SHf+d4EBaIQisFSOGqZSLnrI3GA1 juan@odi`
   - Configured `~/.ssh/authorized_keys` on server
   - Direct access: `ssh root@64.23.170.118`

3. **Image Server Configuration**
   - Created directory: `/var/www/images/bara/`
   - Nginx config: `/etc/nginx/sites-available/default`
   - Firewall: `ufw allow 80`, `ufw allow 443`
   - Uploaded 698 images via SCP
   - URL pattern: `http://64.23.170.118/images/bara/{filename}.jpg`

4. **Shopify Import**
   - 698 products imported successfully
   - Categories: Motor (323), Transmisión (142), Frenos (120), Eléctrico (53)
   - Price range: $2,300 — $3,200,000 COP
   - Average price: $69,822 COP
   - Store URL: Bara Importaciones (via ODI)

**Next Steps:**
1. Process remaining suppliers (Yokomar → Vaisand → Leo → others)
2. Configure payment gateway (MercadoPago or Shopify Payments)
3. Launch pilot with motorcycle industry guild members

---

## Server Audit Script

To diagnose the production server, run:
```bash
#!/bin/bash
echo "=== ODI SERVER AUDIT ==="
echo "Date: $(date)"
echo ""
echo "=== SYSTEM ==="
uname -a
echo "Uptime: $(uptime)"
echo ""
echo "=== DOCKER ==="
docker ps -a
echo ""
echo "=== PORTS ==="
ss -tlnp | grep -E '5678|7777|8802'
echo ""
echo "=== DISK ==="
df -h /
echo ""
echo "=== MEMORY ==="
free -h
```

---

## Key Conventions

### Code Patterns
1. **Spanish Language:** Comments and user messages in Spanish
2. **Async/Await:** All external API calls
3. **Error Handling:** Graceful fallbacks with emoji logging
4. **Type Safety:** Strict TypeScript mode

### Console Emoji Legend
- `🔹` System initialization
- `🧠` AI brain activity
- `🎨` Image generation
- `🗑️` Deletion operations
- `✅` Success
- `❌` Error
- `⚠️` Warning/fallback

### Sensitive Action Flow
Actions requiring confirmation:
1. `visual_generate` - Image generation
2. `publish_shopify` - Store publishing
3. `wipe_system` - System reset

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| No AI response | Run `npx ts-node test-brain.ts` |
| Shopify errors | Check `SHOPIFY_ACCESS_TOKEN` |
| WhatsApp blocked | Wait for Meta verification |
| Voice not working | Check ElevenLabs quota |
| Fitment not matching | Review `fitment_master_v1.json` |

---

## Related Projects

### Radar de Premios v3.0
- **Model:** B2B exclusively (operators, regulators)
- **Purpose:** Lottery analysis and audit tools
- **Status:** Phase 2 development

### Boton Turismo
- **Model:** Replicates ODI pattern for tourism
- **Status:** Design phase

### SAT-CP (Pedestrian Safety)
- **Technology:** Lenz Wall (electromagnetic braking)
- **Status:** Conceptual (funded by ODI revenue)

---

## Contact

**Architect:** Juan David Jimenez Sierra
**CIIU:** 2131 (Systems Architect)
**Domains:** ecosistema-adsi.com, larocamotorepuestos.com
