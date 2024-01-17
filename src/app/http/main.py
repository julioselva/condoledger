from fastapi import FastAPI

from modules.account import account_controller
from modules.health import health_controller
from modules.transaction import transaction_controller

app = FastAPI(
    root_path="/api/v1",
)


app.include_router(health_controller.router)
app.include_router(account_controller.router)
app.include_router(transaction_controller.router)
