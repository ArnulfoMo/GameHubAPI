from pydantic import BaseModel, Field
from typing import Optional

class GamePlatform(BaseModel):
    games_id: Optional[int] = Field(
        default=None,
        description="ID del juego (FK a games).",
        examples=[1, 5, 12]
    )

    platforms_id: Optional[int] = Field(
        default=None,
        description="ID de la plataforma (FK a platforms).",
        examples=[2, 8, 15]
    )

    active: Optional[bool] = Field(
        default=True,
        description="Indica si la edición del juego en esta plataforma está activa.",
        examples=[True, False]
    )
