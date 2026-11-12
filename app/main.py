from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from app.config import settings
from app.controllers.home_controller import router as home_router
from app.controllers.registro_controller import router as registro_router
from app.controllers.parcela_controller import router as parcela_router

app = FastAPI(title=settings.app_name, version="0.1.0")

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent / "static"),
    name="static",
)

app.include_router(home_router)
app.include_router(registro_router, prefix="/registro")
app.include_router(parcela_router, prefix="/parcelas")
