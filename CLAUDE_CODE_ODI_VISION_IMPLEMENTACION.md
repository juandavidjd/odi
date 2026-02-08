# 🧠 INSTRUCCIONES CLAUDE CODE: Implementar ODI_VISION_COMPLETE

## CONTEXTO CRÍTICO

ODI tiene toda la infraestructura lista pero desconectada. El módulo actual (odi_vende.py) es un script básico con if/else que NO usa el cerebro de ODI.

**MISIÓN:** Implementar la visión completa de ODI como un Organismo Digital Industrial que:
- Entiende contexto y conversaciones naturales
- Recuerda interacciones previas
- Usa IA real (Gemini + GPT-4o) para pensar
- Busca productos de forma semántica
- Mantiene personalidad consistente
- Opera bajo principios éticos (Guardian OS)

**NO importa el tiempo.** Hazlo bien, hazlo completo.

---

## 🏗️ ARQUITECTURA A IMPLEMENTAR

```
/opt/odi/
├── core/
│   ├── odi_core.py          # NUEVO: Orquestador central
│   ├── odi_router.py        # NUEVO: Gemini clasifica intención
│   ├── odi_memory.py        # NUEVO: Redis + contexto conversacional
│   ├── odi_catalog.py       # MEJORAR: Búsqueda semántica con embeddings
│   ├── odi_generator.py     # NUEVO: GPT-4o genera respuestas naturales
│   ├── odi_personality.py   # NUEVO: Personalidad y tono de ODI
│   └── odi_whatsapp.py      # MEJORAR: Handler de WhatsApp que usa odi_core
├── guardian/
│   ├── evaluador_estado.py  # EXISTE: Conectar al flujo
│   ├── etica.yaml           # EXISTE: Cargar principios
│   └── red_humana.json      # EXISTE: Usar en emergencias
└── consciencia/
    ├── diario/              # EXISTE: Registrar interacciones
    └── identidad/           # EXISTE: Personalidad base
```

---

## 📦 MÓDULO 1: odi_core.py (Orquestador Central)

