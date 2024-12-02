'''
Tetris Game
'''
import pygame
from pygame.locals import *
from board import Board
from tetromino import Tetromino
from utils import draw_block, draw_grid
# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
FPS = 30
class TetrisGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.board = Board(SCREEN_WIDTH // BLOCK_SIZE, SCREEN_HEIGHT // BLOCK_SIZE)
        self.current_tetromino = Tetromino([[1, 1, 1, 1]], (255, 0, 0))
        self.current_x = self.board.width // 2 - len(self.current_tetromino.shape[0]) // 2
        self.current_y = 0
    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)
        pygame.quit()
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.is_running = False
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.move_tetromino_left()
                elif event.key == K_RIGHT:
                    self.move_tetromino_right()
                elif event.key == K_DOWN:
                    self.move_tetromino_down()
                elif event.key == K_UP:
                    self.rotate_tetromino()
    def update(self):
        if self.is_valid_position(self.current_tetromino, self.current_x, self.current_y + 1):
            self.current_y += 1
        else:
            self.board.add_tetromino(self.current_tetromino, self.current_x, self.current_y)
            self.board.remove_completed_rows()
            if self.board.is_game_over():
                self.is_running = False
            else:
                self.current_tetromino = Tetromino([[1, 1, 1, 1]], (255, 0, 0))
                self.current_x = self.board.width // 2 - len(self.current_tetromino.shape[0]) // 2
                self.current_y = 0
    def render(self):
        self.screen.fill((0, 0, 0))
        self.draw_board()
        pygame.display.flip()
    def draw_board(self):
        for row in range(len(self.board.grid)):
            for col in range(len(self.board.grid[row])):
                if self.board.grid[row][col] != 0:
                    draw_block(
                        self.screen,
                        self.board.grid[row][col],
                        col * BLOCK_SIZE,
                        row * BLOCK_SIZE,
                    )
        draw_grid(self.screen, SCREEN_WIDTH, SCREEN_HEIGHT)
    def is_valid_position(self, tetromino, x, y):
        shape = tetromino.shape
        for row in range(len(shape)):
            for col in range(len(shape[row])):
                if shape[row][col] != 0:
                    new_x = x + col
                    new_y = y + row
                    if (
                        new_x < 0
                        or new_x >= self.board.width
                        or new_y >= self.board.height
                        or self.board.grid[new_y][new_x] != 0
                    ):
                        return False
        return True
    def move_tetromino_left(self):
        if self.is_valid_position(self.current_tetromino, self.current_x - 1, self.current_y):
            self.current_x -= 1
    def move_tetromino_right(self):
        if self.is_valid_position(self.current_tetromino, self.current_x + 1, self.current_y):
            self.current_x += 1
    def move_tetromino_down(self):
        if self.is_valid_position(self.current_tetromino, self.current_x, self.current_y + 1):
            self.current_y += 1
        else:
            self.board.add_tetromino(self.current_tetromino, self.current_x, self.current_y)
            self.board.remove_completed_rows()
            if self.board.is_game_over():
                self.is_running = False
            else:
                self.current_tetromino = Tetromino([[1, 1, 1, 1]], (255, 0, 0))
                self.current_x = self.board.width // 2 - len(self.current_tetromino.shape[0]) // 2
                self.current_y = 0
    def rotate_tetromino(self):
        self.current_tetromino.rotate()
        if not self.is_valid_position(self.current_tetromino, self.current_x, self.current_y):
            self.current_tetromino.rotate()
if __name__ == "__main__":
    game = TetrisGame()
    game.run()