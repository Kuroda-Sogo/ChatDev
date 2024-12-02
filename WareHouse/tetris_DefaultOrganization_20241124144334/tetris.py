'''
Tetris class for game logic and GUI.
'''
import tkinter as tk
import random
from pieces import Piece, I_Piece, J_Piece, L_Piece, O_Piece, S_Piece, T_Piece, Z_Piece
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
        self.create_reset_button()  # Add reset button
    def start(self):
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Up>", self.rotate_piece)
        self.root.after(1000, self.update)
    def draw_board(self):
        self.canvas.delete("all")
        for i in range(20):
            for j in range(10):
                if self.board[i][j] == 1:
                    self.canvas.create_rectangle(j * 30, i * 30, (j + 1) * 30, (i + 1) * 30, fill="blue")
    def update(self):
        if self.current_piece is None:
            self.current_piece = self.create_piece()
        else:
            if not self.move_piece_down():
                self.place_piece()
                self.clear_lines()
                self.current_piece = None
        self.draw_board()
        self.root.after(1000, self.update)
    def create_piece(self):
        # Create a new Tetris piece
        piece = random.choice([I_Piece, J_Piece, L_Piece, O_Piece, S_Piece, T_Piece, Z_Piece])
        return piece()
    def move_piece_down(self):
        # Move the current piece down
        if self.can_move(1, 0):
            self.clear_piece()
            self.current_piece.move(1, 0)
            self.place_piece()
            return True
        return False
    def move_left(self, event):
        # Move the current piece to the left
        if self.can_move(0, -1):
            self.clear_piece()
            self.current_piece.move(0, -1)
            self.place_piece()
    def move_right(self, event):
        # Move the current piece to the right
        if self.can_move(0, 1):
            self.clear_piece()
            self.current_piece.move(0, 1)
            self.place_piece()
    def move_down(self, event):
        # Move the current piece down
        if self.can_move(1, 0):
            self.clear_piece()
            self.current_piece.move(1, 0)
            self.place_piece()
    def rotate_piece(self, event):
        # Rotate the current piece
        if self.can_rotate():
            self.clear_piece()
            self.current_piece.rotate()
            self.place_piece()
    def can_move(self, dx, dy):
        # Check if the current piece can move in the specified direction
        for i in range(4):
            for j in range(4):
                if self.current_piece.shape[i][j] == 1:
                    x = self.current_piece.x + i + dx
                    y = self.current_piece.y + j + dy
                    if x < 0 or x >= 20 or y < 0 or y >= 10 or self.board[x][y] == 1:
                        return False
        return True
    def can_rotate(self):
        # Check if the current piece can be rotated
        temp_shape = self.current_piece.get_rotated_shape()
        for i in range(4):
            for j in range(4):
                if temp_shape[i][j] == 1:
                    x = self.current_piece.x + i
                    y = self.current_piece.y + j
                    if x < 0 or x >= 20 or y < 0 or y >= 10 or self.board[x][y] == 1:
                        return False
        return True
    def clear_piece(self):
        # Clear the current piece from the board
        for i in range(4):
            for j in range(4):
                if self.current_piece.shape[i][j] == 1:
                    x = self.current_piece.x + i
                    y = self.current_piece.y + j
                    self.board[x][y] = 0
    def place_piece(self):
        # Place the current piece on the board
        for i in range(4):
            for j in range(4):
                if self.current_piece.shape[i][j] == 1:
                    x = self.current_piece.x + i
                    y = self.current_piece.y + j
                    self.board[x][y] = 1
    def clear_lines(self):
        # Clear completed lines and update score
        lines_cleared = 0
        for i in range(20):
            if all(self.board[i]):
                self.board.pop(i)
                self.board.insert(0, [0] * 10)
                lines_cleared += 1
        self.score += lines_cleared * 100
    def create_reset_button(self):
        reset_button = tk.Button(self.root, text="Reset", command=self.reset_game)
        reset_button.pack()
    def reset_game(self):
        self.board = [[0] * 10 for _ in range(20)]
        self.score = 0
        self.current_piece = None
        self.draw_board()