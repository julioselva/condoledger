import uuid
from datetime import datetime
from enum import Enum, auto

from sqlalchemy import Enum as SQLEnum
from sqlalchemy import ForeignKey, Integer, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import UUID, DateTime

from adapters.database.base import Base


class TransactionType(Enum):
    DEBIT = "DEBIT"
    CREDIT = "CREDIT"


class Transaction(Base):
    __tablename__ = "transaction"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    account_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("account.id"), nullable=False
    )
    type: Mapped[TransactionType] = mapped_column(
        SQLEnum("DEBIT", "CREDIT", name="transaction_type"), nullable=False
    )
    amount: Mapped[int] = mapped_column(Integer)
    datetime: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
