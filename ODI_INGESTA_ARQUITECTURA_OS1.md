# ODI - Arquitectura de Ingesta Cognitiva
## Inspirado en OS1 (Her) - Procesamiento Invisible

---

## 1. Filosofía Central

> "ODI no es una herramienta que usas. Es un organismo que trabaja contigo."

### Principios de Diseño

| Software Tradicional | ODI (Enfoque Cognitivo) |
|---------------------|------------------------|
| Carga manual / Mapeo rígido | Ingesta por Visión Artificial |
| Clics, menús y formularios | Diálogo con los datos / Automatización |
| Almacenar información | Normalizar y "entender" el caos |
| Intrusiva (necesitas estar frente a ella) | Ambiental (trabaja en el backend) |
| Estados de "cargando..." | Estados de "comprendiendo..." |

---

## 2. Arquitectura del Repositorio de Ingesta

```
/opt/odi/
├── ingesta/
│   ├── boca/                    # 🎯 PUNTO DE ENTRADA ÚNICO
│   │   ├── dropzone/            # Usuario suelta archivos aquí
│   │   ├── urls/                # Enlaces para scraping
│   │   └── whatsapp/            # Archivos recibidos por WA
│   │
│   ├── cognitivo/               # 🧠 PROCESAMIENTO INVISIBLE
│   │   ├── percepcion/          # Visión artificial detecta tipo
│   │   ├── comprension/         # NLP extrae semántica
│   │   └── memoria/             # ChromaDB embeddings
│   │
│   ├── organizacion/            # 📁 ODI ORGANIZA AUTOMÁTICAMENTE
│   │   ├── empresas/
│   │   │   ├── {empresa_uuid}/
│   │   │   │   ├── identidad/   # Logo, colores, datos empresa
│   │   │   │   ├── catalogo/    # Productos detectados
│   │   │   │   ├── precios/     # Listas de precios
│   │   │   │   ├── imagenes/    # Fotos de productos
│   │   │   │   └── fitment/     # Compatibilidades motos
│   │   │   └── ...
│   │   └── taxonomia/           # Estructura SRM unificada
│   │
│   ├── enriquecimiento/         # ✨ VALOR AGREGADO ODI
│   │   ├── descripciones_ia/    # GPT genera descripciones
│   │   ├── fitment_engine/      # Motor de compatibilidad
│   │   └── fichas_360/          # Fichas técnicas completas
│   │
│   └── salida/                  # 📤 LISTO PARA COMERCIO
│       ├── shopify/             # Formato Shopify
│       ├── woocommerce/         # Formato WooCommerce
│       ├── mercadolibre/        # Formato ML
│       └── api/                 # JSON para integraciones
│
├── dialogo/                     # 💬 INTERFAZ CONVERSACIONAL
│   ├── whatsapp/                # Interacción WA
│   ├── web/                     # Chat web SRM Intelligent
│   └── voice/                   # ElevenLabs Tony/Ramona
│
└── consciencia/                 # 🔮 ESTADO DEL ORGANISMO
    ├── pulso/                   # Métricas en tiempo real
    ├── aprendizaje/             # Patrones detectados
    └── excepciones/             # Human-in-the-loop queue
```

---

## 3. Flujo de Ingesta Cognitiva

### 3.1 Usuario "Muestra" un Archivo

```
ENTRADA: Usuario arrastra PDF de catálogo a la interfaz
         (o envía por WhatsApp, o pega URL)

ODI PERCIBE:
├── Tipo de archivo: PDF
├── Páginas: 47
├── Contenido visual: Tablas + Imágenes de productos
└── Idioma: Español

ODI COMPRENDE:
├── Empresa detectada: "YOKOMAR SAS" (logo en header)
├── Tipo de documento: Catálogo de precios
├── Estructura: Código | Descripción | Precio | Imagen
└── Categorías: Motor, Transmisión, Frenos, Eléctrico

ODI ORGANIZA:
├── Crea carpeta: /organizacion/empresas/yokomar-uuid/
├── Extrae 1,612 SKUs
├── Asocia 1,000 imágenes
└── Detecta 379 con precio completo

ODI ENRIQUECE:
├── Genera descripciones SEO
├── Calcula compatibilidades (fitment)
└── Crea fichas 360°

ODI INFORMA (solo si necesario):
└── "Encontré 621 productos sin precio. ¿Tienes la lista de precios actualizada?"
```

### 3.2 Estados de Consciencia (No "Cargando...")

