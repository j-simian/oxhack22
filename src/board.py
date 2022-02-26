import pygame
import gfx
import math

DIST = 30
SQUARE_SIZE = 10 
SQUARE_OFFSET = 5

class Board:

    beats = [1] * 100
    squares = [[0, 0], [2, 1], [5, -1], [5, 0], [2, 1], [2, 1], [2, -1]]

    def render(self, screen):
        x = gfx.SCREEN_WIDTH/2
        y = gfx.SCREEN_HEIGHT/2
        angle = 0
        for i in self.squares:
            pygame.draw.circle(screen, gfx.COLOURS[11], (x, y), SQUARE_SIZE)
            angle += i[1]
            x += math.cos(angle*math.pi/2)*i[0] * (DIST)
            y += math.sin(angle*math.pi/2)*i[0] * (DIST)

