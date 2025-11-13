from datetime import datetime
import json
import logging

from fastapi import HTTPException

from models.players import Player
from utils.database import execute_query_json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def get_one( id:int ) -> Player:

    selectscript = """
        SELECT [id]
            ,[firstname]
            ,[lastname]
            ,[nickname]
            ,[email]
            ,[birth_date]
        FROM [gamehub].[players]
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