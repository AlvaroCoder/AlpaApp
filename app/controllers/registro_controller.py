from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from typing import Optional

from app.models.cultivo import CULTIVOS_TRANSITORIOS, CULTIVOS_BY_ID

router = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).parent.parent / "views" / "templates")

# In-memory session store (replace with real session/DB in production)
_session: dict = {}


@router.get("/transitorio/ubicacion", response_class=HTMLResponse)
async def paso_ubicacion(request: Request):
    return templates.TemplateResponse(
        "registro/ubicacion.html",
        {"request": request, "tipo": "Sembrado transitorio", "datos": _session},
    )


@router.post("/transitorio/ubicacion")
async def guardar_ubicacion(
    request: Request,
    parcela_nombre: str = Form("Parcela 1"),
    area_ha: float = Form(0.0),
    geojson: Optional[str] = Form(None),
    ubicacion_texto: Optional[str] = Form(None),
    lat: Optional[float] = Form(None),
    lng: Optional[float] = Form(None),
):
    _session.update(
        parcela_nombre=parcela_nombre,
        area_ha=area_ha,
        geojson=geojson,
        ubicacion_texto=ubicacion_texto,
        lat=lat,
        lng=lng,
    )
    return RedirectResponse("/registro/transitorio/cultivo", status_code=303)


@router.get("/transitorio/cultivo", response_class=HTMLResponse)
async def paso_cultivo(request: Request):
    return templates.TemplateResponse(
        "registro/cultivo.html",
        {
            "request": request,
            "tipo": "Sembrado transitorio",
            "datos": _session,
            "cultivos": CULTIVOS_TRANSITORIOS,
        },
    )


@router.post("/transitorio/cultivo")
async def guardar_cultivo(
    request: Request,
    cultivo_id: str = Form(...),
):
    cultivo = CULTIVOS_BY_ID.get(cultivo_id)
    _session.update(cultivo_id=cultivo_id, cultivo_nombre=cultivo.nombre if cultivo else cultivo_id)
    return RedirectResponse("/registro/transitorio/rotacion", status_code=303)


@router.get("/transitorio/rotacion", response_class=HTMLResponse)
async def paso_rotacion(request: Request):
    return templates.TemplateResponse(
        "registro/rotacion.html",
        {
            "request": request,
            "tipo": "Sembrado transitorio",
            "datos": _session,
            "cultivos_anteriores": ["Papa", "Frijol", "Arroz", "Maíz", "Algodón", "Otro"],
        },
    )


@router.post("/transitorio/rotacion")
async def guardar_rotacion(
    request: Request,
    rotacion: str = Form(...),
    cultivo_anterior: Optional[str] = Form(None),
):
    _session.update(rotacion=rotacion, cultivo_anterior=cultivo_anterior)
    return RedirectResponse("/registro/transitorio/resumen", status_code=303)


@router.get("/transitorio/resumen", response_class=HTMLResponse)
async def resumen(request: Request):
    return templates.TemplateResponse(
        "registro/resumen.html",
        {"request": request, "datos": dict(_session)},
    )
