from fastapi import HTTPException
from beanie import PydanticObjectId
from app.models.category import Category
from app.models.player import Player
from app.schemas.player import PlayerCreate

class PlayerService:
    
    @staticmethod
    async def create_player(data: PlayerCreate) -> Player:
        # 1. Buscar Categoría
        try:
            cat_id = PydanticObjectId(data.categoria_id)
            category = await Category.get(cat_id)
        except:
            raise HTTPException(status_code=400, detail="ID de categoría inválido")

        if not category:
            raise HTTPException(status_code=404, detail="Categoría no encontrada")

        # 2. VALIDACIÓN DE NEGOCIO: Rango de edad
        anio_nacimiento = data.fecha_nacimiento.year
        if not (category.anio_min <= anio_nacimiento <= category.anio_max):
            raise HTTPException(
                status_code=400,
                detail=f"Edad inválida: Jugador nacido en {anio_nacimiento} no aplica para {category.nombre} ({category.anio_min}-{category.anio_max})"
            )

        # 3. Crear Jugador
        new_player = Player(
            nombre_completo=data.nombre_completo,
            fecha_nacimiento=data.fecha_nacimiento,
            numero_playera=data.numero_playera,
            posiciones=data.posiciones,
            categoria_id=category.id
        )
        await new_player.insert()
        return new_player

    @staticmethod
    async def get_by_category(category_id: str) -> list[Player]:
        try:
            oid = PydanticObjectId(category_id)
            return await Player.find(Player.categoria_id == oid).to_list()
        except:
            return []