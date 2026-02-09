from fastapi import APIRouter
from typing import List
from app.schemas.player import PlayerCreate, PlayerResponse
from app.services.player_service import PlayerService

router = APIRouter(prefix="/jugadores", tags=["Jugadores"])

@router.post("/", response_model=PlayerResponse)
async def register_player(player_data: PlayerCreate):
    return await PlayerService.create_player(player_data)

@router.get("/{category_id}", response_model=List[PlayerResponse])
async def get_players_by_category(category_id: str):
    return await PlayerService.get_by_category(category_id)