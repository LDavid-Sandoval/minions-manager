from beanie import Document
from pydantic import Field

class Category(Document):
    nombre: str = Field(..., description="Nombre de la categoría (ej: Sub 15)")
    alias: str = Field(..., description="Alias o Generación (ej: 2010-2011)")
    anio_min: int
    anio_max: int

    class Settings:
        name = "categorias" # Nombre de la colección en Mongo