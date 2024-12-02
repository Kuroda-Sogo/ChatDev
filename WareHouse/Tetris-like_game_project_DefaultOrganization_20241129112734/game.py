'''
This file contains the Game class that manages the game logic.
'''
import pygame
from board import Board
from block import Block
from special_block import SpecialBlock
from combo_system import ComboSystem
from multiplayer import Multiplayer
from achievements import Achievements
class Game:
    def __init__(self):
        self.board = Board()
        self.block = Block()
        self.special_block = SpecialBlock()
        self.combo_system = ComboSystem()
        self.multiplayer = Multiplayer()
        self.achievements = Achievements()
    def run(self):
        # Game loop
        while True:
            self.handle_events()
            self.update()
            self.render()
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise GameOverException("Game Over")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.block.move("left")
                elif event.key == pygame.K_RIGHT:
                    self.block.move("right")
                elif event.key == pygame.K_DOWN:
                    self.block.move("down")
                elif event.key == pygame.K_UP:
                    self.block.rotate()
    def update(self):
        # Update game state
        self.board.update()
        self.block.update()
        self.special_block.update()
        self.combo_system.update()
        self.multiplayer.update()
        self.achievements.update()
        # Check if game over
        if self.board.is_game_over():
            raise GameOverException("Game Over")
    def render(self):
        # Render game graphics
        self.board.render()
        self.block.render()
        self.special_block.render()
        # Render multiplayer graphics if in multiplayer mode
        if self.multiplayer.is_multiplayer_mode():
            self.multiplayer.render()
class GameOverException(Exception):
    pass