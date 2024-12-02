'''
Tetris Board
'''
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0] * width for _ in range(height)]
    def is_valid_position(self, tetromino, x, y):
        shape = tetromino.shape
        for row in range(len(shape)):
            for col in range(len(shape[row])):
                if shape[row][col] != 0:
                    new_x = x + col
                    new_y = y + row
                    if (
                        new_x < 0
                        or new_x >= self.width
                        or new_y >= self.height
                        or self.grid[new_y][new_x] != 0
                    ):
                        return False
        return True
    def add_tetromino(self, tetromino, x, y):
        shape = tetromino.shape
        color = tetromino.color
        for row in range(len(shape)):
            for col in range(len(shape[row])):
                if shape[row][col] != 0:
                    new_x = x + col
                    new_y = y + row
                    self.grid[new_y][new_x] = color
    def remove_completed_rows(self):
        completed_rows = []
        for row in range(self.height):
            if all(cell != 0 for cell in self.grid[row]):
                completed_rows.append(row)
        for row in completed_rows:
            del self.grid[row]
            self.grid.insert(0, [0] * self.width)
    def is_game_over(self):
        return any(cell != 0 for cell in self.grid[0])