from datetime import datetime

class Expense:
    def __init__(
            self,
            expenseId: str,
            shope_id: str,
            catagory: str,
            amount: float,
            created_at: datetime,
    ):
        self.expenseId = expenseId
        self.shope_id = shope_id
        self.catagory = catagory
        self.amount = amount
        self.created_at = created_at