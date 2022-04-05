from fastapi.routing import APIRouter
from fastapi import Response
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
async def status(response: Response):
    try:
        return output_game.GameStatus(**game.get_status())
    except Exception as e:
        response.status_code = 500
        return {"message": f"Internal error! Error: {str(e)}"}


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
async def jogada(play: input_game.Play, response: Response):
    try:
        result = game.validate_and_execute_play(
            {
                "player": play.jogador,
                "x": int(play.posicao.value[1]),
                "y": int(play.posicao.value[2]),
            }
        )
        if result == True:
            return output_game.Play(**play.dict())
        else:
            response.status_code = 409
            return output_game.MessageModel(**result)
    except Exception as e:
        return {"status_code": 500, "message": f"Internal error! Error: {str(e)}"}


@router.delete(
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
async def reniciar(response: Response):
    try:
        game.restart()
    except Exception as e:
        response.status_code = 500
        return {"message": f"Internal error! Error: {str(e)}"}
