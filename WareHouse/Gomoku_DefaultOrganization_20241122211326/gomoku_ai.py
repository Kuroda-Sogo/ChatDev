'''
This file contains the AI player for the Gomoku game.
'''
import random
class GomokuAI:
    def __init__(self, board_size):
        self.board_size = board_size
    def make_move(self, board):
        while True:
            row = random.randint(0, self.board_size - 1)
            col = random.randint(0, self.board_size - 1)
            if board[row][col] == '':
                return row, col