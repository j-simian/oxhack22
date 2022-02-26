import pygame
import gfx
import math

SQUARE_SIZE = 10
PLAYER_SIZE = 15
START_TILE = [gfx.SCREEN_WIDTH/2, gfx.SCREEN_HEIGHT/2] 
SCALE = 200


class Board:
    def __init__(self, beatmap, timer):
        self.timer = timer
        self.mode = 0
        self.cameraOffsetX = 0
        self.cameraOffsetY = 0
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

            ar = angle / 180 * math.pi
            d = (d[0] * math.cos(ar) - d[1] * math.sin(ar), d[0] * math.sin(ar) + d[1] * math.cos(ar))
            self.squares.append(((x, y), angle, time))

    def _scale_position(self, p):
        x, y = p
        return (START_TILE[0] + x * SCALE + self.cameraOffsetX*SCALE, START_TILE[1] + y * SCALE+self.cameraOffsetY*SCALE)

    def render(self, screen):
        for pos, dir, _ in reversed(self.squares[self.timer.active_beat+1:]):
            color = gfx.COLOURS[{0: 6, 90: 11, -90: 7, 45: 12, -45: 13}.get(dir, 4)]
            pygame.draw.circle(screen, color, self._scale_position(pos), SQUARE_SIZE)
        self.render_player(screen)

    def render_player(self, screen):
        if self.timer.active_beat+1 == len(self.squares):
            pygame.draw.circle(screen, gfx.COLOURS[9], self._scale_position(self.squares[-1][0]), PLAYER_SIZE)
            return

        tp, _, tt = self.squares[self.timer.active_beat]
        np, _, nt = self.squares[self.timer.active_beat+1]
        x = tp[0] + (self.timer.global_timer - tt) / (nt - tt) * (np[0] - tp[0])
        y = tp[1] + (self.timer.global_timer - tt) / (nt - tt) * (np[1] - tp[1])
        pygame.draw.circle(screen, gfx.COLOURS[9], self._scale_position((x, y)), PLAYER_SIZE)
        if self.mode == 0:
            self.cameraOffsetX = -x
            self.cameraOffsetY = -y
