from fastapi import APIRouter
from app.models.alimento import Alimento

router = APIRouter(prefix="/alimentos", tags=["Alimentos"])

alimentos = [
    Alimento(id=10, nombre="Yogur Griego", kcal=59.0, proteinas=10.0, carbos=3.6, costo=1800.0, activo=True)
]

@router.get("/")
def obtener_alimentos():
    return alimentos
