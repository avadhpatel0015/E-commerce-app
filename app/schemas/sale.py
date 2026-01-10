from datetime import datetime
from typing import List
from enum import Enum

class SaleStatus(str, Enum):
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class SaleItem:
    def __init__(self, product_id: str, qty: int, price: float):
        self.product_id = product_id
        self.qty = qty
        self.price = price

class Sale:
    def __init__(
        self,
        saleId: str,
        shop_id: str,
        customer_name: str,
        sale_date: datetime,
        status: SaleStatus,
        total_amount: float,
        is_edited: bool,
        items: List[SaleItem],
        created_at: datetime,
        updated_at: datetime,
    ):
        self.saleId = saleId
        self.shop_id = shop_id
        self.customer_name = customer_name
        self.sale_date = sale_date
        self.status = status
        self.total_amount = total_amount
        self.is_edited = is_edited
        self.items = items
        self.created_at = created_at
        self.updated_at = updated_at