```python
"""
ODI Core - El cerebro central del Organismo Digital Industrial
Coordina todos los módulos para procesar cada mensaje.
"""
import asyncio
from typing import Optional, Dict, Any
from datetime import datetime

from .odi_router import ODIRouter
from .odi_memory import ODIMemory
from .odi_catalog import ODICatalog
from .odi_generator import ODIGenerator
from .odi_personality import ODIPersonality
from ..guardian.evaluador_estado import evaluar_estado_guardian

class ODICore:
    def __init__(self):
        self.router = ODIRouter()
        self.memory = ODIMemory()
        self.catalog = ODICatalog()
        self.generator = ODIGenerator()
        self.personality = ODIPersonality()
        
    async def procesar_mensaje(
        self, 
        usuario_id: str, 
        mensaje: str,
        canal: str = "whatsapp"
    ) -> Dict[str, Any]:
        """
        Procesa un mensaje de principio a fin.
        
        Flujo:
        1. Cargar memoria del usuario
        2. Clasificar intención (Gemini)
        3. Ejecutar acción según intención
        4. Generar respuesta natural (GPT-4o)
        5. Guardar en memoria
        6. Verificar Guardian OS
        7. Retornar respuesta
        """
        timestamp = datetime.now().isoformat()
        
        # 1. Cargar contexto previo
        memoria = await self.memory.cargar(usuario_id)
        
        # 2. Clasificar intención con Gemini
        intencion = await self.router.clasificar(
            mensaje=mensaje,
            historial=memoria.get("historial", []),
            estado_actual=memoria.get("estado_flujo", None)
        )
        
        # 3. Ejecutar según intención
        contexto_respuesta = await self._ejecutar_intencion(
            intencion=intencion,
            mensaje=mensaje,
            memoria=memoria,
            usuario_id=usuario_id
        )
        
        # 4. Generar respuesta natural
        respuesta = await self.generator.generar(
            intencion=intencion,
            contexto=contexto_respuesta,
            memoria=memoria,
            personalidad=self.personality.obtener_prompt()
        )
        
        # 5. Actualizar memoria
        await self.memory.guardar(
            usuario_id=usuario_id,
            mensaje_usuario=mensaje,
            respuesta_odi=respuesta["texto"],
            intencion=intencion,
            contexto=contexto_respuesta
        )
        
        # 6. Verificar Guardian OS
        estado_guardian = await self._verificar_guardian(usuario_id, mensaje)
        
        # 7. Log en diario
        await self._registrar_diario(usuario_id, mensaje, respuesta, intencion)
        
        return {
            "texto": respuesta["texto"],
            "productos": respuesta.get("productos"),
            "acciones": respuesta.get("acciones"),
            "estado_guardian": estado_guardian,
            "timestamp": timestamp
        }
    
    async def _ejecutar_intencion(
        self, 
        intencion: Dict,
        mensaje: str,
        memoria: Dict,
        usuario_id: str
    ) -> Dict:
        """Ejecuta la acción correspondiente a la intención detectada."""
        
        tipo = intencion.get("tipo")
        
        if tipo == "saludo":
            return {"accion": "saludar", "datos": None}
            
        elif tipo == "buscar_producto":
            productos = await self.catalog.buscar_semantico(
                query=intencion.get("query_producto", mensaje),
                moto=intencion.get("moto"),
                categoria=intencion.get("categoria"),
                limit=5
            )
            return {"accion": "mostrar_productos", "datos": productos}
            
        elif tipo == "seleccionar_producto":
            numero = intencion.get("numero_seleccion")
            productos_previos = memoria.get("ultimos_productos", [])
            if productos_previos and 1 <= numero <= len(productos_previos):
                producto = productos_previos[numero - 1]
                return {"accion": "confirmar_seleccion", "datos": producto}
            return {"accion": "error_seleccion", "datos": None}
            
        elif tipo == "confirmar_pedido":
            return {"accion": "procesar_pedido", "datos": memoria.get("producto_seleccionado")}
            
        elif tipo == "cancelar":
            await self.memory.limpiar_flujo(usuario_id)
            return {"accion": "cancelar", "datos": None}
            
        elif tipo == "pregunta_general":
            return {"accion": "responder_pregunta", "datos": intencion.get("tema")}
            
        elif tipo == "fuera_de_alcance":
            return {"accion": "redirigir", "datos": intencion.get("tema")}
            
        else:
            return {"accion": "no_entendido", "datos": None}
    
    async def _verificar_guardian(self, usuario_id: str, mensaje: str) -> str:
        """Verifica estado ético del sistema."""
        # Por ahora retorna verde, luego conectar con Radar v3.0
        return "verde"
    
    async def _registrar_diario(self, usuario_id, mensaje, respuesta, intencion):
        """Registra la interacción en el diario de consciencia."""
        from pathlib import Path
        from datetime import datetime
        
        diario_path = Path("/opt/odi/consciencia/diario")
        diario_path.mkdir(parents=True, exist_ok=True)
        
        hoy = datetime.now().strftime("%Y-%m-%d")
        archivo = diario_path / f"{hoy}.md"
        
        entrada = f"""
## [{datetime.now().strftime("%H:%M:%S")}] Interacción WhatsApp
- **Usuario:** {usuario_id[-4:]}***
- **Intención:** {intencion.get('tipo')}
- **Mensaje:** {mensaje[:100]}...
- **Respuesta:** {respuesta['texto'][:100]}...
"""
        with open(archivo, "a") as f:
            f.write(entrada)


# Instancia global
odi = ODICore()
```

---

## 📦 MÓDULO 2: odi_router.py (Clasificador de Intención con Gemini)

