from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List


class PurchaseStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class PurchaseItem:
    def __init__(self, product_id: str, qty: int, cost: float):
        self.product_id = product_id
        self.qty = qty
        self.cost = cost


class Purchase:
    def __init__(
        self,
        purchaseId: str,
        shop_id: str,
        supplier_name: str,
        purchase_date: datetime,
        status: PurchaseStatus,
        total_cost: float,
        is_edited: bool,
        items: List[PurchaseItem],
        created_at: datetime,
        updated_at: datetime,
    ):
        self.purchaseId = purchaseId
        self.shop_id = shop_id
        self.supplier_name = supplier_name
        self.purchase_date = purchase_date
        self.status = status
        self.total_cost = total_cost
        self.is_edited = is_edited
        self.items = items
        self.created_at = created_at
        self.updated_at = updated_at
