#!/usr/bin/env python3
"""
ODI SHOPIFY MANAGER v1.0
========================
Sistema de gestión multi-tienda para SRM (Sistema de Repuestos de Motos)
Desarrollado para el ecosistema ODI (Organismo Digital Industrial)

Comandos de voz soportados:
- "ODI, mejora los textos de Bara"
- "ODI, detecta duplicados en todas las tiendas"
- "ODI, sincroniza precios en las 10 tiendas"
- "ODI, lista productos de Yokomar"
- "ODI, actualiza inventario de Kaiqi"

Autor: Juan David Jiménez Sierra
Fecha: 24 de Enero 2026
"""

import os
import json
import requests
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# ============================================
# CONFIGURACIÓN DE TIENDAS
# ============================================

@dataclass
class ShopifyStore:
    """Representa una tienda Shopify"""
    name: str
    shop_domain: str
    access_token: str
    api_version: str = "2026-01"
    
    @property
    def base_url(self) -> str:
        return f"https://{self.shop_domain}/admin/api/{self.api_version}"
    
    @property
    def headers(self) -> Dict[str, str]:
        return {
            "X-Shopify-Access-Token": self.access_token,
            "Content-Type": "application/json"
        }


# Inicializar las 10 tiendas
STORES: Dict[str, ShopifyStore] = {
    "bara": ShopifyStore(
        name="Bara Importaciones",
        shop_domain=os.getenv("BARA_SHOP", "4jqcki-jq.myshopify.com"),
        access_token=os.getenv("BARA_TOKEN", "")
    ),
    "yokomar": ShopifyStore(
        name="Yokomar",
        shop_domain=os.getenv("YOKOMAR_SHOP", "u1zmhk-ts.myshopify.com"),
        access_token=os.getenv("YOKOMAR_TOKEN", "")
    ),
    "kaiqi": ShopifyStore(
        name="Kaiqi Parts",
        shop_domain=os.getenv("KAIQI_SHOP", "u03tqc-0e.myshopify.com"),
        access_token=os.getenv("KAIQI_TOKEN", "")
    ),
    "dfg": ShopifyStore(
        name="DFG",
        shop_domain=os.getenv("DFG_SHOP", "0se1jt-q1.myshopify.com"),
        access_token=os.getenv("DFG_TOKEN", "")
    ),
    "duna": ShopifyStore(
        name="Duna",
        shop_domain=os.getenv("DUNA_SHOP", "ygsfhq-fs.myshopify.com"),
        access_token=os.getenv("DUNA_TOKEN", "")
    ),
    "imbra": ShopifyStore(
        name="Imbra",
        shop_domain=os.getenv("IMBRA_SHOP", "0i1mdf-gi.myshopify.com"),
        access_token=os.getenv("IMBRA_TOKEN", "")
    ),
    "japan": ShopifyStore(
        name="Japan",
        shop_domain=os.getenv("JAPAN_SHOP", "7cy1zd-qz.myshopify.com"),
        access_token=os.getenv("JAPAN_TOKEN", "")
    ),
    "leo": ShopifyStore(
        name="Leo",
        shop_domain=os.getenv("LEO_SHOP", "h1hywg-pq.myshopify.com"),
        access_token=os.getenv("LEO_TOKEN", "")
    ),
    "store": ShopifyStore(
        name="Store",
        shop_domain=os.getenv("STORE_SHOP", "0b6umv-11.myshopify.com"),
        access_token=os.getenv("STORE_TOKEN", "")
    ),
    "vaisand": ShopifyStore(
        name="Vaisand",
        shop_domain=os.getenv("VAISAND_SHOP", "z4fpdj-mz.myshopify.com"),
        access_token=os.getenv("VAISAND_TOKEN", "")
    ),
}


# ============================================
# CLASE PRINCIPAL: ODI SHOPIFY MANAGER
# ============================================