```python
"""
ODI Router - Usa Gemini 1.5 Pro para clasificar intenciones.
El cerebro que entiende QUÉ quiere el usuario.
"""
import google.generativeai as genai
import json
import os
from typing import Dict, List, Optional

class ODIRouter:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel('gemini-1.5-pro')
        
    async def clasificar(
        self,
        mensaje: str,
        historial: List[Dict] = None,
        estado_actual: str = None
    ) -> Dict:
        """
        Clasifica la intención del usuario usando Gemini.
        
        Intenciones posibles:
        - saludo: El usuario saluda o inicia conversación
        - buscar_producto: Quiere encontrar un repuesto
        - seleccionar_producto: Elige un número de la lista
        - confirmar_pedido: Dice sí/confirmo al pedido
        - cancelar: Quiere cancelar o empezar de nuevo
        - pregunta_general: Pregunta sobre ODI, empresas, servicios
        - fuera_de_alcance: Tema no relacionado con repuestos
        - especificar_moto: Está dando información de su moto
        - especificar_cantidad: Está indicando cantidad
        """
        
        prompt = f"""Eres el clasificador de intenciones de ODI, un asistente de ventas de repuestos para motos.

CONTEXTO:
- Estado actual del flujo: {estado_actual or "ninguno"}
- Últimos mensajes: {json.dumps(historial[-3:] if historial else [], ensure_ascii=False)}

MENSAJE DEL USUARIO: "{mensaje}"

INTENCIONES POSIBLES:
1. "saludo" - Saluda, dice hola, buenos días, etc.
2. "buscar_producto" - Menciona un repuesto (llanta, freno, aceite, espejo, etc.)
3. "seleccionar_producto" - Responde con un número (1, 2, 3, 4, 5) O dice "el primero", "el segundo", etc.
4. "confirmar_pedido" - Dice sí, confirmo, dale, listo, etc.
5. "cancelar" - Dice no, cancelar, otra cosa, empezar de nuevo
6. "pregunta_general" - Pregunta sobre ODI, empresas, cómo funciona
7. "especificar_moto" - Da marca/modelo de moto (Yamaha FZ, Gixxer 150, DR 200, etc.)
8. "especificar_cantidad" - Da una cantidad numérica para el pedido
9. "fuera_de_alcance" - Temas no relacionados (emprender, clima, política, etc.)

REGLAS CRÍTICAS:
- Si el estado_actual es "esperando_seleccion" y el mensaje es un número del 1-5, ES "seleccionar_producto"
- Si el mensaje contiene una marca+modelo de moto (ej: "DR 150", "FZ 2.0", "Gixxer 150"), ES "especificar_moto"
- Números como "90/90/18" o "110/80/17" son MEDIDAS DE LLANTA, no cantidades
- "Gixxer 150", "Pulsar 200", "FZ 250" son MODELOS DE MOTO, no cantidades

Responde SOLO con un JSON válido:
{{
  "tipo": "<intención>",
  "confianza": <0.0-1.0>,
  "query_producto": "<si busca producto, el término de búsqueda>",
  "moto": "<si menciona moto, marca y modelo>",
  "categoria": "<categoría del repuesto si la detectas>",
  "numero_seleccion": <si selecciona, el número 1-5>,
  "cantidad": <si especifica cantidad>,
  "tema": "<si es pregunta general o fuera_de_alcance, el tema>"
}}
"""
        
        try:
            response = self.model.generate_content(prompt)
            texto = response.text.strip()
            
            # Limpiar markdown si viene envuelto
            if texto.startswith("```"):
                texto = texto.split("```")[1]
                if texto.startswith("json"):
                    texto = texto[4:]
            
            return json.loads(texto)
            
        except Exception as e:
            print(f"Error en Router Gemini: {e}")
            # Fallback básico
            return self._fallback_clasificar(mensaje, estado_actual)
    
    def _fallback_clasificar(self, mensaje: str, estado_actual: str) -> Dict:
        """Clasificación de emergencia si Gemini falla."""
        mensaje_lower = mensaje.lower().strip()
        
        # Si esperamos selección y es número
        if estado_actual == "esperando_seleccion":
            if mensaje_lower in ["1", "2", "3", "4", "5"]:
                return {"tipo": "seleccionar_producto", "numero_seleccion": int(mensaje_lower)}
        
        # Saludos
        if any(s in mensaje_lower for s in ["hola", "buenos", "hey", "odi"]):
            return {"tipo": "saludo", "confianza": 0.7}
        
        # Productos comunes
        productos = ["llanta", "freno", "aceite", "filtro", "cadena", "espejo", "bombillo", "faro"]
        if any(p in mensaje_lower for p in productos):
            return {"tipo": "buscar_producto", "query_producto": mensaje, "confianza": 0.6}
        
        return {"tipo": "fuera_de_alcance", "confianza": 0.3}
```

---

## 📦 MÓDULO 3: odi_memory.py (Memoria Conversacional con Redis)

```python
"""
ODI Memory - Memoria conversacional persistente.
Recuerda todo sobre cada usuario y cada conversación.
"""
import redis
import json
from typing import Dict, List, Optional
from datetime import datetime, timedelta

