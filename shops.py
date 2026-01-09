from datetime import datetime
from typing import List

class Shop:
    def __init__(
            self,
            shopeId: str,
            name: str,
            staff_ids: List[str],
            created_at: datetime,
    ):
        self.shopeId = shopeId
        self.name = name
        self.staff_ids = staff_ids
        self.created_at = created_at