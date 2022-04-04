from fastapi.routing import APIRouter
from src.schemas import input_game, output_game
from src.models.game import Game

router = APIRouter()


game = Game()


@router.get(
    "/status",
    responses={
        200: {
            "model": output_game.GameStatus,
            "description": "API was able to fetch the data",
        },
        500: {
            "model": output_game.MessageModel,
            "description": "Internal Error, it was not possible to recover the data",
        },
    },
)
async def status():
    try:
        return game.get_status()
    except:
        pass


@router.post(
    "/jogada",
    responses={
        200: {
            "model": output_game.Play,
            "description": "API was able to fetch the data",
        },
        409: {
            "model": output_game.MessageModel,
            "description": "Client error, invalid move",
        },
        500: {
            "model": output_game.MessageModel,
            "description": "Internal Error, it was not possible to recover the data",
        },
    },
)
async def jogada(play: input_game.Play):
    try:
        pass
    except:
        pass


@router.post(
    "/reiniciar",
    responses={
        200: {
            "model": output_game.MessageModel,
            "description": "API was able to fetch the data",
        },
        500: {
            "model": output_game.MessageModel,
            "description": "Internal Error, it was not possible to recover the data",
        },
    },
)
async def reniciar():
    try:
        pass
    except:
        pass
