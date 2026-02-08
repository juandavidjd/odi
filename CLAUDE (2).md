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
| **Image Server (nginx)** | 80 | **Operational** |

### Data Assets (Updated 2026-01-23)
| Resource | Count |
|----------|-------|
| **Products indexed** | **12,749** |
| Brands | 43 |
| **Suppliers** | **10 (ALL LIVE)** |
| Product images | ~10,000+ |
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
├── Data/                     # 10 suppliers (ALL PROCESSED)
│   ├── Bara/     (3 files)   # ✅ LIVE - 698 products
│   ├── Yokomar/  (3 files)   # ✅ LIVE - 977 products
│   ├── Vaisand/  (2 files)   # ✅ LIVE - 50 products
│   ├── Leo/      (2 files)   # ✅ LIVE - 114 products
│   ├── Imbra/    (3 files)   # ✅ LIVE - 1,094 products
│   ├── Duna/     (2 files)   # ✅ LIVE - 1,200 products
│   ├── DFG/      (3 files)   # ✅ LIVE - 7,443 products
│   ├── Japan/    (2 files)   # ✅ LIVE - 729 products
│   ├── Kaiqi/    (3 files)   # ✅ LIVE - 378 products
│   └── Store/    (2 files)   # ✅ LIVE - 66 products
├── Imagenes/                 # ~10,000+ product images
├── Catalogos/                # 111 catalogs
├── Manuales/                 # 48 technical manuals
└── model/                    # VOSK offline speech model
```

### Image Server Directories
```
/var/www/images/
├── bara/      # 698 images
├── yokomar/   # 977 images
├── kaiqi/     # 138 images
├── dfg/       # 3,296 images
├── duna/      # 1,200 images
├── japan/     # 734 images
├── leo/       # 114 images (renamed: spaces → hyphens)
└── store/     # 66 images (renamed: spaces → hyphens)
```

**Note:** Imbra and Vaisand use external CDN (Shopify CDN and vaisand.com respectively)

---

## Current Status (January 23, 2026)

### 🏆 ODI 100% OPERATIONAL - ALL 10 STORES READY TO INVOICE 🏆

| Supplier | Products | Images | Prices | Status |
|----------|----------|--------|--------|--------|
| Bara | 698 | ✅ Server | ✅ Real | ✅ LIVE |
| Yokomar | 977 | ✅ Server | ✅ Real | ✅ LIVE |
| Kaiqi | 378 | ✅ Server | ✅ Real | ✅ LIVE |
| DFG | 7,443 | ✅ Server | ✅ Real | ✅ LIVE |
| Duna | 1,200 | ✅ Server | ⚠️ Temp $50K | ✅ LIVE |
| Imbra | 1,094 | ✅ CDN | ✅ Real | ✅ LIVE |
| Japan | 729 | ✅ Server | ⚠️ Temp $50K | ✅ LIVE |
| Leo | 114 | ✅ Server | ⚠️ Temp $50K | ✅ LIVE |
| Store | 66 | ✅ Server | ⚠️ Temp $50K | ✅ LIVE |
| Vaisand | 50 | ✅ CDN | ⚠️ Temp $50K | ✅ LIVE |
| **TOTAL** | **12,749** | | | **10/10 LIVE** |

### ✅ Payment Gateway: WOMPI (Bancolombia) - ALL 10 STORES

| Payment Method | Status |
|----------------|--------|
| Visa | ✅ Active |
| Mastercard | ✅ Active |
| American Express | ✅ Active |
| Bancolombia (Botón) | ✅ Active |
| Nequi | ✅ Active |
| DaviPlata | ✅ Active |
| PSE (Bank Transfer) | ✅ Active |

**Wompi Credentials:**
- Public Key: `pub_prod_kq2trmwV3fUIw6ybpbI2jwj5Kwh2whTA`
- Private Key: (stored securely in Wompi dashboard)
- Webhook URL: `https://wompi-event-shopify.conexa.ai/api/v1/shopify/webhooks/event`

**Commission:** ~2.79% + COP 900 per transaction (+ Shopify fee if applicable)

### ✅ Checkout Verified - All 10 Stores

| Store | Test Product | Total (COP) | Wompi |
|-------|--------------|-------------|-------|
| Carguero Store | Kit cilindro motocarguero | $133,951 | ✅ |
| YOKOMAR | Disco freno 115cc | $199,325 | ✅ |
| Industrias LEO | CDI 125cc electrónico | $714,000 | ✅ |
| Industrias Japan | Palanca cambio cromada | $714,000 | ✅ |
| Imbra | Alineador cadena universal | $293,341 | ✅ |
| DUNA | Bombilla halógena 12V | $2,975,000 | ✅ |
| KAIQI PARTS | Ventilador radiador | $446,250 | ✅ |
| Bara Importaciones | Balancín motor 205cc | $318,920 | ✅ |
| DFG | Amortiguadores traseros | $971,135 | ✅ |
| Vaisand | Adaptador carburador | $74,451 | ✅ |

### Ready for Production
- [x] n8n Orchestration (100% operational)
- [x] Fitment Engine M6.2 (12,749 products)
- [x] Voice Engine (ElevenLabs active)
- [x] Shopify Integration (10 stores)
- [x] CES Ethics System (constitutional)
- [x] 2FA Security (admin-only)
- [x] **Image Server** (nginx @ 64.23.170.118/images/)
- [x] **SSH Access** (ed25519 key configured)
- [x] **ALL 10 SUPPLIERS LIVE**
- [x] **WOMPI PAYMENT GATEWAY - 10/10 STORES** ✅
- [x] **ALL CHECKOUTS VERIFIED AND FUNCTIONAL** ✅

### Pending
- [ ] Meta WhatsApp verification (administrative block)
- [ ] **First commercial transaction (Caso 001)** ← 🚀 READY TO EXECUTE!
- [ ] **Update temporary prices** (Duna, Japan, Leo, Store, Vaisand)

---

## Operations Log

### Session 2026-01-23: ODI FULLY OPERATIONAL 🚀🚀🚀

**Objective:** Get all 10 suppliers operational + Configure payment gateway

**🏆 MISSION 100% ACCOMPLISHED 🏆**

#### Phase 1: All Suppliers Live (12,749 products)

1. **Bara** - 698 products with real prices
2. **Yokomar** - 977 products, 1,000 images uploaded
3. **Kaiqi** - 378 products, fixed 4 missing motor images
4. **DFG** - 7,443 products (largest supplier), smart image matching
5. **Duna** - 1,200 products (100% images), temp pricing
6. **Imbra** - 1,094 products, Shopify CDN images
7. **Japan** - 729 products, temp pricing
8. **Leo** - 114 products, fixed filename spaces issue
9. **Store** - 66 motocarguero products, fixed filename spaces
10. **Vaisand** - 50 products, external CDN (vaisand.com)

#### Phase 2: Payment Gateway Configuration ✅

**Wompi (Bancolombia) Successfully Configured:**

1. **Account Setup**
   - Created Wompi account at comercios.wompi.co
   - Account activated and verified
   - Production credentials obtained

2. **Shopify Integration**
   - Found Wompi Colombia plugin (via Shopify partner integration)
   - Installed on Vaisand store as pilot
   - Connected production credentials
   - Configured webhook URL

3. **Payment Methods Enabled:**
   - ✅ Visa
   - ✅ Mastercard
   - ✅ American Express
   - ✅ Bancolombia (Botón)
   - ✅ Nequi
   - ✅ DaviPlata
   - ✅ PSE (Pagos Electrónicos Seguros)

#### Phase 3: Wompi Deployed to ALL 10 Stores ✅✅✅

**Replicated Wompi configuration across all stores:**

