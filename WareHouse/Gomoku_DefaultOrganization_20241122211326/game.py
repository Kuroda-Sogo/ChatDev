'''
This file contains the Game class which handles the game logic.
'''
class Game:
    def __init__(self):
        self.board = [['' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
    def make_move(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            return True
        return False
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    def check_winner(self):
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        for row in range(15):
            for col in range(15):
                if self.board[row][col] == self.current_player:
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
    def is_board_full(self):
        for row in self.board:
            if '' in row:
                return False
        return True
    def reset(self):
        self.board = [['' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'