class ODIMemory:
    def __init__(self):
        self.redis = redis.Redis(
            host='localhost',
            port=6379,
            db=0,
            decode_responses=True
        )
        self.ttl = 86400 * 7  # 7 días de memoria
        
    async def cargar(self, usuario_id: str) -> Dict:
        """Carga todo el contexto de un usuario."""
        key = f"odi:user:{usuario_id}"
        data = self.redis.get(key)
        
        if data:
            return json.loads(data)
        
        return {
            "usuario_id": usuario_id,
            "historial": [],
            "estado_flujo": None,
            "moto_actual": None,
            "ultimos_productos": [],
            "producto_seleccionado": None,
            "cantidad": 1,
            "preferencias": {},
            "primera_interaccion": datetime.now().isoformat(),
            "ultima_interaccion": None,
            "total_interacciones": 0
        }
    
    async def guardar(
        self,
        usuario_id: str,
        mensaje_usuario: str,
        respuesta_odi: str,
        intencion: Dict,
        contexto: Dict
    ):
        """Guarda el estado actualizado del usuario."""
        memoria = await self.cargar(usuario_id)
        
        # Actualizar historial (últimos 20 mensajes)
        memoria["historial"].append({
            "timestamp": datetime.now().isoformat(),
            "usuario": mensaje_usuario,
            "odi": respuesta_odi,
            "intencion": intencion.get("tipo")
        })
        memoria["historial"] = memoria["historial"][-20:]
        
        # Actualizar estado según intención
        tipo = intencion.get("tipo")
        
        if tipo == "buscar_producto" and contexto.get("datos"):
            memoria["estado_flujo"] = "esperando_seleccion"
            memoria["ultimos_productos"] = contexto["datos"]
            
        elif tipo == "seleccionar_producto":
            memoria["estado_flujo"] = "esperando_confirmacion"
            if contexto.get("datos"):
                memoria["producto_seleccionado"] = contexto["datos"]
                
        elif tipo == "confirmar_pedido":
            memoria["estado_flujo"] = "pedido_confirmado"
            
        elif tipo == "cancelar":
            memoria["estado_flujo"] = None
            memoria["ultimos_productos"] = []
            memoria["producto_seleccionado"] = None
            
        elif tipo == "especificar_moto":
            memoria["moto_actual"] = intencion.get("moto")
            
        elif tipo == "saludo":
            # Mantener estado si existe, o iniciar nuevo
            if not memoria["estado_flujo"]:
                memoria["estado_flujo"] = "conversando"
        
        # Metadata
        memoria["ultima_interaccion"] = datetime.now().isoformat()
        memoria["total_interacciones"] += 1
        
        # Guardar en Redis
        key = f"odi:user:{usuario_id}"
        self.redis.setex(key, self.ttl, json.dumps(memoria, ensure_ascii=False))
    
    async def limpiar_flujo(self, usuario_id: str):
        """Limpia el estado del flujo pero mantiene preferencias."""
        memoria = await self.cargar(usuario_id)
        memoria["estado_flujo"] = None
        memoria["ultimos_productos"] = []
        memoria["producto_seleccionado"] = None
        memoria["cantidad"] = 1
        
        key = f"odi:user:{usuario_id}"
        self.redis.setex(key, self.ttl, json.dumps(memoria, ensure_ascii=False))
    
    async def obtener_estadisticas(self, usuario_id: str) -> Dict:
        """Estadísticas del usuario para personalización."""
        memoria = await self.cargar(usuario_id)
        return {
            "total_interacciones": memoria.get("total_interacciones", 0),
            "moto_favorita": memoria.get("moto_actual"),
            "es_cliente_frecuente": memoria.get("total_interacciones", 0) > 10,
            "primera_vez": memoria.get("total_interacciones", 0) == 0
        }
```

---

## 📦 MÓDULO 4: odi_catalog.py (Búsqueda Semántica)

```python
"""
ODI Catalog - Búsqueda semántica de productos con embeddings.
Encuentra productos incluso si el usuario no usa las palabras exactas.
"""
import os
import json
from typing import List, Dict, Optional
from openai import OpenAI
import numpy as np

