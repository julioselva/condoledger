import uuid
from enum import Enum, auto

from sqlalchemy import Enum as SQLEnum
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import UUID

from adapters.database.base import Base


class AccountType(Enum):
    CHECKING = "CHECKING"
    SAVINGS = "SAVINGS"


class Account(Base):
    __tablename__ = "account"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    type: Mapped[AccountType] = mapped_column(
        SQLEnum("CHECKING", "SAVINGS", name="account_type"), nullable=False
    )
    balance: Mapped[int] = mapped_column(Integer, default=0)
