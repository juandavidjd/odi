# ODI PROJECT STATUS
## Última actualización: 4 Febrero 2026

---

## 🏗️ ARQUITECTURA DEFINIDA (RESPETAR SIEMPRE)

```
┌─────────────────────────────────────────────────────────────┐
│  GITHUB                    │  WINSCP                        │
│  ─────────────────────     │  ───────────────────────────   │
│  • Código/Scripts          │  • Archivos pesados            │
│  • Perfiles YAML           │  • Catálogos Excel/PDF         │
│  • Configuraciones         │  • Imágenes de productos       │
│  • Versionado/respaldo     │  • Paquetes completos empresa  │
│                            │                                │
│  Repo: juandavidjd/extrac  │  Destino: /mnt/volume_sfo3_01/ │
│  Branch: claude/load-...   │                                │
└─────────────────────────────────────────────────────────────┘
```

### Servidor de Producción
- IP: 64.23.170.118 (DigitalOcean)
- Usuario: root
- Sistema: Ubuntu 22.04 LTS
- Dominios: ecosistema-adsi.com, larocamotorepuestos.com, somosrepuestosmotos.com

### Directorios Clave (Servidor)
- `/opt/odi/` - Sistema en producción
- `/opt/odi/extractors/` - Scripts de extracción
- `/opt/odi/profiles/` - Perfiles YAML de empresas
- `/mnt/volume_sfo3_01/` - Volumen de datos (200GB)
- `/mnt/volume_sfo3_01/profesion/10 empresas ecosistema ODI/Data/` - Catálogos por empresa
- `/tmp/odi_output/` - Salidas de procesamiento temporal
- `~/.odi/cache/embeddings_cache.db` - Cache SQLite de embeddings

---

## ✅ COMPONENTES OPERATIVOS (v17.2)

| Componente | Versión | Estado | Ubicación |
|------------|---------|--------|-----------|
| Vision Extractor | v3.2 | ✅ | /opt/odi/extractors/ |
| Price Processor | v1.0 | ✅ | /opt/odi/extractors/ |
| Catalog Enricher | v1.0 | ✅ | /opt/odi/extractors/ |
| Semantic Normalizer | v1.2 | ✅ | /opt/odi/extractors/ |
| Pipeline Orchestrator | v1.2 | ✅ | /opt/odi/extractors/ |
| Industrial Extractor | v2.0 | ✅ | /opt/odi/extractors/ |
| Excel Converter | v1.0 | ✅ | /opt/odi/extractors/ |
| VariantPreClassifier | v1.0 | ✅ | Integrado en Normalizer |
| SQLite Embedding Cache | v1.0 | ✅ | ~/.odi/cache/ |

---

## 📊 YOKOMAR - PROCESADO COMPLETAMENTE

### Archivos de Entrada
- Base_Datos_Yokomar.csv: 1,000 productos
- Lista de Precios (Excel 28-01-2026): 843 precios

### Resultados del Pipeline
| Métrica | Valor |
|---------|-------|
| Productos procesados | 1,000 |
| Con precio | 387 |
| Embeddings generados | 1,000 |
| Embeddings en cache | 1,459 |
| Duplicados detectados | 305 (187 grupos) |
| Familias totales | 190 |
| - Pre-clasificadas | 7 (variantes talla/litros) |
| - Por código/embedding | 183 |
| Productos con fitment | 318 |
| Marca detectada | 97.2% |
| Modelo detectado | 92.8% |

### Archivos Generados (servidor)
- `/tmp/odi_output/YOK_NORMALIZED.csv` - Catálogo normalizado
- `/tmp/odi_output/YOK_NORMALIZED_metadata.json` - Metadata
- `/tmp/odi_output/Lista_Precios_Yokomar_2026.csv` - Precios limpios

---

## 🏢 EMPRESAS CONFIGURADAS (13 total)

| Empresa | Perfil YAML | Productos | Estado |
|---------|-------------|-----------|--------|
| YOKOMAR | ✅ yokomar.yaml | 1,000 | ✅ Procesado |
| Bara Importaciones | ⏳ | ~500 | Pendiente |
| Kaiqi | ⏳ | ~800 | Pendiente |
| Vitton | ⏳ | ~200 | Pendiente |
| Vaisand | ⏳ | - | Pendiente |
| Imbra | ⏳ | - | Pendiente |
| Duna | ⏳ | - | Pendiente |
| Industrias Leo | ⏳ | - | Pendiente |
| Armotos | ⏳ | 1,586 | Extraído |
| DFG | ⏳ | - | Pendiente |
| CBI | ⏳ | - | Pendiente |
| Japan | ⏳ | - | Pendiente |
| Store | ⏳ | - | Pendiente |

---

## ⏳ META BUSINESS VERIFICATION

**Estado**: EN REVISIÓN (enviado 3 Feb 2026)
**Tiempo estimado**: 2-7 días hábiles (respuesta esperada: 5-10 Feb 2026)

### Documentos Enviados
- RUT de LA ROCA MOTOREPUESTOS (NIT: 10776560-1)
- Dirección: MZ 14 CA 1 SEC A PARQUE INDUSTRIAL, Pereira
- Teléfono: +57 3114368937
- Website: https://larocamotorepuestos.com

### WhatsApp Templates (6 activos)
- odi_saludo
- odi_contract_approval
- odi_shipping_update
- odi_order_status
- odi_order_confirm
- hello_world

---

## 🎯 PRÓXIMOS PASOS

1. **Esperar Meta Verification** (bloqueador principal)
2. **Mover archivos Yokomar a ubicación permanente**:
   ```bash
   mkdir -p /opt/odi/data/yokomar
   cp /tmp/odi_output/YOK_NORMALIZED.csv /opt/odi/data/yokomar/
   ```
3. **Procesar Bara, Kaiqi, Vitton** con el pipeline genérico
4. **Activar WhatsApp** cuando Meta apruebe
5. **Ejecutar Caso 001** - Primera venta real

---

## 📦 DEPENDENCIAS INSTALADAS (servidor)

```
Python 3.10
pandas
openpyxl (para Excel sin Java)
pyyaml
openai (embeddings)
scikit-learn (clustering)
chromadb (RAG)
flask
n8n (Docker)
```

---

## 🔧 COMANDOS ÚTILES

### Procesar empresa con pipeline genérico
```bash
cd /opt/odi/extractors
python3 odi_industrial_extractor.py --profile yokomar -o /tmp/odi_output/
```

### Normalizar con embeddings
```bash
export $(cat /opt/odi/.env | xargs)
python3 odi_semantic_normalizer.py input.csv -o output.csv
```

### Convertir Excel a CSV (sin Java)
```bash
python3 odi_xlsx_to_csv.py archivo.xlsx --price-mode -o precios.csv
```

### Ver perfiles disponibles
```bash
python3 odi_industrial_extractor.py --list-profiles
```

---

## ⚠️ NOTAS IMPORTANTES

1. **NO buscar datos en este entorno** - Los datos están en el servidor
2. **Código → GitHub**, **Datos pesados → WinSCP**
3. **API Key OpenAI** está en `/opt/odi/.env`
4. **Cache de embeddings** se guarda en SQLite para reutilización
5. **El preprocesador de Yokomar necesita apuntar al archivo de precios 2026**

---

## 📞 CONTACTO

- Juan David Jiménez
- WhatsApp: +57 3114368937
- Negocio: LA ROCA MOTOREPUESTOS
- NIT: 10.776.560-1