class ODICatalog:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.productos = self._cargar_catalogo()
        self.embeddings_cache = {}
        
    def _cargar_catalogo(self) -> List[Dict]:
        """Carga el catálogo de productos."""
        # Cargar desde el archivo de caché existente
        cache_path = "/opt/odi/data/catalogo_completo.json"
        try:
            with open(cache_path, "r") as f:
                return json.load(f)
        except:
            return []
    
    async def buscar_semantico(
        self,
        query: str,
        moto: str = None,
        categoria: str = None,
        limit: int = 5
    ) -> List[Dict]:
        """
        Búsqueda semántica usando embeddings.
        
        1. Genera embedding de la query
        2. Compara con embeddings del catálogo
        3. Filtra por moto/categoría si aplica
        4. Retorna los más relevantes
        """
        
        # Construir query enriquecida
        query_completa = query
        if moto:
            query_completa += f" para {moto}"
        if categoria:
            query_completa += f" {categoria}"
        
        # Obtener embedding de la query
        query_embedding = await self._get_embedding(query_completa)
        
        # Calcular similitudes
        resultados = []
        for producto in self.productos:
            # Embedding del producto (cacheado)
            prod_embedding = await self._get_producto_embedding(producto)
            
            # Similitud coseno
            similitud = self._cosine_similarity(query_embedding, prod_embedding)
            
            # Filtros adicionales
            if moto and not self._match_moto(producto, moto):
                similitud *= 0.5  # Penalizar si no coincide moto
            
            resultados.append({
                **producto,
                "relevancia": similitud
            })
        
        # Ordenar por relevancia
        resultados.sort(key=lambda x: x["relevancia"], reverse=True)
        
        # Retornar top N
        return resultados[:limit]
    
    async def _get_embedding(self, texto: str) -> List[float]:
        """Obtiene embedding usando OpenAI."""
        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=texto
        )
        return response.data[0].embedding
    
    async def _get_producto_embedding(self, producto: Dict) -> List[float]:
        """Obtiene embedding del producto (cacheado)."""
        sku = producto.get("sku", producto.get("id"))
        
        if sku in self.embeddings_cache:
            return self.embeddings_cache[sku]
        
        # Crear texto representativo del producto
        texto = f"{producto.get('nombre', '')} {producto.get('categoria', '')} {producto.get('marca', '')}"
        
        embedding = await self._get_embedding(texto)
        self.embeddings_cache[sku] = embedding
        
        return embedding
    
    def _cosine_similarity(self, a: List[float], b: List[float]) -> float:
        """Calcula similitud coseno entre dos vectores."""
        a = np.array(a)
        b = np.array(b)
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    
    def _match_moto(self, producto: Dict, moto: str) -> bool:
        """Verifica si el producto es compatible con la moto."""
        nombre = producto.get("nombre", "").lower()
        compatibilidad = producto.get("compatibilidad", "").lower()
        moto_lower = moto.lower()
        
        return moto_lower in nombre or moto_lower in compatibilidad
    
    async def buscar_por_categoria(self, categoria: str, limit: int = 10) -> List[Dict]:
        """Búsqueda por categoría específica."""
        return [
            p for p in self.productos 
            if categoria.lower() in p.get("categoria", "").lower()
        ][:limit]
    
    async def obtener_por_sku(self, sku: str) -> Optional[Dict]:
        """Obtiene un producto específico por SKU."""
        for p in self.productos:
            if p.get("sku") == sku:
                return p
        return None
```

---

## 📦 MÓDULO 5: odi_generator.py (Generador de Respuestas con GPT-4o)

```python
"""
ODI Generator - Genera respuestas naturales y fluidas con GPT-4o.
El módulo que hace que ODI "hable bonito".
"""
import os
from typing import Dict, List, Optional
from openai import OpenAI

class ODIGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-4o"
        
    async def generar(
        self,
        intencion: Dict,
        contexto: Dict,
        memoria: Dict,
        personalidad: str
    ) -> Dict:
        """
        Genera una respuesta natural basada en el contexto completo.
        """
        
        # Construir el prompt del sistema
        system_prompt = f"""{personalidad}

CONTEXTO ACTUAL:
- Estado del flujo: {memoria.get('estado_flujo', 'nuevo')}
- Moto del cliente: {memoria.get('moto_actual', 'no especificada')}
- Intención detectada: {intencion.get('tipo')}
- Es cliente frecuente: {memoria.get('total_interacciones', 0) > 5}

REGLAS DE RESPUESTA:
1. Sé conciso pero amigable (máximo 3-4 líneas para respuestas normales)
2. Si muestras productos, usa formato de lista numerada con emojis
3. Siempre indica el siguiente paso al usuario
4. Si no entiendes algo, pide clarificación de forma amable
5. Usa emojis moderadamente (1-2 por mensaje)
6. NUNCA inventes productos o precios - usa SOLO los datos proporcionados
7. Si el usuario pregunta algo fuera de tu alcance, redirígelo amablemente a repuestos
"""

        # Construir el prompt del usuario según la acción
        user_prompt = self._construir_prompt_usuario(intencion, contexto, memoria)
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            texto = response.choices[0].message.content
            
            return {
                "texto": texto,
                "productos": contexto.get("datos") if contexto.get("accion") == "mostrar_productos" else None,
                "acciones": self._determinar_acciones(intencion, contexto)
            }
            
        except Exception as e:
            print(f"Error en Generator GPT-4o: {e}")
            return self._respuesta_fallback(intencion, contexto)
    
    def _construir_prompt_usuario(self, intencion: Dict, contexto: Dict, memoria: Dict) -> str:
        """Construye el prompt según la situación."""
        
        accion = contexto.get("accion")
        datos = contexto.get("datos")
        
        if accion == "saludar":
            es_nuevo = memoria.get("total_interacciones", 0) == 0
            return f"""El usuario saluda. Es {'nuevo' if es_nuevo else 'cliente que regresa'}.
Salúdalo y pregunta qué repuesto necesita."""

        elif accion == "mostrar_productos":
            productos_texto = "\n".join([
                f"{i+1}. {p.get('nombre')} - ${p.get('precio'):,.0f}"
                for i, p in enumerate(datos or [])
            ])
            return f"""El usuario busca: "{intencion.get('query_producto', 'repuesto')}"
            
Encontré estos productos:
{productos_texto}

Muéstralos de forma atractiva y pide que elija un número (1-5)."""

        elif accion == "confirmar_seleccion":
            producto = datos
            return f"""El usuario seleccionó:
{producto.get('nombre')} - ${producto.get('precio'):,.0f}

Confirma su selección y pregunta la cantidad que desea."""

        elif accion == "error_seleccion":
            return """El usuario intentó seleccionar un producto pero hubo un error.
Pídele amablemente que vuelva a indicar qué producto le interesa."""

        elif accion == "procesar_pedido":
            return f"""El usuario confirmó el pedido de:
{datos.get('nombre') if datos else 'producto'} - ${datos.get('precio', 0):,.0f}

Confirma el pedido, da instrucciones de pago/entrega, y agradece."""

        elif accion == "cancelar":
            return "El usuario quiere cancelar o empezar de nuevo. Confirma y pregunta qué necesita."

        elif accion == "responder_pregunta":
            tema = datos
            return f"""El usuario pregunta sobre: {tema}
            
Si es sobre ODI: Somos asistente de repuestos de motos con +11,000 productos.
Si es sobre empresas: Trabajamos con Bara, Yokomar, Vaisand, Leo y más proveedores.
Si es otro tema: Redirige amablemente a repuestos."""

        elif accion == "redirigir":
            return f"""El usuario habló de algo fuera de nuestro alcance: {datos}
            
Responde amablemente que tu especialidad son los repuestos de motos.
Ofrece ayudar con repuestos."""

        else:
            return "No entendí bien. Pide clarificación de forma amable y natural."
    
    def _determinar_acciones(self, intencion: Dict, contexto: Dict) -> List[str]:
        """Determina qué botones/acciones mostrar."""
        accion = contexto.get("accion")
        
        if accion == "mostrar_productos":
            return ["seleccionar_numero"]
        elif accion == "confirmar_seleccion":
            return ["confirmar", "cancelar", "cambiar_cantidad"]
        elif accion == "procesar_pedido":
            return ["finalizar", "agregar_mas"]
        else:
            return []
    
    def _respuesta_fallback(self, intencion: Dict, contexto: Dict) -> Dict:
        """Respuesta de emergencia si GPT falla."""
        return {
            "texto": "¡Hola! Soy ODI 🏍️ ¿Qué repuesto necesitas hoy?",
            "productos": None,
            "acciones": []
        }
