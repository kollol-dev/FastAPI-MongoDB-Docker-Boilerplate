import sys
from dotenv import load_dotenv
from fastapi import FastAPI, Depends

sys.path.insert(1, './app')
load_dotenv()

from core.dependencies.log import Log
from core.routes import router
from core.config import config

def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)
    

def create_app() -> FastAPI:
    app_ = FastAPI(
        title="FastAPI Boilerplate",
        description="FastAPI Boilerplate",
        version="1.0.0",
        docs_url=None if config.ENVIRONMENT == "production" else "/docs",
        redoc_url=None if config.ENVIRONMENT == "production" else "/redoc",
        debug=config.ENVIRONMENT == "production",
        dependencies=[Depends(Log)],
        # middleware=make_middleware(),
    )
    init_routers(app_=app_)
    # init_listeners(app_=app_)
    # init_cache()
    return app_

app = create_app()