| Store | Test Product | Total Verified |
|-------|--------------|----------------|
| Carguero Store | Kit cilindro motocarguero | $133,951 ✅ |
| YOKOMAR | Disco freno 115cc | $199,325 ✅ |
| Industrias LEO | CDI 125cc electrónico | $714,000 ✅ |
| Industrias Japan | Palanca cambio cromada | $714,000 ✅ |
| Imbra | Alineador cadena universal | $293,341 ✅ |
| DUNA | Bombilla halógena 12V | $2,975,000 ✅ |
| KAIQI PARTS | Ventilador radiador | $446,250 ✅ |
| Bara Importaciones | Balancín motor 205cc | $318,920 ✅ |
| DFG | Amortiguadores traseros | $971,135 ✅ |
| Vaisand | Adaptador carburador | $74,451 ✅ |

**TOTAL STORES WITH WOMPI: 10/10** 🎉

**Technical Issues Resolved:**
- Filename spaces causing 403 errors → Renamed with hyphens (Leo, Store)
- Image URL mismatches → Regenerated CSVs
- Encoding issues (UTF-8-sig) → Handled in Python scripts
- Permission issues → chmod 755 + chown www-data
- Wompi El Salvador vs Colombia confusion → Found correct plugin via partner page

**Wompi Integration Notes:**
- Plugin URL: Found through Shopify partner integration (not direct app store)
- Requires both production AND sandbox credentials
- Webhook URL: `https://wompi-event-shopify.conexa.ai/api/v1/shopify/webhooks/event`
- Mode: Production (sandbox disabled for real transactions)

**Final Status:**
1. ~~Configure payment gateway~~ ✅ DONE
2. ~~Replicate Wompi setup on remaining 9 stores~~ ✅ DONE (ALL 10 STORES LIVE)
3. Execute first commercial transaction (Caso 001) ← 🚀 READY!
4. Update temporary prices when suppliers provide them
5. Launch pilot with motorcycle industry guild members

---

### Server Commands Reference

```bash
# Rename files with spaces to hyphens
cd /var/www/images/{supplier}
for f in *.png *.jpg; do mv "$f" "$(echo $f | tr ' ' '-')" 2>/dev/null; done

# Fix permissions
chmod -R 755 /var/www/images/{supplier}
chown -R www-data:www-data /var/www/images/{supplier}

# Verify images accessible
curl -I http://64.23.170.118/images/{supplier}/filename.jpg

# Count images per directory
for dir in /var/www/images/*/; do
  echo "$(basename $dir): $(ls -1 "$dir" 2>/dev/null | wc -l) images"
done
```

---

### Session 2026-01-23 (Earlier): Bara Store Launch

**Completed:**
1. **CSV Generation for Shopify**
   - Mapped 698 products from 3 source files
   - 100% price mapping achieved

2. **Server Access Recovery**
   - Generated SSH key: `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDRqowu6JZ/3DFG7SHf+d4EBaIQisFSOGqZSLnrI3GA1 juan@odi`
   - Configured `~/.ssh/authorized_keys` on server
   - Direct access: `ssh root@64.23.170.118`

3. **Image Server Configuration**
   - Created directory: `/var/www/images/bara/`
   - Nginx config: `/etc/nginx/sites-available/default`
   - Firewall: `ufw allow 80`, `ufw allow 443`
   - URL pattern: `http://64.23.170.118/images/{supplier}/{filename}`

4. **Shopify Import**
   - 698 products imported successfully

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
ss -tlnp | grep -E '5678|7777|8802|80'
echo ""
echo "=== DISK ==="
df -h /
echo ""
echo "=== MEMORY ==="
free -h
echo ""
echo "=== IMAGE SERVER ==="
ls -la /var/www/images/
echo ""
echo "=== IMAGE COUNTS ==="
for dir in /var/www/images/*/; do
  echo "$(basename $dir): $(ls -1 "$dir" 2>/dev/null | wc -l) images"
done
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
- Stores: 10 active supplier stores
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
| Images 403 error | Check file permissions and nginx config |
| Spaces in filenames | Rename: `for f in *\ *; do mv "$f" "${f// /-}"; done` |

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
