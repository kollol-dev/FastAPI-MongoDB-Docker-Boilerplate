from fastapi import APIRouter

# Bring all routers from all the modules
from health_check.health_check_route import health_check_router

router = APIRouter()
router.include_router(health_check_router, prefix='/health_check')

# def init_routers(app_: FastAPI) -> None:
#     app_.include_router(router)