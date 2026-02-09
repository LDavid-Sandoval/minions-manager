from fastapi import FastAPI
from app.core.database import init_db
from app.routers import category_router, player_router

app = FastAPI(title="Minions FC Backend")

@app.on_event("startup")
async def on_startup():
    await init_db()
    print("✅ Base de Datos y Modelos Iniciados")

# Registrar Routers
app.include_router(category_router.router)
app.include_router(player_router.router)