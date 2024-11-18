'''
This file contains the Tetromino class which represents a single Tetromino piece.
'''
import tkinter as tk
class Tetromino:
    def __init__(self, shape, x, y):
        self.shape = shape
        self.x = x
        self.y = y
        self.rotation = 0
    def move_left(self):
        self.x -= 1
    def move_right(self):
        self.x += 1
    def move_down(self):
        self.y += 1
    def move_up(self):
        self.y -= 1
    def rotate(self):
        self.rotation = (self.rotation + 1) % 4
    def rotate_back(self):
        self.rotation = (self.rotation - 1) % 4