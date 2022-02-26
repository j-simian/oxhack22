import pygame
import gfx

SQUARE_SIZE = 60
SQUARE_OFFSET = 5

class Board:

    beats = [1] * 100
    squares = []

    def genSquares(self):
        self.squares = []
        for i in self.beats:
            self.squares.append()

    def render(self, screen):
        for i in self.squares:
            pygame.draw.rect(screen, gfx.COLOURS[11], pygame.Rect(gfx.SCREEN_WIDTH/2 + SQUARE_SIZE*i[0], gfx.SCREEN_HEIGHT/2 + SQUARE_SIZE*i[1], SQUARE_SIZE - SQUARE_OFFSET, SQUARE_SIZE - SQUARE_OFFSET))

