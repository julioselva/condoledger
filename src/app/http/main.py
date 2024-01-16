from fastapi import FastAPI
from modules.health import health_controller

app = FastAPI(
    root_path="/api/v1",
)


app.include_router(health_controller.router)
