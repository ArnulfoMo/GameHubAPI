from fastapi import APIRouter, status
from models.games import Game

from controllers.games import (
    get_one
    , get_all
    , create_game
    , update_game
    , delete_game
)

router = APIRouter(prefix="/games")

@router.get("/{id}", tags=["Games"], status_code=status.HTTP_200_OK)
async def get_one_game( id:int ):
    result: Game = await get_one(id)
    return result

@router.get( "/", tags=["Games"], status_code=status.HTTP_200_OK)
async def get_all_games():
    result = await get_all()
    return result

@router.post( "/", tags=["Games"], status_code=status.HTTP_201_CREATED)
async def create_new_game(game_data: Game):
    result = await create_game(game_data)
    return result

@router.put("/{id}", tags=["Games"], status_code=status.HTTP_201_CREATED)
async def update_game_information( id:int, game_data:Game ):
    game_data.id = id
    result = await update_game(game_data)
    return result

@router.delete("/{id}", tags=["Games"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_game_information( id:int ):
    status: str = await delete_game(id)
    return status




