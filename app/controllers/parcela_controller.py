from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).parent.parent / "views" / "templates")


@router.get("/", response_class=HTMLResponse)
async def lista_parcelas(request: Request):
    return templates.TemplateResponse("parcelas/lista.html", {"request": request, "parcelas": []})
