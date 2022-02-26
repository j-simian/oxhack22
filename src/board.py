import pygame
import gfx
import math

DIST = 30
SQUARE_SIZE = 10 
SQUARE_OFFSET = 5

START_TILE = [gfx.SCREEN_WIDTH/2, gfx.SCREEN_HEIGHT/2] 

class Board:

    player_pos = [START_TILE[0], START_TILE[1]]
    player_dist = 0
    player_last_tile = 0

    beats = [1] * 100
    squares = [[0, 0], [2, 1], [5, -1], [5, 0], [2, 1], [2, 1], [2, -1]]

    def render_player(self, screen):
        pygame.draw.circle(screen, gfx.COLOURS[9], (self.player_pos[0], self.player_pos[1]), SQUARE_SIZE*2)

    def render(self, screen, delta):
        x = START_TILE[0]
        y = START_TILE[1]
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
        self.tick_player(delta)
        self.render_player(screen)

    def tick_player(self, delta):
        self.player_dist += delta * 0.01
        print(self.player_dist)
        self.player_pos[0] = self.squares[self.player_last_tile][0] + math.cos(sum(y for x,y in self.squares[0:self.player_last_tile])*math.pi/2) * self.player_dist * DIST
        self.player_pos[1] = self.squares[self.player_last_tile][1] + math.sin(sum(y for x,y in self.squares[0:self.player_last_tile])*math.pi/2) * self.player_dist * DIST
        print(self.player_pos[0])
        if self.player_dist > self.squares[self.player_last_tile][0]: 
            self.player_last_tile += 1
            self.player_dist = 0

