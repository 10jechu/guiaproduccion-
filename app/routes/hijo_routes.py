from fastapi import APIRouter
from app.models.hijo import Hijo

router = APIRouter(prefix="/hijos", tags=["Hijos"])

hijos = [
    Hijo(id=5, nombre="Daniela", usuario_id=1)
]

@router.get("/")
def obtener_hijos():
    return hijos
