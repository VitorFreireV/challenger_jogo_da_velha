import numpy as np


class Game:
    def __init__(self, size=3):
        self.size = size
        self.board = np.zeros([size, size])
        self.status = "Em andamento"
        self.player_turn = None
        self.play_history = []

    def restart(self):
        self.board = np.zeros([self.size, self.size])
        self.status = "Em andamento"
        self.play_history = []
        self.player_turn = None

    def calculate_status_by_play(self, play):
        # calculate actual state, check rows, columns and diagonal
        if abs(sum(self.board[:, play["y"]])) == self.size:
            self.status = f"Vitoria de {self.play['player']}"
            return

        if abs(sum(self.board[play["x"], :])) == self.size:
            self.status = f"Vitoria de {self.play['player']}"
            return

        if sum(self.board.diagonal()) == self.size:
            self.status = f"Vitoria de {self.play['player']}"
            return

        if sum(np.flipud(self.board).diagonal()) == self.size:
            self.status = f"Vitoria de {self.play['player']}"
            return

        if not np.any(self.board == 0):
            self.status = "Empate"
            return

    def get_status(self):
        return {"status": self.status, "jogadas": self.play_history}

    def validate_and_execute_play(self, play):
        if self.player_turn == play["player"]:
            return {
                "message": f"Invalid play. Two consecutive moves by the same player are not allowed, player '{'X' if self.player_turn == 'O' else 'O'}' is expected to move."
            }
        if self.board[play["x"] - 1, play["y"] - 1] != 0:
            return {
                "message": f"Invalid play. Position P{str(play['x']) + str(play['y'])} has already been filled."
            }

        self.play_history.append(
            {"jogador": play["player"], "posicao": f"P{play['x']}{play['y']}"}
        )
        self.player_turn = play["player"]
        self.board[play["x"] - 1, play["y"] - 1] = -1 if play["player"] == "X" else -2
        self.calculate_status_by_play(play)
        return True
