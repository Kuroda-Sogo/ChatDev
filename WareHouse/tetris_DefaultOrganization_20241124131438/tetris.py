'''
This file contains the Tetris class which represents the game logic.
'''
import random
import tkinter as tk
from piece import Piece
class Tetris:
    def __init__(self, root):
        self.root = root
        self.root.title("Tetris")
        self.canvas = tk.Canvas(self.root, width=300, height=600, bg="white")
        self.canvas.pack()
        self.board = [[0] * 10 for _ in range(20)]
        self.current_piece = None
        self.score = 0
        self.draw_board()
        self.root.bind("<Key>", self.handle_keypress)
        self.start_game()
    def draw_board(self):
        self.canvas.delete("all")
        for row in range(20):
            for col in range(10):
                if self.board[row][col] == 1:
                    self.canvas.create_rectangle(col * 30, row * 30, (col + 1) * 30, (row + 1) * 30, fill="blue")
    def start_game(self):
        self.current_piece = self.get_random_piece()
        self.draw_piece()
        self.root.after(1000, self.move_piece_down)
    def get_random_piece(self):
        # Return a random Tetris piece
        pieces = [
            [[1, 1, 1, 1]],
            [[1, 1], [1, 1]],
            [[1, 1, 0], [0, 1, 1]],
            [[0, 1, 1], [1, 1, 0]],
            [[1, 1, 1], [0, 1, 0]],
            [[1, 1, 1], [1, 0, 0]],
            [[1, 1, 1], [0, 0, 1]]
        ]
        return Piece(random.choice(pieces))
    def draw_piece(self):
        for row in range(len(self.current_piece.get_shape())):
            for col in range(len(self.current_piece.get_shape()[0])):
                if self.current_piece.get_shape()[row][col] == 1:
                    self.canvas.create_rectangle((col + 4) * 30, (row + 1) * 30, (col + 5) * 30, (row + 2) * 30, fill="blue")
    def move_piece_down(self):
        if self.check_collision():
            self.merge_piece()
            self.clear_lines()
            if self.check_game_over():
                self.game_over()
            else:
                self.current_piece = self.get_random_piece()
        else:
            self.clear_piece()
            for row in range(len(self.current_piece.get_shape())):
                for col in range(len(self.current_piece.get_shape()[0])):
                    if self.current_piece.get_shape()[row][col] == 1:
                        self.current_piece.get_shape()[row][col] = 0
                        self.current_piece.get_shape()[row + 1][col] = 1
            self.draw_piece()
            self.root.after(1000, self.move_piece_down)
    def handle_keypress(self, event):
        if event.keysym == "Left":
            self.move_piece_left()
        elif event.keysym == "Right":
            self.move_piece_right()
        elif event.keysym == "Down":
            self.move_piece_down()
    def move_piece_left(self):
        if not self.check_collision_left():
            self.clear_piece()
            for row in range(len(self.current_piece.get_shape())):
                for col in range(len(self.current_piece.get_shape()[0])):
                    if self.current_piece.get_shape()[row][col] == 1:
                        self.current_piece.get_shape()[row][col] = 0
                        self.current_piece.get_shape()[row][col - 1] = 1
            self.draw_piece()
    def move_piece_right(self):
        if not self.check_collision_right():
            self.clear_piece()
            for row in range(len(self.current_piece.get_shape())):
                for col in range(len(self.current_piece.get_shape()[0])):
                    if self.current_piece.get_shape()[row][col] == 1:
                        self.current_piece.get_shape()[row][col] = 0
                        self.current_piece.get_shape()[row][col + 1] = 1
            self.draw_piece()
    def check_collision(self):
        for row in range(len(self.current_piece.get_shape())):
            for col in range(len(self.current_piece.get_shape()[0])):
                if self.current_piece.get_shape()[row][col] == 1:
                    if row + 1 >= len(self.board) or self.board[row + 1][col] == 1:
                        return True
        return False
    def check_collision_left(self):
        for row in range(len(self.current_piece.get_shape())):
            for col in range(len(self.current_piece.get_shape()[0])):
                if self.current_piece.get_shape()[row][col] == 1:
                    if col - 1 < 0 or self.board[row][col - 1] == 1:
                        return True
        return False
    def check_collision_right(self):
        for row in range(len(self.current_piece.get_shape())):
            for col in range(len(self.current_piece.get_shape()[0])):
                if self.current_piece.get_shape()[row][col] == 1:
                    if col + 1 >= len(self.board[0]) or self.board[row][col + 1] == 1:
                        return True
        return False
    def merge_piece(self):
        for row in range(len(self.current_piece.get_shape())):
            for col in range(len(self.current_piece.get_shape()[0])):
                if self.current_piece.get_shape()[row][col] == 1:
                    self.board[row][col + 4] = 1
    def clear_piece(self):
        for row in range(len(self.current_piece.get_shape())):
            for col in range(len(self.current_piece.get_shape()[0])):
                if self.current_piece.get_shape()[row][col] == 1:
                    self.canvas.create_rectangle((col + 4) * 30, (row + 1) * 30, (col + 5) * 30, (row + 2) * 30, fill="white")
    def clear_lines(self):
        lines_cleared = 0
        for row in range(len(self.board)):
            if all(cell == 1 for cell in self.board[row]):
                self.board.pop(row)
                self.board.insert(0, [0] * 10)
                lines_cleared += 1
        self.score += lines_cleared * 100
    def check_game_over(self):
        for col in range(len(self.board[0])):
            if self.board[0][col] == 1:
                return True
        return False
    def game_over(self):
        self.canvas.create_text(150, 300, text="Game Over", font=("Arial", 36), fill="red")
        self.canvas.create_text(150, 350, text=f"Score: {self.score}", font=("Arial", 24), fill="red")