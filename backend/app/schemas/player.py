from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date
from beanie import PydanticObjectId

class PlayerCreate(BaseModel):
    nombre_completo: str
    fecha_nacimiento: date
    numero_playera: int
    posiciones: List[str]
    categoria_id: str  # Recibimos el ID como string desde el frontend

class PlayerResponse(BaseModel):
    id: PydanticObjectId = Field(alias="_id")
    nombre_completo: str
    fecha_nacimiento: date
    numero_playera: int
    posiciones: List[str]
    categoria_id: PydanticObjectId