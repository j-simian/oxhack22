import pygame
import gfx
import math

SQUARE_SIZE = 10
START_TILE = [gfx.SCREEN_WIDTH/2, gfx.SCREEN_HEIGHT/2] 
SCALE = 50

class Board:
    def __init__(self, beatmap):
        self.cur_square = 0
        self.time = 0
        self.squares = [((0, 0), 0, 0)]
        x, y = (0, 0)
        d = (1, 0)
        for i in range(beatmap.len):
            time, angle = beatmap.times[i], beatmap.angles[i]
            if i == 0:
                x = d[0] * time
                y = d[1] * time
            else:
                x += d[0] * (time - beatmap.times[i-1])
                y += d[1] * (time - beatmap.times[i-1])

            if angle == 90:
                d = (d[1], -d[0])
            elif angle == -90:
                d = (-d[1], d[0])
            else:
                print("invalid angle {beatmap.angles[i]}")
                exit(1)
            self.squares.append(((x, y), angle, time))

    def render(self, screen, delta):
        self.time += delta
        for pos, dir, _ in self.squares:
            currColour = gfx.COLOURS[4]
            if dir == 90:
                currColour = gfx.COLOURS[11]
            elif dir == -90:
                currColour = gfx.COLOURS[7]
            pygame.draw.circle(screen, currColour, (START_TILE[0] + pos[0] * SCALE, START_TILE[1] + pos[1] * SCALE), SQUARE_SIZE)
        self.render_player(screen)

    def render_player(self, screen):
        if self.cur_square < len(self.squares) and self.time > self.squares[self.cur_square][2]:
            self.cur_square += 1
        if self.cur_square == len(self.squares):
            pygame.draw.circle(screen, gfx.COLOURS[9], self.squares[-1][0], SQUARE_SIZE*2)
            return

        tp, _, tt = self.squares[self.cur_square-1]
        np, _, nt = self.squares[self.cur_square]
        x = tp[0] + (self.time - tt) / (nt - tt) * (np[0] - tp[0])
        y = tp[1] + (self.time - tt) / (nt - tt) * (np[1] - tp[1])
        pygame.draw.circle(screen, gfx.COLOURS[9], (START_TILE[0] + x * SCALE, START_TILE[1] + y * SCALE), SQUARE_SIZE*2)
