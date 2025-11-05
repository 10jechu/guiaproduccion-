from fastapi import APIRouter
from app.models.lonchera import Lonchera
from datetime import date

router = APIRouter(prefix="/loncheras", tags=["Loncheras"])

loncheras = [
    Lonchera(id=101, hijo_id=5, fecha=date(2025, 11, 15), estado="Borrador", direccion_id=4)
]

@router.get("/")
def obtener_loncheras():
    return loncheras
