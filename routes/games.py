from fastapi import APIRouter, status
from models.games import Game
from models.games_platforms import GamePlatform

from controllers.games import (
    get_one
    , get_all
    , create_game
    , update_game
    , delete_game
    # players_games
    , get_all_players
    # games_platforms
    , get_one_platform
    , get_all_platforms
    , add_platform
    , update_platform_info
    , remove_platform
)

router = APIRouter(prefix="/games")

# ============================================================
#                    MAIN CRUD FOR GAMES
# ============================================================

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

# ============================================================
#             GAME → PLAYERS RELATION (players_games)
# ============================================================

@router.get( "/{id}/players", tags=["Games"], status_code=status.HTTP_200_OK)
async def get_all_players_of_game( id:int ):
    result = await get_all_players(id)
    return result

# ============================================================
#            GAME → PLATFORMS RELATION (games_platforms)
# ============================================================

@router.get("/{id}/platforms/{platforms_id}", tags=["Games"], status_code=status.HTTP_200_OK)
async def get_one_platform_of_game( id:int, platforms_id:int ):
    result = await get_one_platform(id, platforms_id)
    return result

@router.get( "/{id}/platforms", tags=["Games"], status_code=status.HTTP_200_OK)
async def get_all_platforms_of_game( id:int ):
    result = await get_all_platforms(id)
    return result

@router.post( "/{id}/platforms", tags=["Games"], status_code=status.HTTP_201_CREATED)
async def assing_platform_to_game( id:int, platform_data: GamePlatform ):
    result = await add_platform(id, platform_data.platforms_id)
    return result

@router.delete("/{id}/platforms/{platforms_id}", tags=["Games"], status_code=status.HTTP_204_NO_CONTENT)
async def remove_platform_of_game( id:int, platforms_id:int ):
    status: str = await remove_platform( id, platforms_id)
    return status

@router.put("/{id}/platforms/{platforms_id}", tags=["Games"], status_code=status.HTTP_201_CREATED)
async def update_platform_of_game( id: int, platforms_id: int, platform_data: GamePlatform ):
    platform_data.games_id = id
    platform_data.platforms_id = platforms_id
    result = await update_platform_info(platform_data)
    return result