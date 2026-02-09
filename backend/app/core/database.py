from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.core.config import settings
from app.models.category import Category
from app.models.player import Player

async def init_db():
    # settings.MONGO_URL ya contiene la cadena completa construida
    client = AsyncIOMotorClient(settings.MONGO_URL)
    
    # Inicializamos Beanie con la base de datos específica
    await init_beanie(
        database=client[settings.DB_NAME],
        document_models=[Category, Player]
    )