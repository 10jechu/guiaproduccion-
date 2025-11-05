from fastapi import FastAPI
from app.routes import items

app = FastAPI(title="Guia de Produccion con FastAPI")

# Incluir rutas
app.include_router(items.router)

@app.get("/")
def root():
    return {"message": "Hola profe "
    ", FastAPI esta funcionando correctamente"}

