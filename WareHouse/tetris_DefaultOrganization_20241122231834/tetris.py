'''
This file contains the TetrisGame class which represents the Tetris game logic.
'''
import tkinter as tk
import random
class TetrisGame:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=300, height=600, bg="white")
        self.canvas.pack()
        self.board = [[0] * 10 for _ in range(20)]
        self.current_piece = None
        self.score = 0
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Up>", self.rotate_piece)
        self.draw_board()
    def start(self):
        self.create_piece()
        self.update()
    def draw_board(self):
        self.canvas.delete("all")
        for row in range(20):
            for col in range(10):
                if self.board[row][col] == 1:
                    self.canvas.create_rectangle(col * 30, row * 30, (col + 1) * 30, (row + 1) * 30, fill="blue")
    def create_piece(self):
        # Generate a random Tetris piece
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
        self.current_piece = shape
        self.place_piece()
    def place_piece(self):
        # Place the current piece on the board
        for row in range(len(self.current_piece)):
            for col in range(len(self.current_piece[0])):
                if self.current_piece[row][col] == 1:
                    self.board[row][col + 3] = 1
    def move_left(self, event):
        # Move the current piece to the left
        if self.can_move(self.current_piece, 0, -1):
            self.clear_piece()
            self.place_piece()
            self.draw_board()
    def move_right(self, event):
        # Move the current piece to the right
        if self.can_move(self.current_piece, 0, 1):
            self.clear_piece()
            self.place_piece()
            self.draw_board()
    def move_down(self, event):
        # Move the current piece down
        if self.can_move(self.current_piece, 1, 0):
            self.clear_piece()
            self.place_piece()
            self.draw_board()
    def rotate_piece(self, event):
        # Rotate the current piece
        rotated_piece = list(zip(*self.current_piece[::-1]))
        if self.can_move(rotated_piece, 0, 0):
            self.clear_piece()
            self.current_piece = rotated_piece
            self.place_piece()
            self.draw_board()
    def can_move(self, piece, dx, dy):
        # Check if the piece can be moved to the specified direction
        for row in range(len(piece)):
            for col in range(len(piece[0])):
                if piece[row][col] == 1:
                    new_row = row + dx
                    new_col = col + dy
                    if (
                        new_row < 0
                        or new_row >= len(self.board)
                        or new_col < 0
                        or new_col >= len(self.board[0])
                        or self.board[new_row][new_col] == 1
                    ):
                        return False
        return True
    def clear_piece(self):
        # Clear the current piece from the board
        for row in range(len(self.current_piece)):
            for col in range(len(self.current_piece[0])):
                if self.current_piece[row][col] == 1:
                    self.board[row][col + 3] = 0
    def update(self):
        # Update the game state and redraw the board
        if self.can_move(self.current_piece, 1, 0):
            self.clear_piece()
            self.place_piece()
            self.draw_board()
            self.root.after(500, self.update)
        else:
            self.freeze_piece()
            self.clear_lines()
            self.create_piece()
            self.update()
    def freeze_piece(self):
        # Freeze the current piece on the board
        for row in range(len(self.current_piece)):
            for col in range(len(self.current_piece[0])):
                if self.current_piece[row][col] == 1:
                    self.board[row][col + 3] = 1
    def clear_lines(self):
        # Clear completed lines from the board
        lines_cleared = 0
        for row in range(len(self.board)):
            if all(cell == 1 for cell in self.board[row]):
                self.board.pop(row)
                self.board.insert(0, [0] * 10)
                lines_cleared += 1
        self.score += lines_cleared * 100
        # Update the score display
        self.root.title(f"Tetris - Score: {self.score}")
        # Increase the game speed based on the score
        speed = max(100, 500 - self.score)
        self.root.after(speed, self.update)