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

    started_at: Optional[datetime] = Field(
        default=None,
        description="Fecha y hora en que el jugador inició el juego.",
        examples=["2025-02-01T14:30:00"]
    )

    last_played_at: Optional[datetime] = Field(
        default=None,
        description="Fecha y hora de la última sesión del jugador.",
        examples=["2025-03-10T22:15:00"]
    )

    hours_played: Optional[float] = Field(
        default=0.0,
        description="Horas jugadas acumuladas por el jugador para este juego. Debe ser mayor o igual a 0.",
        ge=0,
        examples=[0.0, 12.75, 150.5]
    )