class ODIShopifyManager:
    """
    Gestor principal de tiendas Shopify para ODI.
    Permite operaciones CRUD y análisis en múltiples tiendas.
    """
    
    def __init__(self):
        self.stores = STORES
        self._validate_tokens()
    
    def _validate_tokens(self) -> None:
        """Valida que todos los tokens estén configurados"""
        missing = [name for name, store in self.stores.items() if not store.access_token]
        if missing:
            print(f"⚠️  Advertencia: Tokens faltantes para: {', '.join(missing)}")
    
    # ----------------------------------------
    # OPERACIONES DE PRODUCTOS
    # ----------------------------------------
    
    def get_products(self, store_key: str, limit: int = 50) -> List[Dict]:
        """Obtiene productos de una tienda"""
        store = self.stores.get(store_key.lower())
        if not store:
            raise ValueError(f"Tienda '{store_key}' no encontrada")
        
        url = f"{store.base_url}/products.json?limit={limit}"
        response = requests.get(url, headers=store.headers)
        response.raise_for_status()
        return response.json().get("products", [])
    
    def get_all_products(self, store_key: str) -> List[Dict]:
        """Obtiene TODOS los productos de una tienda (paginación automática)"""
        store = self.stores.get(store_key.lower())
        if not store:
            raise ValueError(f"Tienda '{store_key}' no encontrada")
        
        all_products = []
        url = f"{store.base_url}/products.json?limit=250"
        
        while url:
            response = requests.get(url, headers=store.headers)
            response.raise_for_status()
            products = response.json().get("products", [])
            all_products.extend(products)
            
            # Verificar si hay más páginas
            link_header = response.headers.get("Link", "")
            url = None
            if 'rel="next"' in link_header:
                for link in link_header.split(","):
                    if 'rel="next"' in link:
                        url = link.split(";")[0].strip("<> ")
                        break
        
        return all_products
    
    def get_product(self, store_key: str, product_id: int) -> Dict:
        """Obtiene un producto específico"""
        store = self.stores.get(store_key.lower())
        if not store:
            raise ValueError(f"Tienda '{store_key}' no encontrada")
        
        url = f"{store.base_url}/products/{product_id}.json"
        response = requests.get(url, headers=store.headers)
        response.raise_for_status()
        return response.json().get("product", {})
    
    def update_product(self, store_key: str, product_id: int, data: Dict) -> Dict:
        """Actualiza un producto"""
        store = self.stores.get(store_key.lower())
        if not store:
            raise ValueError(f"Tienda '{store_key}' no encontrada")
        
        url = f"{store.base_url}/products/{product_id}.json"
        payload = {"product": data}
        response = requests.put(url, headers=store.headers, json=payload)
        response.raise_for_status()
        return response.json().get("product", {})
    
    def update_product_description(self, store_key: str, product_id: int, 
                                    new_title: str = None, new_description: str = None) -> Dict:
        """Actualiza título y/o descripción de un producto"""
        data = {}
        if new_title:
            data["title"] = new_title
        if new_description:
            data["body_html"] = new_description
        
        return self.update_product(store_key, product_id, data)
    
    # ----------------------------------------
    # OPERACIONES DE INVENTARIO
    # ----------------------------------------
    
    def get_inventory_levels(self, store_key: str, location_id: int = None) -> List[Dict]:
        """Obtiene niveles de inventario"""
        store = self.stores.get(store_key.lower())
        if not store:
            raise ValueError(f"Tienda '{store_key}' no encontrada")
        
        # Primero obtener locations si no se proporciona
        if not location_id:
            locations = self.get_locations(store_key)
            if locations:
                location_id = locations[0]["id"]
        
        url = f"{store.base_url}/inventory_levels.json?location_ids={location_id}"
        response = requests.get(url, headers=store.headers)
        response.raise_for_status()
        return response.json().get("inventory_levels", [])
    
    def get_locations(self, store_key: str) -> List[Dict]:
        """Obtiene ubicaciones de una tienda"""
        store = self.stores.get(store_key.lower())
        if not store:
            raise ValueError(f"Tienda '{store_key}' no encontrada")
        
        url = f"{store.base_url}/locations.json"
        response = requests.get(url, headers=store.headers)
        response.raise_for_status()
        return response.json().get("locations", [])
    
    # ----------------------------------------
    # OPERACIONES MULTI-TIENDA
    # ----------------------------------------
    
    def get_products_count_all_stores(self) -> Dict[str, int]:
        """Obtiene el conteo de productos en todas las tiendas"""
        counts = {}
        for store_key, store in self.stores.items():
            try:
                url = f"{store.base_url}/products/count.json"
                response = requests.get(url, headers=store.headers)
                response.raise_for_status()
                counts[store_key] = response.json().get("count", 0)
            except Exception as e:
                counts[store_key] = f"Error: {str(e)}"
        return counts
    
    def find_duplicates_across_stores(self, field: str = "title") -> Dict[str, List[Dict]]:
        """
        Encuentra productos duplicados entre tiendas basado en un campo.
        Útil para detectar productos repetidos por SKU, título, etc.
        """
        all_products = {}
        duplicates = {}
        
        for store_key in self.stores:
            try:
                products = self.get_all_products(store_key)
                for product in products:
                    key = product.get(field, "").lower().strip()
                    if key:
                        if key not in all_products:
                            all_products[key] = []
                        all_products[key].append({
                            "store": store_key,
                            "product_id": product["id"],
                            "title": product["title"],
                            "handle": product.get("handle", "")
                        })
            except Exception as e:
                print(f"Error en {store_key}: {e}")
        
        # Filtrar solo los duplicados
        for key, items in all_products.items():
            if len(items) > 1:
                duplicates[key] = items
        
        return duplicates
    
    def sync_prices_across_stores(self, source_store: str, 
                                   target_stores: List[str] = None) -> Dict[str, Any]:
        """
        Sincroniza precios de una tienda fuente a otras tiendas.
        Basado en SKU como identificador común.
        """
        if not target_stores:
            target_stores = [k for k in self.stores.keys() if k != source_store]
        
        # Obtener productos de la tienda fuente
        source_products = self.get_all_products(source_store)
        source_prices = {}
        
        for product in source_products:
            for variant in product.get("variants", []):
                sku = variant.get("sku", "").strip()
                if sku:
                    source_prices[sku] = {
                        "price": variant.get("price"),
                        "compare_at_price": variant.get("compare_at_price")
                    }
        
        results = {"source": source_store, "synced": {}, "errors": []}
        
        for target_store in target_stores:
            try:
                target_products = self.get_all_products(target_store)
                updated = 0
                
                for product in target_products:
                    for variant in product.get("variants", []):
                        sku = variant.get("sku", "").strip()
                        if sku in source_prices:
                            # Actualizar precio
                            store = self.stores[target_store]
                            url = f"{store.base_url}/variants/{variant['id']}.json"
                            payload = {
                                "variant": {
                                    "price": source_prices[sku]["price"],
                                    "compare_at_price": source_prices[sku]["compare_at_price"]
                                }
                            }
                            response = requests.put(url, headers=store.headers, json=payload)
                            if response.status_code == 200:
                                updated += 1
                
                results["synced"][target_store] = updated
            except Exception as e:
                results["errors"].append({"store": target_store, "error": str(e)})
        
        return results
    
    # ----------------------------------------
    # ANÁLISIS Y REPORTES
    # ----------------------------------------
    
    def generate_inventory_report(self) -> Dict[str, Any]:
        """Genera un reporte de inventario de todas las tiendas"""
        report = {
            "total_products": 0,
            "by_store": {},
            "low_stock": [],
            "out_of_stock": []
        }
        
        for store_key in self.stores:
            try:
                products = self.get_all_products(store_key)
                store_data = {
                    "product_count": len(products),
                    "total_variants": 0,
                    "total_inventory": 0
                }
                
                for product in products:
                    variants = product.get("variants", [])
                    store_data["total_variants"] += len(variants)
                    
                    for variant in variants:
                        qty = variant.get("inventory_quantity", 0)
                        store_data["total_inventory"] += qty
                        
                        if qty == 0:
                            report["out_of_stock"].append({
                                "store": store_key,
                                "product": product["title"],
                                "variant": variant.get("title", "Default"),
                                "sku": variant.get("sku", "N/A")
                            })
                        elif qty < 5:
                            report["low_stock"].append({
                                "store": store_key,
                                "product": product["title"],
                                "variant": variant.get("title", "Default"),
                                "sku": variant.get("sku", "N/A"),
                                "quantity": qty
                            })
                
                report["by_store"][store_key] = store_data
                report["total_products"] += len(products)
                
            except Exception as e:
                report["by_store"][store_key] = {"error": str(e)}
        
        return report
    
    # ----------------------------------------
    # UTILIDADES
    # ----------------------------------------
    
    def test_connection(self, store_key: str = None) -> Dict[str, bool]:
        """Prueba la conexión a una o todas las tiendas"""
        stores_to_test = [store_key] if store_key else list(self.stores.keys())
        results = {}
        
        for key in stores_to_test:
            store = self.stores.get(key.lower())
            if not store:
                results[key] = False
                continue
            
            try:
                url = f"{store.base_url}/shop.json"
                response = requests.get(url, headers=store.headers)
                results[key] = response.status_code == 200
            except:
                results[key] = False
        
        return results
    
    def get_store_info(self, store_key: str) -> Dict:
        """Obtiene información de la tienda"""
        store = self.stores.get(store_key.lower())
        if not store:
            raise ValueError(f"Tienda '{store_key}' no encontrada")
        
        url = f"{store.base_url}/shop.json"
        response = requests.get(url, headers=store.headers)
        response.raise_for_status()
        return response.json().get("shop", {})


