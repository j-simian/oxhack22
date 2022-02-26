import pygame
import gfx
import math

DIST = 30
SQUARE_SIZE = 10 
SQUARE_OFFSET = 5

class Board:

    player_pos = (0, 0)

    beats = [1] * 100
    squares = [[0, 0], [2, 1], [5, -1], [5, 0], [2, 1], [2, 1], [2, -1]]

    def render_player(self, screen):
        pygame.draw.circle(screen, gfx.COLOURS[9], (self.player_pos[0], self.player_pos[1]), SQUARE_SIZE*2)

    def render(self, screen):
        x = gfx.SCREEN_WIDTH/2
        y = gfx.SCREEN_HEIGHT/2
        angle = 0
        for i in self.squares:
            currColour = gfx.COLOURS[4] 
            if i[1] == 1:
                currColour = gfx.COLOURS[11]
            elif i[1] == -1:
                currColour = gfx.COLOURS[7]

            pygame.draw.circle(screen, currColour, (x, y), SQUARE_SIZE)
            angle += i[1]
            x += math.cos(angle*math.pi/2)*i[0] * (DIST)
            y += math.sin(angle*math.pi/2)*i[0] * (DIST)
        self.render_player(screen)


