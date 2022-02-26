import pygame
import gfx

SQUARE_SIZE = 50
OFFSET = 100

class Board:

    squares = [
            [0, 0], [1, 0], [2, 1], [3, 0]
            ]

    def render(self, screen):
        for i in self.squares:
            pygame.draw.rect(screen, gfx.COLOURS[11], pygame.Rect(OFFSET + SQUARE_SIZE*i[0], OFFSET + SQUARE_SIZE*i[1], SQUARE_SIZE, SQUARE_SIZE))