# ============================================
# CLI INTERFACE
# ============================================

def main():
    """Interfaz de línea de comandos"""
    import argparse
    
    parser = argparse.ArgumentParser(description="ODI Shopify Manager")
    parser.add_argument("command", choices=[
        "test", "count", "products", "duplicates", 
        "sync-prices", "report", "info"
    ])
    parser.add_argument("--store", "-s", help="Tienda específica")
    parser.add_argument("--source", help="Tienda fuente (para sync)")
    parser.add_argument("--limit", type=int, default=50)
    
    args = parser.parse_args()
    manager = ODIShopifyManager()
    
    if args.command == "test":
        print("🔍 Probando conexión a tiendas...")
        results = manager.test_connection(args.store)
        for store, ok in results.items():
            status = "✅" if ok else "❌"
            print(f"  {status} {store}")
    
    elif args.command == "count":
        print("📊 Conteo de productos por tienda:")
        counts = manager.get_products_count_all_stores()
        total = 0
        for store, count in counts.items():
            print(f"  • {store}: {count}")
            if isinstance(count, int):
                total += count
        print(f"\n  Total: {total} productos")
    
    elif args.command == "products":
        if not args.store:
            print("❌ Especifica una tienda con --store")
            return
        products = manager.get_products(args.store, args.limit)
        print(f"📦 Productos de {args.store} ({len(products)}):")
        for p in products[:10]:
            print(f"  • {p['title']}")
    
    elif args.command == "duplicates":
        print("🔍 Buscando duplicados entre tiendas...")
        duplicates = manager.find_duplicates_across_stores()
        print(f"  Encontrados: {len(duplicates)} productos duplicados")
        for title, items in list(duplicates.items())[:5]:
            print(f"\n  '{title[:50]}...':")
            for item in items:
                print(f"    - {item['store']}")
    
    elif args.command == "report":
        print("📊 Generando reporte de inventario...")
        report = manager.generate_inventory_report()
        print(f"\n  Total productos: {report['total_products']}")
        print(f"  Sin stock: {len(report['out_of_stock'])}")
        print(f"  Stock bajo: {len(report['low_stock'])}")
    
    elif args.command == "info":
        if not args.store:
            print("❌ Especifica una tienda con --store")
            return
        info = manager.get_store_info(args.store)
        print(f"🏪 {info.get('name', 'N/A')}")
        print(f"  Domain: {info.get('domain', 'N/A')}")
        print(f"  Email: {info.get('email', 'N/A')}")


if __name__ == "__main__":
    main()
