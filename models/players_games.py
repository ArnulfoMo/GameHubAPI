from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class PlayerGame(BaseModel):
    player_id: Optional[int] = Field(
        default=None,
        description="ID del jugador (FK a players).",
        examples=[1, 5, 12]
    )

    game_id: Optional[int] = Field(
        default=None,
        description="ID del juego (FK a games).",
        examples=[10, 22, 7]
    )

    registered_date: Optional[datetime] = Field(
        default=None,
        description="Fecha y hora en que el jugador adquirio el juego.",
        examples=["2025-02-01T14:30:00"]
    )

