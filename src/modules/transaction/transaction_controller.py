from datetime import datetime
from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy import extract
from sqlalchemy.orm import Session

from adapters.database.datasource import get_session
from modules.transaction.transaction_model import Transaction, TransactionType

router = APIRouter()


class ListThisMonthTransactionsResponse(BaseModel):
    id: UUID
    account_id: UUID
    type: TransactionType
    amount: int
    datetime: datetime


@router.get(
    "/account/{account_id}/transaction",
    response_model=List[ListThisMonthTransactionsResponse],
)
def list_this_month_transactions(
    account_id: UUID, session: Session = Depends(get_session)
):
    current_month = datetime.now().month

    return (
        session.query(Transaction)
        .filter(
            (Transaction.account_id == account_id)
            and extract("month", Transaction.date) == current_month
        )
        .all()
    )
