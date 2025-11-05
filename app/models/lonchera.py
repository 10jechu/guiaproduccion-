from pydantic import BaseModel
from datetime import date

class Lonchera(BaseModel):
    id: int
    hijo_id: int
    fecha: date
    estado: str
    direccion_id: int | None = None
