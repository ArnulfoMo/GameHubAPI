from datetime import datetime
import json
import logging

from fastapi import HTTPException

from models.games import Game
from utils.database import execute_query_json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def get_one( id:int ) -> Game:

    selectscript = """
        SELECT [id]
            ,[categories_id]
            ,[title]
            ,[release_date]
        FROM [gamehub].[games]
        WHERE [id] = ?;
    """

    params = [id]
    result_dict = []

    try:
        result = await execute_query_json(selectscript, params=params)
        result_dict = json.loads(result)

        #Validacion de elemento vacio
        if len(result_dict) > 0:
            return result_dict[0]
        else:
            return []

    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Database error { str(e) }")
    
async def get_all() -> list[Game]:

    selectscript = """
        SELECT [id]
            ,[categories_id]
            ,[title]
            ,[release_date]
        FROM [gamehub].[games]
    """

    result_dict = []

    try:
        result = await execute_query_json(selectscript)
        result_dict = json.loads(result)
        return result_dict

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")
    
async def create_game( game: Game ) -> Game:
    
    createscript = """
        INSERT INTO [gamehub].[games] ( [categories_id] ,[title] ,[release_date]) 
        VALUES ( ?, ?, ?);
    """

    params = (
        game.categories_id
        , game.title
        , game.release_date
    )

    insert_result = None

    try:
        insert_result = await execute_query_json( createscript, params, needs_commit=True )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")
    
    sqlfind: str = """
        SELECT [id]
            ,[categories_id]
            ,[title]
            ,[release_date]
        FROM [gamehub].[games]
        WHERE [id] = ?;
    """

    params = [game.id]

    try:
        result = await execute_query_json(sqlfind, params=params)
        result_dict = json.loads(result)

        #Validacion de elemento vacio
        if len(result_dict) > 0:
            return result_dict[0]
        else:
            return []

    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Database error { str(e) }")

async def update_game( game:Game ) -> Game:

    dict = game.model_dump(exclude_none=True)

    keys = [ k for k in  dict.keys() ]
    keys.remove('id')
    variables = " = ?, ".join(keys)+" = ?"

    updatescript = f"""
        UPDATE [gamehub].[games]
        SET {variables}
        WHERE [id] = ?;
    """

    params = [ dict[v] for v in keys ]
    params.append( game.id )

    update_result = None
    try:
        update_result = await execute_query_json( updatescript, params, needs_commit=True )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")

    sqlfind: str = """
        SELECT [id]
            ,[categories_id]
            ,[title]
            ,[release_date]
        FROM [gamehub].[games]
        WHERE [id] = ?;
    """

    params = [game.id]

    result_dict=[]
    try:
        result = await execute_query_json(sqlfind, params=params)
        result_dict = json.loads(result)

        if len(result_dict) > 0:
            return result_dict[0]
        else:
            return []
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")

async def delete_game( id:int ) -> str:

    deletescript = """
        DELETE FROM [gamehub].[games]
        WHERE [id] = ?
    """

    params = [id]

    try:
        await execute_query_json(deletescript, params=params, needs_commit=True)
        return "DELETED"
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")