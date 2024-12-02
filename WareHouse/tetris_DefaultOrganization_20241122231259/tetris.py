'''
This file contains the Tetris class which represents the game logic and GUI.
'''
import tkinter as tk
import random
class Tetris:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=300, height=600, bg="white")
        self.canvas.pack()
        self.board = [[0] * 10 for _ in range(20)]
        self.current_piece = None
        self.current_piece_x = 0
        self.current_piece_y = 0
        self.score = 0
        self.draw_board()
    def draw_board(self):
        self.canvas.delete("all")
        for row in range(20):
            for col in range(10):
                if self.board[row][col] == 1:
                    self.canvas.create_rectangle(col * 30, row * 30, (col + 1) * 30, (row + 1) * 30, fill="blue")
    def start_game(self):
        self.current_piece = self.get_random_piece()
        self.current_piece_x = 4
        self.current_piece_y = 0
        self.draw_piece()
    def draw_piece(self):
        for row in range(len(self.current_piece)):
            for col in range(len(self.current_piece[0])):
                if self.current_piece[row][col] == 1:
                    self.canvas.create_rectangle((col + self.current_piece_x) * 30, (row + self.current_piece_y) * 30,
                                                 (col + self.current_piece_x + 1) * 30, (row + self.current_piece_y + 1) * 30,
                                                 fill="blue")
    def get_random_piece(self):
        pieces = [
            [[1, 1, 1, 1]],
            [[1, 1], [1, 1]],
            [[1, 1, 0], [0, 1, 1]],
            [[0, 1, 1], [1, 1, 0]],
            [[1, 1, 1], [0, 1, 0]],
            [[1, 1, 1], [1, 0, 0]],
            [[1, 1, 1], [0, 0, 1]]
        ]
        return random.choice(pieces)
    def move_piece(self, direction):
        if direction == "left":
            self.current_piece_x -= 1
        elif direction == "right":
            self.current_piece_x += 1
        elif direction == "down":
            self.current_piece_y += 1
        if self.check_collision():
            if direction == "left":
                self.current_piece_x += 1
            elif direction == "right":
                self.current_piece_x -= 1
            elif direction == "down":
                self.current_piece_y -= 1
        self.draw_board()
        self.draw_piece()
    def rotate_piece(self):
        rotated_piece = list(zip(*self.current_piece[::-1]))
        if self.check_collision(rotated_piece):
            return
        self.current_piece = rotated_piece
        self.draw_board()
        self.draw_piece()
    def check_collision(self, piece=None):
        if piece is None:
            piece = self.current_piece
        for row in range(len(piece)):
            for col in range(len(piece[0])):
                if piece[row][col] == 1:
                    if (
                        self.current_piece_x + col < 0
                        or self.current_piece_x + col >= 10
                        or self.current_piece_y + row >= 20
                        or self.board[self.current_piece_y + row][self.current_piece_x + col] == 1
                    ):
                        return True
        return False
    def update_board(self):
        for row in range(len(self.current_piece)):
            for col in range(len(self.current_piece[0])):
                if self.current_piece[row][col] == 1:
                    self.board[self.current_piece_y + row][self.current_piece_x + col] = 1
        self.clear_lines()
        self.start_game()
    def clear_lines(self):
        lines_cleared = 0
        for row in range(len(self.board)):
            if all(cell == 1 for cell in self.board[row]):
                self.board.pop(row)
                self.board.insert(0, [0] * 10)
                lines_cleared += 1
        self.score += lines_cleared * 100
        if self.check_collision():
            self.game_over()
    def game_over(self):
        self.canvas.create_text(150, 300, text="Game Over", font=("Arial", 36), fill="red")
        self.canvas.create_text(150, 350, text=f"Score: {self.score}", font=("Arial", 24), fill="red")