from pydantic import BaseModel
from typing import Optional


class ParcelaBase(BaseModel):
    nombre: str
    area_ha: float
    geojson: Optional[str] = None
    ubicacion_texto: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None


class Parcela(ParcelaBase):
    id: int


class ParcelaCreate(ParcelaBase):
    pass
