from fastapi import APIRouter, status

from models.players import Player
from models.players_games import PlayerGame

from controllers.players import (
    get_one
    , get_all
    , create_player
    , update_player
    , delete_player
    #PLAYER_GAMES
    , get_one_game
    , get_all_games
    , add_game
    , remove_game
)


router = APIRouter(prefix="/players")

# ============================================================
#                    MAIN CRUD FOR PLAYERS
# ============================================================

@router.get("/{id}", tags=["Players"], status_code=status.HTTP_200_OK)
async def get_one_player( id:int ):
    result: Player = await get_one(id)
    return result

@router.get( "/", tags=["Players"], status_code=status.HTTP_200_OK)
async def get_all_players():
    result = await get_all()
    return result

@router.post( "/", tags=["Players"], status_code=status.HTTP_201_CREATED)
async def create_new_player(player_data: Player):
    result = await create_player(player_data)
    return result

@router.put("/{id}", tags=["Players"], status_code=status.HTTP_201_CREATED)
async def update_player_information( id:int, player_data:Player ):
    player_data.id = id
    result = await update_player(player_data)
    return result

@router.delete("/{id}", tags=["Players"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_player_content( id:int ):
    status: str = await delete_player(id)
    return status

# ============================================================
#          PLAYER → GAMES RELATION (players_games)
# ============================================================

@router.get("/{id}/games/{game_id}", tags=["Players"], status_code=status.HTTP_200_OK)
async def get_one_game_of_player( id:int, game_id:int ):
    result = await get_one_game(id, game_id)
    return result

@router.get( "/{id}/games", tags=["Players"], status_code=status.HTTP_200_OK)
async def get_all_games_of_player( id:int ):
    result = await get_all_games(id)
    return result

@router.post( "/{id}/games", tags=["Players"], status_code=status.HTTP_201_CREATED)
async def assing_game_to_player( id:int, game_data: PlayerGame ):
    result = await add_game(id, game_data.game_id)
    return result

@router.delete("/{id}/games/{game_id}", tags=["Players"], status_code=status.HTTP_204_NO_CONTENT)
async def remove_game_of_player( id:int, game_id:int ):
    status: str = await remove_game( id, game_id)
    return status