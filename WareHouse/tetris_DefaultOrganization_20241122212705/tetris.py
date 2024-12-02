'''
This file contains the Tetris class which represents the game logic and GUI.
'''
import tkinter as tk
import random
class Tetris(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.bind("<KeyPress>", self.handle_keypress)
        self.canvas = tk.Canvas(self, width=300, height=600, bg="white")
        self.canvas.pack()
        self.board = [[0] * 10 for _ in range(20)]
        self.current_piece = None
        self.score = 0
        self.draw_board()
        self.start_game()
    def draw_board(self):
        self.canvas.delete("all")
        for row in range(20):
            for col in range(10):
                if self.board[row][col] == 1:
                    self.canvas.create_rectangle(col * 30, row * 30, (col + 1) * 30, (row + 1) * 30, fill="blue")
    def start_game(self):
        self.current_piece = self.get_random_piece()
        self.master.after(1000, self.update)
    def handle_keypress(self, event):
        if event.keysym == "Up":
            self.rotate_piece()
        elif event.keysym == "Left":
            self.move_left()
        elif event.keysym == "Right":
            self.move_right()
        elif event.keysym == "Down":
            self.move_down()
        elif event.keysym == "space":
            self.drop_piece()
    def update(self):
        if self.check_collision() and self.current_piece["position"][0] == 0:
            self.game_over()
            return
        self.move_down()
        self.master.after(1000, self.update)
    def check_collision(self):
        piece_shape = self.current_piece["shape"]
        piece_row, piece_col = self.current_piece["position"]
        for row in range(len(piece_shape)):
            for col in range(len(piece_shape[0])):
                if piece_shape[row][col] and (piece_row + row >= 20 or piece_col + col < 0 or piece_col + col >= 10 or self.board[piece_row + row][piece_col + col]):
                    return True
        return False
    def rotate_piece(self):
        rotated_shape = list(zip(*self.current_piece["shape"][::-1]))
        self.current_piece["shape"] = rotated_shape
        if self.check_collision():
            self.rotate_piece()
    def move_left(self):
        self.current_piece["position"][1] -= 1
        if self.check_collision():
            self.current_piece["position"][1] += 1
    def move_right(self):
        self.current_piece["position"][1] += 1
        if self.check_collision():
            self.current_piece["position"][1] -= 1
    def move_down(self):
        self.current_piece["position"][0] += 1
        if self.check_collision():
            self.current_piece["position"][0] -= 1
            self.place_piece()
    def place_piece(self):
        piece_shape = self.current_piece["shape"]
        piece_row, piece_col = self.current_piece["position"]
        for row in range(len(piece_shape)):
            for col in range(len(piece_shape[0])):
                if piece_shape[row][col]:
                    self.board[piece_row + row][piece_col + col] = 1
        self.clear_lines()
        self.current_piece = self.get_random_piece()
    def clear_lines(self):
        full_rows = []
        for row in range(20):
            if all(self.board[row]):
                full_rows.append(row)
        for row in full_rows:
            del self.board[row]
            self.board.insert(0, [0] * 10)
        self.score += len(full_rows)
    def get_random_piece(self):
        tetrominoes = [
            [[1, 1, 1, 1]],
            [[1, 1], [1, 1]],
            [[1, 1, 0], [0, 1, 1]],
            [[0, 1, 1], [1, 1, 0]],
            [[1, 1, 1], [0, 1, 0]],
            [[1, 1, 1], [1, 0, 0]],
            [[1, 1, 1], [0, 0, 1]]
        ]
        random_shape = random.choice(tetrominoes)
        return {
            "shape": random_shape,
            "position": [0, 3]
        }
    def drop_piece(self):
        while not self.check_collision():
            self.current_piece["position"][0] += 1
        self.current_piece["position"][0] -= 1
        self.place_piece()
    def game_over(self):
        self.canvas.create_text(150, 300, text="Game Over", font=("Arial", 30), fill="red")
        self.board = [[0] * 10 for _ in range(20)]
        self.score = 0
        self.draw_board()
        self.start_game()