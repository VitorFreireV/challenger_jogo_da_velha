from fastapi import FastAPI
from src.api_v1 import game

app = FastAPI(title="Jogo da Velha")

app.include_router(game.router, tags=["Jogo da Velha"])
