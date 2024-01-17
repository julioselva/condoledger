from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from adapters.database.datasource import get_session
from modules.account.account_model import Account

router = APIRouter()


class GetAccountBalanceResponse(BaseModel):
    balance: int


@router.get("/account/{account_id}/balance", response_model=GetAccountBalanceResponse)
def get_account_balance(account_id: UUID, session: Session = Depends(get_session)):
    account = session.query(Account).filter(Account.id == account_id).one_or_none()
    if not account:
        raise HTTPException(
            status_code=404, detail="The given account id was not found"
        )
    return {"balance": account.balance}
