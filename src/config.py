import pygame

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)

DIRECTIONS = {
    pygame.K_UP: (0, -CELL_SIZE),
    pygame.K_DOWN: (0, CELL_SIZE),
    pygame.K_LEFT: (-CELL_SIZE, 0),
    pygame.K_RIGHT: (CELL_SIZE, 0),
    pygame.K_w: (0, -CELL_SIZE),
    pygame.K_s: (0, CELL_SIZE),
    pygame.K_a: (-CELL_SIZE, 0),
    pygame.K_d: (CELL_SIZE, 0)
}