"""Importing time to get the system uptime"""
import time

import psutil
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HealthCheckResponse(BaseModel):
    uptime: float


@router.get("/health", response_model=HealthCheckResponse)
def health_check():
    """Return the API uptime"""
    return {"uptime": time.time() - psutil.boot_time()}
