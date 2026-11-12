from pydantic import BaseModel
from typing import Optional


class RegistroBase(BaseModel):
    parcela_nombre: str = "Parcela 1"
    area_ha: float = 0.0
    geojson: Optional[str] = None
    ubicacion_texto: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
    cultivo_id: Optional[str] = None
    cultivo_nombre: Optional[str] = None
    rotacion: Optional[str] = None
    cultivo_anterior_id: Optional[str] = None


class RegistroCreate(RegistroBase):
    pass


class Registro(RegistroBase):
    id: int
