'''
This file contains the Piece class which represents a Tetris piece.
'''
class Piece:
    def __init__(self, shape):
        self.shape = shape
    def rotate(self):
        # Rotate the piece
        self.shape = list(zip(*self.shape[::-1]))
    def get_shape(self):
        return self.shape