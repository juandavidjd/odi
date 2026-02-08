#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
═══════════════════════════════════════════════════════════════════════════════
ODI CATALOG PIPELINE v2.0 — CATÁLOGO UNIFICADO MULTI-EMPRESA
═══════════════════════════════════════════════════════════════════════════════

Pipeline completo para unificar catálogos de las 10 empresas del ecosistema ODI.

ESTRUCTURA DE DATOS DETECTADA (Bara):
- Base_Datos_*.csv: DESCRIPCION, CODIGO, PRECIO
- catalogo_imagenes_*.csv: Salida del script IA (16 columnas)
- shopify_*_final.csv: Ya procesado para Shopify

USO:
    python odi_pipeline_maestro.py
    python odi_pipeline_maestro.py --empresas Bara Kaiqi
    python odi_pipeline_maestro.py --base "E:\Mi_Carpeta" --output "E:\Salida"

REQUISITOS:
    pip install pandas openpyxl tqdm fuzzywuzzy python-Levenshtein

AUTOR: ODI System / ADSI
VERSIÓN: 2.0
═══════════════════════════════════════════════════════════════════════════════
"""

import os
import json
import hashlib
import re
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, List, Tuple
from dataclasses import dataclass, asdict, field

import pandas as pd

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(x, **kw): return x

try:
    from fuzzywuzzy import fuzz
    FUZZY = True
except ImportError:
    FUZZY = False

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN
# ═══════════════════════════════════════════════════════════════════════════════

BASE_FOLDER = r"E:\Profesion\10 empresas ecosistema ODI"
OUTPUT_FOLDER = r"E:\ODI_Catalogo_Output"

EMPRESAS = ["Bara", "DFG", "Duna", "Imbra", "Japan", "Kaiqi", "Leo", "Store", "Vaisand", "Yokomar"]

IMAGE_BASE_URL = "http://64.23.170.118/images"

MARGEN_MINIMO = 0.15
MARGEN_OBJETIVO = 0.35
SIMILARITY_THRESHOLD = 85

COLORES = {
    "Bara": "#FF6B00", "DFG": "#1E3A5F", "Duna": "#4CAF50",
    "Imbra": "#E91E63", "Japan": "#C41E3A", "Kaiqi": "#FF9800",
    "Leo": "#2196F3", "Store": "#9C27B0", "Vaisand": "#00BCD4", "Yokomar": "#795548"
}

# ═══════════════════════════════════════════════════════════════════════════════
# UTILIDADES
# ═══════════════════════════════════════════════════════════════════════════════

def normalize(text: str) -> str:
    if not text or not isinstance(text, str): return ""
    text = text.lower().strip()
    for a, b in [('á','a'),('é','e'),('í','i'),('ó','o'),('ú','u'),('ñ','n')]:
        text = text.replace(a, b)
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9\s]', ' ', text)).strip()

def dedup_hash(nombre: str, sistema: str = "") -> str:
    return hashlib.md5(f"{normalize(nombre)}|{normalize(sistema)}".encode()).hexdigest()[:12]

def gen_sku(empresa: str, codigo: str, idx: int) -> str:
    pre = empresa[:3].upper()
    cod = re.sub(r'[^a-zA-Z0-9]', '', str(codigo))[:10] or f"{idx:05d}"
    return f"{pre}-{cod}"

def parse_price(p) -> float:
    if pd.isna(p) or p == '': return 0.0
    if isinstance(p, (int, float)): return float(p)
    return float(str(p).replace('$','').replace(',','').replace('.','') or 0)

def calc_price(costo: float, margen: float = MARGEN_OBJETIVO) -> Tuple[float, float]:
    if costo <= 0: return 0.0, 0.0
    m = max(margen, MARGEN_MINIMO)
    pv = round(costo / (1 - m) / 100) * 100
    mr = (pv - costo) / pv if pv > 0 else 0
    return pv, mr

# ═══════════════════════════════════════════════════════════════════════════════
# CARGADORES
# ═══════════════════════════════════════════════════════════════════════════════

def load_csv(path: str, patterns: List[str]) -> pd.DataFrame:
    if not os.path.isdir(path): return pd.DataFrame()
    for f in os.listdir(path):
        if any(p.lower() in f.lower() for p in patterns) and f.endswith('.csv'):
            for sep in [';', ',', '\t']:
                try:
                    df = pd.read_csv(os.path.join(path, f), sep=sep, encoding='utf-8-sig')
                    if len(df.columns) > 1: return df
                except: pass
    return pd.DataFrame()

def load_precios(empresa: str, base: str) -> pd.DataFrame:
    return load_csv(os.path.join(base, "Data", empresa), 
                   ['Lista_Precios', 'Base_Datos', 'precios', 'inventario'])

def load_catalogo(empresa: str, base: str) -> pd.DataFrame:
    return load_csv(os.path.join(base, "Data", empresa),
                   ['catalogo_imagenes', 'catalogo_'])

def load_shopify(empresa: str, base: str) -> pd.DataFrame:
    return load_csv(os.path.join(base, "Data", empresa), ['shopify'])

# ═══════════════════════════════════════════════════════════════════════════════
# PIPELINE
# ═══════════════════════════════════════════════════════════════════════════════

class ODIPipeline:
    def __init__(self, base: str = BASE_FOLDER):
        self.base = base
        self.productos = []
        self.duplicados = []
        self.sin_imagen = []
        self.hashes = {}
        self.stats = {"total": 0, "con_img": 0, "dups": 0, "empresas": {}}

    def run(self, empresas: List[str] = None):
        print("\n" + "═"*60)
        print("🚀 ODI CATALOG PIPELINE v2.0")
        print("═"*60)
        
        for emp in (empresas or EMPRESAS):
            self._process(emp)
        
        self._export()
        
        print("\n✅ COMPLETADO:", self.stats["total"], "productos")

    def _process(self, emp: str):
        print(f"\n📦 {emp}")
        
        precios = load_precios(emp, self.base)
        catalogo = load_catalogo(emp, self.base)
        shopify = load_shopify(emp, self.base)
        
        print(f"   Precios: {len(precios)} | Catálogo: {len(catalogo)} | Shopify: {len(shopify)}")
        
        count = 0
        
        # Priorizar Shopify si existe
        if not shopify.empty and 'Title' in shopify.columns:
            for i, r in shopify.iterrows():
                h = dedup_hash(str(r.get('Title','')), str(r.get('Type','')))
                if h in self.hashes:
                    self.stats["dups"] += 1
                    continue
                
                self.productos.append({
                    'empresa': emp,
                    'sku': gen_sku(emp, str(r.get('SKU',i)), len(self.productos)),
                    'nombre': str(r.get('Title','')),
                    'descripcion': str(r.get('Description','')),
                    'precio_costo': parse_price(r.get('Price',0)) * 0.65,
                    'precio_venta': parse_price(r.get('Price',0)),
                    'sistema': str(r.get('Type','')),
                    'tags': str(r.get('Tags','')),
                    'imagen_url': str(r.get('Product image URL','')),
                    'tiene_imagen': bool(r.get('Product image URL')),
                    'hash': h
                })
                self.hashes[h] = True
                count += 1
                self.stats["con_img"] += 1
        
        # Si no hay Shopify, usar precios
        elif not precios.empty:
            precios.columns = [c.upper().strip() for c in precios.columns]
            col_d = next((c for c in precios.columns if 'DESC' in c), None)
            col_c = next((c for c in precios.columns if 'COD' in c), None)
            col_p = next((c for c in precios.columns if 'PREC' in c), None)
            
            if col_d:
                for i, r in precios.iterrows():
                    desc = str(r.get(col_d,''))
                    if not desc or desc == 'nan': continue
                    
                    cod = str(r.get(col_c,i)) if col_c else str(i)
                    costo = parse_price(r.get(col_p,0)) if col_p else 0
                    pv, m = calc_price(costo)
                    
                    h = dedup_hash(desc)
                    if h in self.hashes:
                        self.stats["dups"] += 1
                        continue
                    
                    # Buscar en catálogo de imágenes
                    img_data = self._find_image(cod, desc, catalogo)
                    
                    self.productos.append({
                        'empresa': emp,
                        'sku': gen_sku(emp, cod, len(self.productos)),
                        'nombre': img_data.get('Nombre_Comercial_Catalogo', desc) if img_data else desc,
                        'descripcion': img_data.get('Funcion', desc) if img_data else desc,
                        'precio_costo': costo,
                        'precio_venta': pv,
                        'sistema': img_data.get('Sistema','') if img_data else '',
                        'tags': img_data.get('Tags_Sugeridos','') if img_data else '',
                        'imagen_url': f"{IMAGE_BASE_URL}/{emp.lower()}/{img_data.get('Filename_Original','')}" if img_data else '',
                        'tiene_imagen': bool(img_data),
                        'compatibilidad': img_data.get('Compatibilidad_Probable_Texto','') if img_data else '',
                        'hash': h
                    })
                    self.hashes[h] = True
                    count += 1
                    if img_data:
                        self.stats["con_img"] += 1
                    else:
                        self.sin_imagen.append({'empresa': emp, 'codigo': cod, 'desc': desc})
        
        self.stats["total"] += count
        self.stats["empresas"][emp] = count
        print(f"   ✅ {count} productos")

    def _find_image(self, codigo: str, desc: str, cat: pd.DataFrame):
        if cat.empty: return None
        cod_n = normalize(codigo)
        desc_n = normalize(desc)
        
        for _, r in cat.iterrows():
            fn = normalize(str(r.get('Filename_Original','')))
            if cod_n and cod_n in fn: return r.to_dict()
            if FUZZY and desc_n:
                nc = normalize(str(r.get('Nombre_Comercial_Catalogo','')))
                if fuzz.ratio(desc_n, nc) > SIMILARITY_THRESHOLD: return r.to_dict()
        return None

    def _export(self):
        Path(OUTPUT_FOLDER).mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        print("\n💾 EXPORTANDO...")
        
        if self.productos:
            df = pd.DataFrame(self.productos)
            
            # Master
            df.to_csv(f"{OUTPUT_FOLDER}/catalogo_unificado_{ts}.csv", index=False, encoding='utf-8-sig')
            print(f"   ✅ catalogo_unificado_{ts}.csv")
            
            # Shopify
            shopify = self._to_shopify(df)
            shopify.to_csv(f"{OUTPUT_FOLDER}/shopify_import_{ts}.csv", index=False, encoding='utf-8-sig')
            print(f"   ✅ shopify_import_{ts}.csv")
            
            # M6.2
            m62 = {'products': [{
                'sku': p['sku'], 'title': p['nombre'], 'price': p['precio_venta'],
                'provider': p['empresa'], 'image': p['imagen_url'],
                'tags': p.get('tags','').split(', ')
            } for p in self.productos]}
            with open(f"{OUTPUT_FOLDER}/catalogo_m62_{ts}.json", 'w', encoding='utf-8') as f:
                json.dump(m62, f, ensure_ascii=False, indent=2)
            print(f"   ✅ catalogo_m62_{ts}.json")
        
        if self.sin_imagen:
            pd.DataFrame(self.sin_imagen).to_csv(f"{OUTPUT_FOLDER}/sin_imagen_{ts}.csv", index=False)
            print(f"   📋 sin_imagen_{ts}.csv ({len(self.sin_imagen)})")
        
        print(f"\n📊 RESUMEN: {self.stats['total']} productos, {self.stats['con_img']} con imagen, {self.stats['dups']} duplicados")

    def _to_shopify(self, df: pd.DataFrame) -> pd.DataFrame:
        rows = []
        for _, r in df.iterrows():
            rows.append({
                'Title': r['nombre'],
                'URL handle': r['sku'].lower(),
                'Description': r['descripcion'],
                'Vendor': r['empresa'],
                'Product category': 'Vehicles & Parts > Vehicle Parts & Accessories',
                'Type': r.get('sistema', 'Repuestos'),
                'Tags': r.get('tags', ''),
                'Published on online store': 'TRUE',
                'Status': 'active',
                'SKU': r['sku'],
                'Price': r['precio_venta'] if r['precio_venta'] > 0 else '',
                'Cost per item': r['precio_costo'] if r['precio_costo'] > 0 else '',
                'Inventory quantity': 10,
                'Product image URL': r['imagen_url'],
                'Image alt text': r['nombre'],
            })
        return pd.DataFrame(rows)

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--base", "-b", default=BASE_FOLDER)
    p.add_argument("--output", "-o", default=OUTPUT_FOLDER)
    p.add_argument("--empresas", "-e", nargs="+", choices=EMPRESAS)
    args = p.parse_args()
    
    OUTPUT_FOLDER = args.output
    ODIPipeline(args.base).run(args.empresas)
