from pydantic import BaseModel

class Hijo(BaseModel):
    id: int
    nombre: str
    usuario_id: int
