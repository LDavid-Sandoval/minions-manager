from pydantic import BaseModel, Field
from beanie import PydanticObjectId

class CategoryCreate(BaseModel):
    nombre: str
    alias: str
    anio_min: int
    anio_max: int

class CategoryResponse(CategoryCreate):
    # CAMBIO AQUÍ: Quitamos Field(alias="_id") y dejamos solo el tipo
    id: PydanticObjectId