from pydantic import BaseModel

class Alimento(BaseModel):
    id: int
    nombre: str
    kcal: float
    proteinas: float
    carbos: float
    costo: float
    activo: bool
