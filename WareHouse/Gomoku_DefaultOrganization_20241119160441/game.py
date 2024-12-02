'''
This file contains the Game class which manages the game logic.
'''
class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
    def make_move(self, row, col):
        if 0 <= row < 15 and 0 <= col < 15 and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    def check_winner(self, row, col):
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        for dx, dy in directions:
            count = 1
            for i in range(1, 5):
                new_row = row + dx * i
                new_col = col + dy * i
                if 0 <= new_row < 15 and 0 <= new_col < 15 and self.board[new_row][new_col] == self.current_player:
                    count += 1
                else:
                    break
            if count == 5:
                return True
        return False
    def reset(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'