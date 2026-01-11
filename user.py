import uuid
import enum
from datetime import datetime, timezone

from sqlalchemy import Column, String, DateTime, Enum, JSON
from database import Base


class UserRole(enum.Enum):
    OWNER = "OWNER"
    STAFF = "STAFF"


class User(Base):
    __tablename__ = "users"

    userId = Column(
        String,
        primary_key=True,
        index=True,
        default=lambda: str(uuid.uuid4())
    )

    name = Column(String, nullable=False)

    role = Column(
        Enum(UserRole, name="user_role"),
        nullable=False
    )

    shop_ids = Column(
        JSON,
        default=list   
    )

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc) 
    )

    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )   