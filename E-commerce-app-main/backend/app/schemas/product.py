from typing import Mapping

class Product:
    def __init__(
            self,
            productID: str,
            name: str,
            description: str,
            category: str,
            sub_category: str,
            price: Mapping[str, float],
            stock: Mapping[str, int],
            is_active: bool,
    ):
        self.productID = productID
        self.name = name
        self.description = description
        self.category = category
        self.sub_category = sub_category
        self.price = price
        self.stock = stock
        self.is_active = is_active