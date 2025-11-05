from fastapi import APIRouter
from app.models.item import Item

router = APIRouter(prefix="/items", tags=["items"])

# Base temporal de datos
items_db = []

@router.get("/")
def obtener_items():
    return {"items": items_db}

@router.post("/")
def crear_item(item: Item):
    items_db.append(item)
    return {"mensaje": "Item agregado correctamente", "item": item}
