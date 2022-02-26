import pygame
import gfx
import math

SQUARE_SIZE = 10
PLAYER_SIZE = 15
START_TILE = [gfx.SCREEN_WIDTH/2, gfx.SCREEN_HEIGHT/2] 
SCALE = 200
LOOKAHEAD_TIME = 3
LOOKAHEAD_OPACITY_MIN = 0.3


class Board:
    def __init__(self, beatmap, timer):
        self.timer = timer
        self.beatmap = beatmap
        self.mode = 0
        self.cameraOffsetX = 0
        self.cameraOffsetY = 0

    def _scale_position(self, p):
        x, y = p
        return (START_TILE[0] + x * SCALE + self.cameraOffsetX*SCALE, START_TILE[1] + y * SCALE+self.cameraOffsetY*SCALE)

    def render(self, screen):
        if self.timer.active_beat > 0:
            pos, dir, time = self.beatmap.pos[self.timer.active_beat-1], self.beatmap.angles[self.timer.active_beat-1], self.beatmap.times[self.timer.active_beat-1]
            opacity = gfx.lerp(0,1,(max(0,min(1,-2*(time - self.timer.global_timer)))))
            color = gfx.COMPASSCOLOURS[dir//45].lerp(gfx.COLOURS[0], 1 - opacity)
            pygame.draw.circle(screen, color, self._scale_position(pos), SQUARE_SIZE)

        for i in reversed(range(self.timer.active_beat, self.beatmap.len)):
            pos, dir, time = self.beatmap.pos[i], self.beatmap.angles[i], self.beatmap.times[i]
            color = gfx.COMPASSCOLOURS[dir//45]
            opacity = gfx.lerp(LOOKAHEAD_OPACITY_MIN, 1, min(1, (time - self.timer.global_timer) / LOOKAHEAD_TIME))
            color = color.lerp(gfx.COLOURS[0], 1 - opacity)
            pygame.draw.circle(screen, color, self._scale_position(pos), SQUARE_SIZE)
        self.render_player(screen)

    def render_player(self, screen):
        if self.timer.active_beat == self.beatmap.len:
            pygame.draw.circle(screen, gfx.COLOURS[9], self._scale_position(self.beatmap.pos[-1]), PLAYER_SIZE)
            return

        if self.timer.active_beat == 0:
            tp, tt = (0, 0), 0
        else:
            tp, tt = self.beatmap.pos[self.timer.active_beat-1], self.beatmap.times[self.timer.active_beat-1]
        np, nt = self.beatmap.pos[self.timer.active_beat], self.beatmap.times[self.timer.active_beat]
        x = tp[0] + (self.timer.global_timer - tt) / (nt - tt) * (np[0] - tp[0])
        y = tp[1] + (self.timer.global_timer - tt) / (nt - tt) * (np[1] - tp[1])
        pygame.draw.circle(screen, gfx.COLOURS[9], self._scale_position((x, y)), PLAYER_SIZE)
        if self.mode == 0:
            self.cameraOffsetX = -x
            self.cameraOffsetY = -y
