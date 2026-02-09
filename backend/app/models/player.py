from typing import List, Optional
from datetime import date
from beanie import Document, PydanticObjectId
from pydantic import Field

class Player(Document):
    nombre_completo: str
    fecha_nacimiento: date
    numero_playera: int
    posiciones: List[str]
    categoria_id: PydanticObjectId  # Referencia al ID de la categoría
    foto_url: Optional[str] = None

    class Settings:
        name = "jugadores"