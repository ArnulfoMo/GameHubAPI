from fastapi import APIRouter, status
from models.platforms import Platform


from controllers.platforms import (
    get_one
    , get_all
    , create_platform
    , update_platform
    , delete_platform
    #game_platform
    , get_all_games
)

router = APIRouter(prefix="/platforms")

@router.get("/{id}", tags=["Platforms"], status_code=status.HTTP_200_OK)
async def get_one_platform( id:int ):
    result: Platform = await get_one(id)
    return result

@router.get( "/", tags=["Platforms"], status_code=status.HTTP_200_OK)
async def get_all_platforms():
    result = await get_all()
    return result

@router.post( "/", tags=["Platforms"], status_code=status.HTTP_201_CREATED)
async def create_new_platfom(platform_data: Platform):
    result = await create_platform(platform_data)
    return result

@router.put("/{id}", tags=["Platforms"], status_code=status.HTTP_201_CREATED)
async def update_platform_information( id:int, platform_data:Platform ):
    platform_data.id = id
    result = await update_platform(platform_data)
    return result

@router.delete("/{id}", tags=["Platforms"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_platform_information( id:int ):
    status: str = await delete_platform(id)
    return status


### games_platforms ### interaction

@router.get( "/{platforms_id}/games", tags=["Platforms"], status_code=status.HTTP_200_OK)
async def get_all_games_of_platform( id:int ):
    result = await get_all_games(id)
    return result



