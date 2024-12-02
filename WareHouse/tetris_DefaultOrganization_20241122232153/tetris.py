'''
This file contains the Tetris class which represents the game logic.
'''
import tkinter as tk
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
    def start(self):
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<space>", self.rotate_piece)
        self.root.after(1000, self.update)
    def draw_board(self):
        self.canvas.delete("all")
        for row in range(20):
            for col in range(10):
                if self.board[row][col] == 1:
                    self.canvas.create_rectangle(col * 30, row * 30, (col + 1) * 30, (row + 1) * 30, fill="blue")
    def update(self):
        self.move_down()
        self.draw_board()
        self.root.after(1000, self.update)
    def move_left(self, event=None):
        if self.current_piece:
            self.clear_piece()
            for row in range(len(self.current_piece)):
                for col in range(len(self.current_piece[row])):
                    if self.current_piece[row][col] == 1:
                        if col > 0 and self.board[self.current_piece_row + row][self.current_piece_col + col - 1] != 1:
                            self.current_piece[row][col] = 0
                            self.current_piece[row][col - 1] = 1
            self.draw_piece()
    def move_right(self, event=None):
        if self.current_piece:
            self.clear_piece()
            for row in range(len(self.current_piece)):
                for col in range(len(self.current_piece[row]) - 1, -1, -1):
                    if self.current_piece[row][col] == 1:
                        if col < len(self.current_piece[row]) - 1 and self.board[self.current_piece_row + row][self.current_piece_col + col + 1] != 1:
                            self.current_piece[row][col] = 0
                            self.current_piece[row][col + 1] = 1
            self.draw_piece()
    def move_down(self, event=None):
        if self.current_piece:
            self.clear_piece()
            for row in range(len(self.current_piece) - 1, -1, -1):
                for col in range(len(self.current_piece[row])):
                    if self.current_piece[row][col] == 1:
                        if row < len(self.current_piece) - 1 and self.board[self.current_piece_row + row + 1][self.current_piece_col + col] != 1:
                            self.current_piece[row][col] = 0
                            self.current_piece[row + 1][col] = 1
                        else:
                            self.lock_piece()
                            return
            self.draw_piece()
    def rotate_piece(self, event=None):
        if self.current_piece:
            self.clear_piece()
            rotated_piece = [[self.current_piece[col][row] for col in range(len(self.current_piece))] for row in range(len(self.current_piece[0]) - 1, -1, -1)]
            if self.is_valid_move(rotated_piece, self.current_piece_row, self.current_piece_col):
                self.current_piece = rotated_piece
            self.draw_piece()
    def clear_piece(self):
        for row in range(len(self.current_piece)):
            for col in range(len(self.current_piece[row])):
                if self.current_piece[row][col] == 1:
                    self.board[self.current_piece_row + row][self.current_piece_col + col] = 0
    def draw_piece(self):
        for row in range(len(self.current_piece)):
            for col in range(len(self.current_piece[row])):
                if self.current_piece[row][col] == 1:
                    self.board[self.current_piece_row + row][self.current_piece_col + col] = 1
    def lock_piece(self):
        for row in range(len(self.current_piece)):
            for col in range(len(self.current_piece[row])):
                if self.current_piece[row][col] == 1:
                    self.board[self.current_piece_row + row][self.current_piece_col + col] = 1
        self.current_piece = None
    def is_valid_move(self, piece, row, col):
        for piece_row in range(len(piece)):
            for piece_col in range(len(piece[piece_row])):
                if piece[piece_row][piece_col] == 1:
                    if row + piece_row < 0 or row + piece_row >= len(self.board) or col + piece_col < 0 or col + piece_col >= len(self.board[0]) or self.board[row + piece_row][col + piece_col] == 1:
                        return False
        return True