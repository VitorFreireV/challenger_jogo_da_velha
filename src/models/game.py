import numpy as np


class Game:
    def __init__(self, size=3):
        self.size = size
        self.board = np.zeros([size, size])
        self.player_turn = None
        self.status_game = "Em andamento"
        self.play_history = []

    def restart(self):
        self.board = np.zeros([self.size, self.size])
        self.player_turn = None
        self.status = "Em andamento"
        self.play_history = []

    def calculate_status(self):
        # calculate actual state, check rows, columns and diagonal
        points = 0
        for i in range(self.size):
            # check row
            points = sum(self.board[:, i])
            if abs(points) == self.size:
                break
            # check column
            points = sum(self.board[i, :])
            if abs(points) == self.size:
                break

        if abs(points) < self.size:
            # check diagonals
            points = sum(self.board.diagonal())
            if abs(points) != self.size:
                points = sum(np.flipud(self.board).diagonal())

        if points == self.size:
            self.status = f"Vitoria de {self.player_turn}"
        else:
            if np.any(self.board == 0):
                self.status = "Em andamento"
            else:
                self.status = "Empate"

    def get_status(self):
        self.calculate_status()
        return {"status": self.status, "jogadas": self.play_history}

    def validate_and_execute_play(self, play):
        pass

    def update_status_game(self):
        pass
