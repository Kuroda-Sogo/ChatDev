'''
Piece classes for Tetris game.
'''
class Piece:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.shape = [[0] * 4 for _ in range(4)]
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def rotate(self):
        self.shape = self.get_rotated_shape()
    def get_rotated_shape(self):
        n = len(self.shape)
        m = len(self.shape[0])
        rotated_shape = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                rotated_shape[j][n - i - 1] = self.shape[i][j]
        return rotated_shape
class I_Piece(Piece):
    def __init__(self):
        super().__init__()
        self.shape = [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
class J_Piece(Piece):
    def __init__(self):
        super().__init__()
        self.shape = [
            [1, 0, 0, 0],
            [1, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
class L_Piece(Piece):
    def __init__(self):
        super().__init__()
        self.shape = [
            [0, 0, 1, 0],
            [1, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
class O_Piece(Piece):
    def __init__(self):
        super().__init__()
        self.shape = [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
class S_Piece(Piece):
    def __init__(self):
        super().__init__()
        self.shape = [
            [0, 1, 1, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
class T_Piece(Piece):
    def __init__(self):
        super().__init__()
        self.shape = [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
class Z_Piece(Piece):
    def __init__(self):
        super().__init__()
        self.shape = [
            [1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]