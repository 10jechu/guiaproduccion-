from fastapi import FastAPI
from app.routes import usuario_routes, hijo_routes, alimento_routes, lonchera_routes

app = FastAPI(title="NutriBox API")

app.include_router(usuario_routes.router)
app.include_router(hijo_routes.router)
app.include_router(alimento_routes.router)
app.include_router(lonchera_routes.router)

@app.get("/")
def root():
    return {"mensaje": "API NutriBox funcionando correctamente"}
