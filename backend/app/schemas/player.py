from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date
from beanie import PydanticObjectId

class PlayerCreate(BaseModel):
    nombre_completo: str
    fecha_nacimiento: date
    numero_playera: int
    posiciones: List[str]
    categoria_id: str

class PlayerResponse(BaseModel):
    # CAMBIO AQUÍ: Usamos id directo sin alias
    id: PydanticObjectId 
    nombre_completo: str
    fecha_nacimiento: date
    numero_playera: int
    posiciones: List[str]
    categoria_id: PydanticObjectId