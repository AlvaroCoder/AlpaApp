from dataclasses import dataclass
from typing import Optional


@dataclass
class Cultivo:
    id: str
    nombre: str
    color_bg: str
    color_icon: str
    categoria: str = "transitorio"
    descripcion: Optional[str] = None


CULTIVOS_TRANSITORIOS: list[Cultivo] = [
    Cultivo("arroz", "Arroz", "#DBEAFE", "#1E40AF"),
    Cultivo("cebada_grano", "Cebada grano", "#FEF3C7", "#92400E"),
    Cultivo("maiz_amarillo_duro", "Maíz amarillo duro", "#FEF3C7", "#78350F"),
    Cultivo("maiz_blanco_duro", "Maíz blanco duro", "#F3F4F6", "#6B7280"),
    Cultivo("maiz_amilaceo", "Maíz amiláceo", "#FEE2E2", "#991B1B"),
    Cultivo("maiz_choclo", "Maíz choclo", "#D1FAE5", "#065F46"),
    Cultivo("sorgo", "Sorgo", "#FCE7F3", "#9D174D"),
    Cultivo("trigo", "Trigo", "#FEF3C7", "#B45309"),
    Cultivo("papa", "Papa", "#F5F5F4", "#57534E"),
    Cultivo("frijol", "Frijol", "#FEF9C3", "#713F12"),
    Cultivo("algodon", "Algodón", "#F0F9FF", "#0369A1"),
]

CULTIVOS_BY_ID: dict[str, Cultivo] = {c.id: c for c in CULTIVOS_TRANSITORIOS}
