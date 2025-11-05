from fastapi import APIRouter
from app.models.usuario import Usuario

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

usuarios = [
    Usuario(id=1, nombre="Jesús Vilardi", email="user@test.com", hash_password="hashed123", activo=True, rol_id=1, membresia_id=3)
]

@router.get("/")
def obtener_usuarios():
    return usuarios
