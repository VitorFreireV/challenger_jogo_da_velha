import numpy as np


class Game:
    def __init__(self, row_size=3, column_size=3):
        self.row_size = row_size
        self.column_size = column_size
        self.board = np.zeros([column_size, row_size])
        self.player_turn = None
        self.status_game = "Em andamento"
        self.play_history = []

    def restart(self):
        self.board = np.zeros([self.column_size, self.row_size])
        self.player_turn = None
        self.status_game = "Em andamento"
        self.play_history = []

    def get_status(self):
        pass

    def validate_and_execute_play(self, play):
        pass

    def update_status_game(self):
        pass
