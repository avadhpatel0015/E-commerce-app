from __future__ import annotations

from datetime import datetime
from enum import Enum


class PaymentMode(str, Enum):
    CASH = "cash"


class SalePayment:
    def __init__(
        self,
        paymentId: str,
        sale_id: str,
        shop_id: str,
        amount_paid: float,
        payment_date: datetime,
        mode: PaymentMode,
        created_at: datetime,
    ):
        self.paymentId = paymentId
        self.sale_id = sale_id
        self.shop_id = shop_id
        self.amount_paid = amount_paid
        self.payment_date = payment_date
        self.mode = mode
        self.created_at = created_at
