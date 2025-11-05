from pydantic import BaseModel

class Item(BaseModel):
    id: int
    nombre: str
    precio: float
    descripcion: str | None = None

