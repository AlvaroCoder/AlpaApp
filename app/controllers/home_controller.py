from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).parent.parent / "views" / "templates")


@router.get("/", response_class=HTMLResponse)
async def landing(request: Request):
    return templates.TemplateResponse("landing.html", {"request": request})


@router.get("/app", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "usuario": "Don Juan"})
