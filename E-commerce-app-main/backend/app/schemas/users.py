from datetime import datetime
from enum import Enum
from typing import List


class UserRole(str, Enum):
    OWNER = "owner"
    STAFF = "staff"

class User:
    def __init__(
        self,
        userId: str,
        name: str,
        email: str,
        role: UserRole,
        shop_ids: List[str],
        created_at: datetime,
        updated_at: datetime
    ):
        self.userId = userId
        self.name = name
        self.email = email
        self.role = role
        self.shop_ids = shop_ids
        self.created_at = created_at
        self.updated_at = updated_at