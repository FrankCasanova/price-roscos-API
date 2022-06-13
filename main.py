from fastapi import FastAPI

from api.urls import router


def include_router(app: FastAPI) -> None:
    app.include_router(router)


def start_app() -> None:
    app = FastAPI()
    include_router(app)
    return app


app = start_app()
