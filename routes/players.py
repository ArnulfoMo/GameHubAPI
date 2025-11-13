from fastapi import APIRouter, status
from models.players import Player


from controllers.players import (
    get_one
)

router = APIRouter(prefix="/players")

@router.get("/{id}", tags=["Players"], status_code=status.HTTP_200_OK)
async def get_one_player( id:int ):
    result: Player = await get_one(id)
    return result
