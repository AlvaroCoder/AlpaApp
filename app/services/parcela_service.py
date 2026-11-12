"""Parcela business logic (placeholder – connect to DB when ready)."""
from app.models.parcela import Parcela, ParcelaCreate

_db: list[Parcela] = []
_counter = 0


def create_parcela(data: ParcelaCreate) -> Parcela:
    global _counter
    _counter += 1
    p = Parcela(id=_counter, **data.model_dump())
    _db.append(p)
    return p


def list_parcelas() -> list[Parcela]:
    return list(_db)


def get_parcela(parcela_id: int) -> Parcela | None:
    return next((p for p in _db if p.id == parcela_id), None)
