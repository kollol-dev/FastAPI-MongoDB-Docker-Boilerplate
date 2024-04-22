from typing import Callable
from fastapi import APIRouter, Depends, Request, Response

# Import All Controller Methods
from .health_check_controller import get_health_status, increase_health_score

health_check_router = APIRouter()

# Route prefix = '/api/v1/health_check'

@health_check_router.get("/")
async def check_health_status(request: Request, response: Response):
    return get_health_status(request, response)

# @health_check_router.post("/get_healthy")
# async def make_healthy_status(request: Request, response: Response):
#     request_json = await request.body()
#     return increase_health_score(request_json, response)