from fastapi import APIRouter, HTTPException
from app.models.usuario import Usuario

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

usuarios = [
    Usuario(id=1, nombre="Jesús Vilardi", email="user@test.com", hash_password="hashed123", activo=True, rol_id=1, membresia_id=3)
]

# ✅ READ - obtener todos
@router.get("/")
def obtener_usuarios():
    return usuarios

# ✅ CREATE - agregar usuario
@router.post("/")
def crear_usuario(usuario: Usuario):
    for u in usuarios:
        if u.id == usuario.id:
            raise HTTPException(status_code=400, detail="El usuario ya existe")
    usuarios.append(usuario)
    return {"mensaje": "Usuario creado correctamente", "usuario": usuario}

# ✅ UPDATE - actualizar usuario por id
@router.put("/{usuario_id}")
def actualizar_usuario(usuario_id: int, usuario_actualizado: Usuario):
    for i, u in enumerate(usuarios):
        if u.id == usuario_id:
            usuarios[i] = usuario_actualizado
            return {"mensaje": "Usuario actualizado", "usuario": usuario_actualizado}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# ✅ DELETE - eliminar usuario por id
@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int):
    for u in usuarios:
        if u.id == usuario_id:
            usuarios.remove(u)
            return {"mensaje": f"Usuario {usuario_id} eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
