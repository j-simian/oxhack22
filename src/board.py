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
    player_angle = 0

    def __init__(self, beatmap):
        self.squares = [(beatmap.times[0], beatmap.angles[0])]
        for i in range(1, beatmap.len):
            self.squares.append((3 * (beatmap.times[i] - beatmap.times[i-1]), beatmap.angles[i]))

    def render_player(self, screen):
        pygame.draw.circle(screen, gfx.COLOURS[9], (self.player_pos[0], self.player_pos[1]), SQUARE_SIZE*2)

    def render(self, screen, delta):
        x = START_TILE[0]
        y = START_TILE[1]
        for index, i in enumerate(self.squares):
            currColour = gfx.COLOURS[4] 
            x = self.cumPos(index)[0]
            y = self.cumPos(index)[1]
            if i[1] == 90:
                currColour = gfx.COLOURS[11]
            elif i[1] == -90:
                currColour = gfx.COLOURS[7]
            pygame.draw.circle(screen, currColour, (x, y), SQUARE_SIZE)
        self.tick_player(delta)
        self.render_player(screen)

    def tick_player(self, delta):
        self.player_dist += delta 
        self.player_angle = self.cumAngle(self.player_last_tile) 
        self.player_pos[0] = self.cumPos(self.player_last_tile)[0] + math.cos(self.player_angle) * self.player_dist * DIST
        self.player_pos[1] = self.cumPos(self.player_last_tile)[1] + math.sin(self.player_angle) * self.player_dist * DIST
        if self.player_dist > self.squares[self.player_last_tile][0]: 
            if self.player_last_tile == len(self.squares):
                self.player_last_tile += 1
            self.player_dist = 0


    def cumAngle(self, x):
        angle = sum(y for x,y in self.squares[0:x-1])  
        return angle

    def cumPos(self, n):
        angle = 0
        x = START_TILE[0]
        y = START_TILE[1]
        for k in range(0, n):
            i = self.squares[k]
            angle += i[1]
            x += math.cos(angle)*i[0] * (DIST)
            y += math.sin(angle)*i[0] * (DIST)
        return (x, y)