| Estado Tradicional | Estado ODI |
|-------------------|------------|
| "Cargando..." | "Observando tu catálogo..." |
| "Procesando..." | "Comprendiendo la estructura..." |
| "Importando datos..." | "Organizando 1,612 productos..." |
| "Error de formato" | "Este formato es nuevo para mí. ¿Me ayudas a entenderlo?" |
| "Completado" | "Tu catálogo está listo. Encontré oportunidades de mejora." |

---

## 4. Detección Automática de Tipo de Archivo

```python
class ODIPercepcion:
    """
    ODI detecta automáticamente qué tipo de información contiene
    cada archivo, sin mapeo manual del usuario.
    """
    
    TIPOS_DETECTABLES = {
        'catalogo': ['sku', 'codigo', 'referencia', 'producto'],
        'precios': ['precio', 'valor', 'costo', 'pvp'],
        'imagenes': ['.jpg', '.png', '.gif', '.webp'],
        'identidad': ['logo', 'marca', 'empresa', 'nit'],
        'fitment': ['moto', 'modelo', 'año', 'compatible'],
    }
    
    def percibir(self, archivo):
        """
        Como Samantha viendo a través de la cámara,
        ODI "ve" el contenido y lo clasifica.
        """
        # 1. Detectar formato físico
        formato = self.detectar_formato(archivo)  # PDF, XLSX, CSV, IMG
        
        # 2. Extraer contenido según formato
        contenido = self.extraer_contenido(archivo, formato)
        
        # 3. Analizar semánticamente
        tipo = self.clasificar_semanticamente(contenido)
        
        # 4. Detectar empresa (si hay logo o nombre)
        empresa = self.identificar_empresa(contenido)
        
        return {
            'formato': formato,
            'tipo': tipo,
            'empresa': empresa,
            'confianza': 0.95,
            'requiere_humano': False
        }
```

---

## 5. Human-in-the-Loop: Cuándo ODI Pregunta

ODI trabaja en silencio, pero emerge cuando necesita criterio humano:

### Triggers para Intervención Humana

```yaml
excepciones:
  ambiguedad_precio:
    condicion: "Múltiples columnas podrían ser precio"
    pregunta: "¿Cuál es el precio de venta? ¿A o B?"
    
  empresa_nueva:
    condicion: "No reconozco esta empresa"
    pregunta: "Parece un catálogo nuevo. ¿De qué empresa es?"
    
  formato_desconocido:
    condicion: "Estructura no reconocida"
    pregunta: "Este formato es diferente. ¿Me muestras un ejemplo?"
    
  conflicto_datos:
    condicion: "El mismo SKU tiene precios diferentes"
    pregunta: "Encontré precios distintos para M110053. ¿Cuál es correcto?"
    
  calidad_imagen:
    condicion: "Imagen muy pequeña o borrosa"
    pregunta: "Esta imagen no se ve bien. ¿Tienes una mejor resolución?"
```

### Interfaz de Excepción (Mínima)

```
┌─────────────────────────────────────────────────────┐
│  🧠 ODI necesita tu ayuda                           │
│                                                      │
│  Encontré dos columnas que podrían ser el precio:  │
│                                                      │
│  ┌─────────────┬─────────────┐                      │
│  │ PRECIO      │ PVP         │                      │
│  ├─────────────┼─────────────┤                      │
│  │ $45,000     │ $52,000     │                      │
│  └─────────────┴─────────────┘                      │
│                                                      │
│  ¿Cuál uso para la tienda?                          │
│                                                      │
│  [PRECIO - Costo]    [PVP - Venta al público]       │
│                                                      │
└─────────────────────────────────────────────────────┘
```

---

## 6. Diálogo con los Datos

### Consultas Conversacionales

En lugar de filtros y reportes, el usuario habla con ODI:

```
Usuario: "ODI, muéstrame las inconsistencias en Yokomar"

ODI: "En el catálogo de Yokomar encontré:
      • 621 productos sin precio asignado
      • 47 SKUs duplicados con descripciones diferentes  
      • 12 imágenes que no coinciden con el producto
      
      ¿Quieres que te muestre los detalles o los corrijo automáticamente?"

Usuario: "Corrige los duplicados y muéstrame los que no tienen precio"

ODI: "Listo. Unifiqué los 47 duplicados (mantuve la descripción más completa).
      Te paso la lista de 621 productos sin precio. 
      ¿Tienes una lista de precios actualizada que pueda procesar?"
```

### Entrenamiento Sin Código

