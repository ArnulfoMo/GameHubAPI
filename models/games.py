from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class Game(BaseModel):
    id: Optional[int] = Field(
        default=None,
        description="ID autoincrementable del juego."
    )

    categories_id: Optional[int] = Field(
        default=None,
        description="ID de la categoría asociada al juego (FK).",
        examples=[1, 2, 3]
    )

    title: Optional[str] = Field(
        default=None,
        description="Título del juego.",
        pattern=r"^[\w' :\-!?,.&()]+$",
        examples=["Halo Infinite", "Super Mario Odyssey"]
    )

    release_date: Optional[date] = Field(   
        default=None,
        description="Fecha de lanzamiento del juego.",
        examples=["2021-11-15", "2017-10-27"]
    )
