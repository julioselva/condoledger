import time

import psutil
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class GetHealthCheckResponse(BaseModel):
    uptime: float


@router.get("/health", response_model=GetHealthCheckResponse)
def get_health_check():
    """Return the API uptime"""
    return {"uptime": time.time() - psutil.boot_time()}
