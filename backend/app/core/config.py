from pydantic_settings import BaseSettings
from urllib.parse import quote_plus

class Settings(BaseSettings):
    # 1. Definimos las variables individuales que leerá del .env
    MONGO_USER: str
    MONGO_PASSWORD: str
    MONGO_HOST: str
    DB_NAME: str
    
    PROJECT_NAME: str = "Minions API"
    API_VERSION: str = "v1"

    # 2. Creamos la propiedad que construye la URL automáticamente
    @property
    def MONGO_URL(self) -> str:
        # Codificamos usuario y contraseña para evitar errores con símbolos especiales (@, :)
        user = quote_plus(self.MONGO_USER)
        password = quote_plus(self.MONGO_PASSWORD)
        
        # Construimos el string final
        return (
            f"mongodb+srv://{user}:{password}@{self.MONGO_HOST}"
            f"/?retryWrites=true&w=majority&appName=MinionsManager"
        )

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

# Instanciamos la configuración
settings = Settings()