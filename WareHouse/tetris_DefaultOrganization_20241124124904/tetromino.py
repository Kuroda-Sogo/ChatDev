'''
Tetrominoes
'''
class Tetromino:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.rotation = 0
    def rotate(self):
        self.rotation = (self.rotation + 1) % 4
        rotated_shape = list(zip(*reversed(self.shape)))
        self.shape = rotated_shape
    def move_left(self):
        self.x -= 1
    def move_right(self):
        self.x += 1
    def move_down(self):
        self.y += 1