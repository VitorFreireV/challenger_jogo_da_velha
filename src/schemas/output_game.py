from pydantic import BaseModel
from src.schemas.input_game import Play
from typing import List


class GameStatus(BaseModel):
    play_history: List[Play]
    status: str


class MessageModel(BaseModel):
    message: str
