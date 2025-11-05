from fastapi import APIRouter, HTTPException
from app.models.alimento import Alimento

router = APIRouter(prefix="/alimentos", tags=["Alimentos"])

alimentos = [
    Alimento(id=10, nombre="Yogur Griego", kcal=59.0, proteinas=10.0, carbos=3.6, costo=1800.0, activo=True)
]

# ✅ READ - obtener todos
@router.get("/")
def obtener_alimentos():
    return alimentos

# ✅ CREATE - agregar alimento
@router.post("/")
def crear_alimento(alimento: Alimento):
    for a in alimentos:
        if a.id == alimento.id:
            raise HTTPException(status_code=400, detail="El alimento ya existe")
    alimentos.append(alimento)
    return {"mensaje": "Alimento creado correctamente", "alimento": alimento}

# ✅ UPDATE - actualizar alimento por id
@router.put("/{alimento_id}")
def actualizar_alimento(alimento_id: int, alimento_actualizado: Alimento):
    for i, a in enumerate(alimentos):
        if a.id == alimento_id:
            alimentos[i] = alimento_actualizado
            return {"mensaje": "Alimento actualizado", "alimento": alimento_actualizado}
    raise HTTPException(status_code=404, detail="Alimento no encontrado")

# ✅ DELETE - eliminar alimento por id
@router.delete("/{alimento_id}")
def eliminar_alimento(alimento_id: int):
    for a in alimentos:
        if a.id == alimento_id:
            alimentos.remove(a)
            return {"mensaje": f"Alimento {alimento_id} eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Alimento no encontrado")
