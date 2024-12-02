'''
This is the main file that runs the Tetris-like game.
'''
import pygame
import sys
from game import Game, GameOverException
def main():
    pygame.init()
    game = Game()
    try:
        game.run()
    except GameOverException:
        pass
    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    main()