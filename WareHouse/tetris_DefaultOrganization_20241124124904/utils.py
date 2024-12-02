'''
Utility Functions
'''
import pygame
def draw_block(surface, color, x, y):
    pygame.draw.rect(surface, color, (x, y, BLOCK_SIZE, BLOCK_SIZE))
def draw_grid(surface, width, height):
    for x in range(0, width, BLOCK_SIZE):
        pygame.draw.line(surface, (128, 128, 128), (x, 0), (x, height))
    for y in range(0, height, BLOCK_SIZE):
        pygame.draw.line(surface, (128, 128, 128), (0, y), (width, y))