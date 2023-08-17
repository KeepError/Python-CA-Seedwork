from fastapi.applications import FastAPI

from .modules import user


def get_app() -> FastAPI:
    app = FastAPI()

    app.include_router(user.users_router)

    return app
