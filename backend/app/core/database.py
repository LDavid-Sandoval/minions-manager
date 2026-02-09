from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.core.config import settings
from app.models.category import Category
from app.models.player import Player

async def init_db():
    client = AsyncIOMotorClient(settings.MONGO_URL)
    await init_beanie(
        database=client[settings.DB_NAME],
        document_models=[Category, Player]
    )