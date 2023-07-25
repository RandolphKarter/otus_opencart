from dataclasses import dataclass


@dataclass
class Product:
    product_name: str = None
    product_model: str = None
    product_description: str = None
    product_price: int = None
