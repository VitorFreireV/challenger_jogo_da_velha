from pydantic import BaseModel
import enum


class PlayerOpt(str, enum.Enum):
    X = "X"
    O = "O"


class PositionOpt(str, enum.Enum):
    P11 = "P11"
    P12 = "P12"
    P13 = "P13"
    P21 = "P21"
    P22 = "P22"
    P23 = "P23"
    P31 = "P31"
    P32 = "P32"
    P33 = "P33"


class Play(BaseModel):
    jogador: PlayerOpt
    posicao: PositionOpt
