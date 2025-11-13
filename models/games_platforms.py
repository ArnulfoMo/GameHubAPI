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

    edition: Optional[str] = Field(
        default=None,
        description="Edición específica del juego para esta plataforma.",
        pattern=r"^[A-Za-z0-9ÁÉÍÓÚÜÑáéíóúüñ' \-]+$",
        examples=["Standard Edition", "Deluxe Edition", "Ultimate Edition"]
    )

    active: Optional[bool] = Field(
        default=True,
        description="Indica si la edición del juego en esta plataforma está activa.",
        examples=[True, False]
    )
