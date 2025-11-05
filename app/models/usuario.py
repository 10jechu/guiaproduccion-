from pydantic import BaseModel, EmailStr

class Usuario(BaseModel):
    id: int
    nombre: str
    email: EmailStr
    hash_password: str
    activo: bool
    rol_id: int
    membresia_id: int
