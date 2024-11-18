'''
This file contains the Tetris class which represents the game logic.
'''
import random
import tkinter as tk
from tetromino import Tetromino
class Tetris:
    def __init__(self, root):
        self.root = root
        self.root.title("Tetris")
        self.canvas = tk.Canvas(self.root, width=300, height=600, bg="black")
        self.canvas.pack()
        self.board = [[0] * 10 for _ in range(20)]
        self.current_piece = None
        self.next_piece = None
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.is_game_over = False
        self.draw_board()
    def start(self):
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Up>", self.rotate_piece)
        self.next_piece = self.generate_piece()  # Initialize the next_piece
        self.update()  # Start the game loop
    def draw_board(self):
        self.canvas.delete("all")
        for row in range(20):
            for col in range(10):
                if self.board[row][col] == 1:
                    self.canvas.create_rectangle(col * 30, row * 30, (col + 1) * 30, (row + 1) * 30, fill="blue")
    def update(self):
        if not self.is_game_over:
            if self.current_piece is None:
                self.current_piece = self.next_piece
                self.next_piece = self.generate_piece()
                if self.check_collision(self.current_piece):
                    self.is_game_over = True
                    self.canvas.create_text(150, 300, text="Game Over", font=("Arial", 36), fill="white")
                else:
                    self.draw_piece(self.current_piece)
            else:
                self.move_down()
        self.root.after(1000 // self.level, self.update)
    def move_left(self, event):
        if not self.is_game_over and self.current_piece is not None:
            self.erase_piece(self.current_piece)
            self.current_piece.move_left()
            if self.check_collision(self.current_piece):
                self.current_piece.move_right()
            self.draw_piece(self.current_piece)
    def move_right(self, event):
        if not self.is_game_over and self.current_piece is not None:
            self.erase_piece(self.current_piece)
            self.current_piece.move_right()
            if self.check_collision(self.current_piece):
                self.current_piece.move_left()
            self.draw_piece(self.current_piece)
    def move_down(self, event=None):
        if not self.is_game_over and self.current_piece is not None:
            self.erase_piece(self.current_piece)
            self.current_piece.move_down()
            if self.check_collision(self.current_piece):
                self.current_piece.move_up()
                self.lock_piece()
                self.clear_lines()
                self.current_piece = None
            self.draw_piece(self.current_piece)
    def rotate_piece(self, event):
        if not self.is_game_over and self.current_piece is not None:
            self.erase_piece(self.current_piece)
            self.current_piece.rotate()
            if self.check_collision(self.current_piece):
                self.current_piece.rotate_back()
            self.draw_piece(self.current_piece)
    def generate_piece(self):
        shapes = [
            [[1, 1, 1, 1]],
            [[1, 1], [1, 1]],
            [[1, 1, 0], [0, 1, 1]],
            [[0, 1, 1], [1, 1, 0]],
            [[1, 1, 1], [0, 1, 0]],
            [[1, 1, 1], [1, 0, 0]],
            [[1, 1, 1], [0, 0, 1]]
        ]
        shape = random.choice(shapes)
        x = 4
        y = 0
        return Tetromino(shape, x, y)
    def draw_piece(self, piece):
        for row in range(len(piece.shape)):
            for col in range(len(piece.shape[row])):
                if piece.shape[row][col] == 1:
                    x = (piece.x + col) * 30
                    y = (piece.y + row) * 30
                    self.canvas.create_rectangle(x, y, x + 30, y + 30, fill="blue")
    def erase_piece(self, piece):
        for row in range(len(piece.shape)):
            for col in range(len(piece.shape[row])):
                if piece.shape[row][col] == 1:
                    x = (piece.x + col) * 30
                    y = (piece.y + row) * 30
                    self.canvas.create_rectangle(x, y, x + 30, y + 30, fill="black")
    def check_collision(self, piece):
        if piece is None:
            return False
        for row in range(len(piece.shape)):
            for col in range(len(piece.shape[row])):
                if piece.shape[row][col] == 1:
                    x = piece.x + col
                    y = piece.y + row
                    if x < 0 or x >= 10 or y >= 20 or self.board[y][x] == 1:
                        return True
        return False
    def lock_piece(self):
        for row in range(len(self.current_piece.shape)):
            for col in range(len(self.current_piece.shape[row])):
                if self.current_piece.shape[row][col] == 1:
                    x = self.current_piece.x + col
                    y = self.current_piece.y + row
                    self.board[y][x] = 1
    def clear_lines(self):
        lines_to_clear = []
        for row in range(len(self.board)):
            if all(self.board[row]):
                lines_to_clear.append(row)
        for row in lines_to_clear:
            del self.board[row]
            self.board.insert(0, [0] * 10)
        self.score += len(lines_to_clear) * 100
        self.lines_cleared += len(lines_to_clear)
        self.level = 1 + self.lines_cleared // 10