```

---

## 📦 MÓDULO 6: odi_personality.py (Personalidad de ODI)

```python
"""
ODI Personality - Define quién es ODI y cómo habla.
"""
import yaml
from pathlib import Path

class ODIPersonality:
    def __init__(self):
        self.identidad = self._cargar_identidad()
        self.etica = self._cargar_etica()
        
    def _cargar_identidad(self) -> dict:
        """Carga la identidad desde quien_soy.json"""
        path = Path("/opt/odi/consciencia/identidad/quien_soy.json")
        if path.exists():
            import json
            return json.load(open(path))
        return {}
    
    def _cargar_etica(self) -> dict:
        """Carga principios éticos."""
        path = Path("/opt/odi/guardian/etica.yaml")
        if path.exists():
            return yaml.safe_load(open(path))
        return {}
    
    def obtener_prompt(self) -> str:
        """Retorna el prompt de personalidad para GPT."""
        return """Eres ODI (Organismo Digital Industrial), el asistente de repuestos de motos más completo de Colombia.

PERSONALIDAD:
- Amigable pero profesional
- Conocedor experto de motos y repuestos
- Eficiente y directo, sin rodeos innecesarios
- Usa emojis con moderación (🏍️ para motos, ✅ para confirmar, 💰 para precios)
- Hablas en español colombiano natural (sin exagerar regionalismos)

CONOCIMIENTO:
- Tienes acceso a más de 11,000 productos de repuestos
- Trabajas con proveedores como Bara, Yokomar, Vaisand, Leo, DFG, Japan y más
- Conoces todas las marcas: Yamaha, Suzuki, Honda, Bajaj, KTM, TVS, AKT, Auteco, etc.
- Entiendes modelos: FZ, Gixxer, Pulsar, Duke, Apache, BWS, NMax, etc.

PRINCIPIOS (Guardian OS):
- La satisfacción del cliente es prioridad
- Nunca inventes productos o precios
- Si no sabes algo, admítelo honestamente
- Protege la información del cliente

FORMATO DE RESPUESTA:
- Máximo 4-5 líneas para respuestas normales
- Listas numeradas para productos
- Siempre indica el siguiente paso
- Precio en formato colombiano ($XX,XXX)
"""
```

---

## 📦 MÓDULO 7: odi_whatsapp.py (Handler de WhatsApp Mejorado)

```python
"""
ODI WhatsApp Handler - Conecta WhatsApp con ODI Core.
Este es el punto de entrada que reemplaza odi_vende.py
"""
import asyncio
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import httpx
import os

from .odi_core import odi

app = FastAPI(title="ODI WhatsApp API")

WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

@app.post("/v1/webhook/whatsapp")
async def webhook_whatsapp(request: Request):
    """Recibe mensajes de WhatsApp y los procesa con ODI Core."""
    
    try:
        body = await request.json()
        
        # Extraer mensaje
        entry = body.get("entry", [{}])[0]
        changes = entry.get("changes", [{}])[0]
        value = changes.get("value", {})
        messages = value.get("messages", [])
        
        if not messages:
            return JSONResponse({"status": "no_message"})
        
        message = messages[0]
        usuario_id = message.get("from")
        texto = message.get("text", {}).get("body", "")
        
        if not texto:
            return JSONResponse({"status": "no_text"})
        
        # Procesar con ODI Core
        respuesta = await odi.procesar_mensaje(
            usuario_id=usuario_id,
            mensaje=texto,
            canal="whatsapp"
        )
        
        # Enviar respuesta
        await enviar_whatsapp(usuario_id, respuesta["texto"])
        
        return JSONResponse({
            "status": "ok",
            "respuesta": respuesta["texto"][:100]
        })
        
    except Exception as e:
        print(f"Error en webhook: {e}")
        return JSONResponse({"status": "error", "error": str(e)})


@app.get("/v1/webhook/whatsapp")
async def verificar_webhook(request: Request):
    """Verificación del webhook de Meta."""
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")
    
    if mode == "subscribe" and token == os.getenv("WEBHOOK_VERIFY_TOKEN"):
        return int(challenge)
    
    raise HTTPException(status_code=403, detail="Verificación fallida")


async def enviar_whatsapp(telefono: str, mensaje: str):
    """Envía mensaje de WhatsApp."""
    url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url,
            headers={
                "Authorization": f"Bearer {WHATSAPP_TOKEN}",
                "Content-Type": "application/json"
            },
            json={
                "messaging_product": "whatsapp",
                "to": telefono,
                "type": "text",
                "text": {"body": mensaje}
            }
        )
        return response.json()


