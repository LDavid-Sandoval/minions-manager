from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Minions FC API"
    MONGO_URL: str = "mongodb://localhost:27017"
    DB_NAME: str = "minions_db"

    class Config:
        env_file = ".env"

settings = Settings()