```
Usuario: [Sube un PDF nuevo con formato diferente]

ODI: "Este catálogo tiene una estructura que no había visto.
      ¿Me ayudas a entenderlo?"
      
      [Muestra preview del PDF]
      
      "¿Qué columna es el código del producto?"
      
Usuario: [Señala columna "REF"]

ODI: "Entendido. ¿Y el precio?"

Usuario: [Señala columna "P. LISTA"]

ODI: "Perfecto. Ahora reconoceré este formato automáticamente.
      ¿Este catálogo es de una empresa nueva o existente?"

Usuario: "Nueva, se llama Industrias Leo"

ODI: "Creé el perfil de Industrias Leo. Procesando 847 productos...
      Listo. ¿Los subo a la tienda Leo en Shopify?"
```

---

## 7. Implementación Técnica

### Servicios Docker para Ingesta Cognitiva

```yaml
# docker-compose.ingesta.yml
version: '3.8'

services:
  odi-percepcion:
    image: odi/percepcion:latest
    volumes:
      - /opt/odi/ingesta/boca:/input
      - /opt/odi/ingesta/cognitivo/percepcion:/output
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - VISION_MODEL=gpt-4-vision-preview
    
  odi-comprension:
    image: odi/comprension:latest
    volumes:
      - /opt/odi/ingesta/cognitivo:/data
    environment:
      - CHROMA_HOST=chromadb
      - EMBEDDING_MODEL=text-embedding-3-large
    
  odi-organizador:
    image: odi/organizador:latest
    volumes:
      - /opt/odi/ingesta:/ingesta
    depends_on:
      - odi-percepcion
      - odi-comprension
    
  odi-enriquecedor:
    image: odi/enriquecedor:latest
    volumes:
      - /opt/odi/ingesta/organizacion:/input
      - /opt/odi/ingesta/enriquecimiento:/output
    environment:
      - FITMENT_ENGINE_URL=http://fitment:5000
      
  odi-dialogo:
    image: odi/dialogo:latest
    ports:
      - "8080:8080"
    environment:
      - ELEVENLABS_API_KEY=${ELEVENLABS_API_KEY}
      - WHATSAPP_TOKEN=${WHATSAPP_TOKEN}
```

### API de Ingesta

```python
# /opt/odi/api/ingesta.py
from fastapi import FastAPI, UploadFile, BackgroundTasks
from odi.cognitivo import Percepcion, Comprension, Organizador

app = FastAPI(title="ODI Ingesta Cognitiva")

@app.post("/mostrar")
async def mostrar_a_odi(
    archivo: UploadFile,
    background_tasks: BackgroundTasks
):
    """
    El usuario "muestra" un archivo a ODI.
    ODI lo procesa en background y notifica cuando termine
    o cuando necesite ayuda humana.
    """
    # Guardar en boca de ingesta
    path = await guardar_en_boca(archivo)
    
    # Procesar en background (invisible para el usuario)
    background_tasks.add_task(procesar_cognitivamente, path)
    
    return {
        "estado": "comprendiendo",
        "mensaje": f"Observando {archivo.filename}...",
        "webhook": "/estado/{proceso_id}"
    }

@app.post("/mostrar-url")
async def mostrar_url_a_odi(url: str, background_tasks: BackgroundTasks):
    """
    El usuario pasa un enlace y ODI lo procesa.
    """
    background_tasks.add_task(procesar_url, url)
    
    return {
        "estado": "explorando",
        "mensaje": f"Visitando {url}..."
    }
```

---

## 8. Métricas de Consciencia ODI

```yaml
# /opt/odi/consciencia/pulso/estado.yml
organismo:
  estado: "activo"
  procesando:
    - empresa: "Yokomar"
      etapa: "enriquecimiento"
      progreso: 78%
    - empresa: "Vitton"  
      etapa: "completado"
      productos: 1264
      
  aprendizajes_hoy: 3
  excepciones_pendientes: 2
  
  salud:
    cpu: 34%
    memoria: 2.1GB
    almacenamiento: 47GB/100GB
    
  capacidades:
    empresas_conocidas: 13
    formatos_reconocidos: 8
    productos_procesados: 4,500+
    fitments_calculados: 12,000+
```

---

## 9. Próximos Pasos

1. **Crear estructura de directorios** en servidor
2. **Implementar servicio de Percepción** (detector de tipo de archivo)
3. **Conectar con pipeline actual** (vision_to_shopify.py)
4. **Crear API de ingesta** para interfaz SRM Intelligent
5. **Implementar cola de excepciones** para Human-in-the-loop
6. **Diseñar estados de consciencia** en UI

---

*"ODI no carga datos. ODI comprende catálogos."*
