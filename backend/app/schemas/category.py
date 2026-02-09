from pydantic import BaseModel, Field
from beanie import PydanticObjectId

class CategoryCreate(BaseModel):
    nombre: str
    alias: str
    anio_min: int
    anio_max: int

class CategoryResponse(CategoryCreate):
    id: PydanticObjectId = Field(alias="_id")