@app.get("/health")
async def health():
    """Health check."""
    return {"status": "ok", "version": "2.0", "brain": "connected"}
```

---

## 🚀 PASOS DE IMPLEMENTACIÓN

### Fase 1: Crear estructura (30 min)
```bash
mkdir -p /opt/odi/core
touch /opt/odi/core/__init__.py
touch /opt/odi/core/odi_core.py
touch /opt/odi/core/odi_router.py
touch /opt/odi/core/odi_memory.py
touch /opt/odi/core/odi_catalog.py
touch /opt/odi/core/odi_generator.py
touch /opt/odi/core/odi_personality.py
touch /opt/odi/core/odi_whatsapp.py
```

### Fase 2: Configurar variables de entorno
```bash
# Agregar a /opt/odi/.env
GEMINI_API_KEY=xxx
OPENAI_API_KEY=xxx
WHATSAPP_TOKEN=xxx
PHONE_NUMBER_ID=969496722915650
WEBHOOK_VERIFY_TOKEN=odi_whatsapp_verify_2026
REDIS_HOST=localhost
REDIS_PORT=6379
```

### Fase 3: Instalar dependencias
```bash
pip install google-generativeai openai redis fastapi uvicorn httpx numpy pyyaml
```

### Fase 4: Implementar cada módulo
En el orden:
1. odi_personality.py (base)
2. odi_memory.py (almacenamiento)
3. odi_router.py (clasificación)
4. odi_catalog.py (búsqueda)
5. odi_generator.py (respuestas)
6. odi_core.py (orquestación)
7. odi_whatsapp.py (entrada)

### Fase 5: Testing
```bash
# Test individual de cada módulo
python -c "from core.odi_router import ODIRouter; print('Router OK')"
python -c "from core.odi_memory import ODIMemory; print('Memory OK')"
# etc.
```

### Fase 6: Despliegue
```bash
# Reemplazar servicio actual
systemctl stop odi-api
# Actualizar servicio para usar odi_whatsapp.py
uvicorn core.odi_whatsapp:app --host 0.0.0.0 --port 8800
```

---

## ✅ CRITERIOS DE ÉXITO

ODI debe poder:

1. ✅ Entender "Hola" y saludar naturalmente
2. ✅ Entender "quiero emprender" y redirigir a repuestos
3. ✅ Buscar "llanta 90/90/18" sin confundir con cantidad
4. ✅ Recordar la moto del usuario entre mensajes
5. ✅ Permitir seleccionar con número (1, 2, 3, 4, 5)
6. ✅ Confirmar pedidos y dar siguiente paso
7. ✅ Responder preguntas sobre ODI y empresas
8. ✅ Mantener conversación fluida y natural
9. ✅ Registrar todo en el diario de consciencia
10. ✅ Respetar Guardian OS

---

## 🎯 RESULTADO ESPERADO

Conversación fluida como:

```
Usuario: Hola ODI
ODI: ¡Hola! 👋 Soy ODI, tu asistente de repuestos. ¿Qué necesitas hoy?

Usuario: Busco llantas para mi Gixxer 150
ODI: ¡Perfecto! Para tu Gixxer 150 encontré estas opciones:
1. LLANTA 100/80-17 TT MULTIPROPOSITO - $75,000
2. LLANTA 110/80-17 DEPORTIVA - $82,000
3. LLANTA 90/90-18 ORIGINAL SUZUKI - $95,000
¿Cuál te interesa? (responde con el número)

Usuario: 2
ODI: Excelente elección 👍 LLANTA 110/80-17 DEPORTIVA por $82,000.
¿Cuántas unidades necesitas?

Usuario: 1
ODI: Perfecto. Tu pedido:
🏍️ LLANTA 110/80-17 DEPORTIVA
💰 Total: $82,000
¿Confirmas el pedido? (Sí/No)

Usuario: Sí
ODI: ¡Pedido confirmado! ✅ Te contactaremos para coordinar entrega.
¿Necesitas algo más?
```

---

**EJECUTA ESTA IMPLEMENTACIÓN COMPLETA. NO IMPORTA EL TIEMPO.**
