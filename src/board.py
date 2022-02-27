import pygame
import gfx
import math
from const import EDITOR_MODE

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
        self.old_active_beat = 0

    def _scale_position(self, p):
        x, y = p
        return (START_TILE[0] + x * SCALE + self.cameraOffsetX*SCALE, START_TILE[1] + y * SCALE+self.cameraOffsetY*SCALE)

    def render(self, screen):
        if self.timer.active_beat > 0 and not EDITOR_MODE:
            pos, dir, time = self.beatmap.pos[self.timer.active_beat-1], self.beatmap.angles[self.timer.active_beat-1], self.beatmap.times[self.timer.active_beat-1]
            opacity = gfx.lerp(0,1,(max(0,min(1,-2*(time - self.timer.global_timer)))))
            color = gfx.COMPASSCOLOURS[dir//45].lerp(gfx.COLOURS[0], 1 - opacity)
            pygame.draw.circle(screen, color, self._scale_position(pos), SQUARE_SIZE)

        if EDITOR_MODE:
            iter = range(0, self.beatmap.len)
        else:
            iter = reversed(range(self.timer.active_beat, self.beatmap.len))
        for i in iter:
            pos, dir, time = self.beatmap.pos[i], self.beatmap.angles[i], self.beatmap.times[i]
            color = gfx.COMPASSCOLOURS[dir//45]
            if EDITOR_MODE:
                opacity = 1
            else:
                opacity = gfx.lerp(LOOKAHEAD_OPACITY_MIN, 1, min(1, (time - self.timer.global_timer) / LOOKAHEAD_TIME))
            color = color.lerp(gfx.COLOURS[0], 1 - opacity)
            pygame.draw.circle(screen, color, self._scale_position(pos), SQUARE_SIZE)
        self.render_player(screen)

    def render_player(self, screen):
        if self.timer.active_beat == self.beatmap.len:
            if self.beatmap.len == 0:
                x, y = (0, 0)
            elif EDITOR_MODE:
                dt = self.timer.global_timer - self.beatmap.times[-1]
                dx = dt * math.cos(self.beatmap.angles_abs[-1] * math.pi / 180)
                dy = dt * math.sin(self.beatmap.angles_abs[-1] * math.pi / 180)
                x = dx + self.beatmap.pos[-1][0]
                y = dy + self.beatmap.pos[-1][1]
                self.cameraOffsetX = -pos[0]
                self.cameraOffsetY = -pos[1]
            else:
                x, y = self.beatmap.pos[-1]

        else:
            if self.timer.active_beat == 0:
                tp, tt = (0, 0), 0
            else:
                tp, tt = self.beatmap.pos[self.timer.active_beat-1], self.beatmap.times[self.timer.active_beat-1]
            np, nt = self.beatmap.pos[self.timer.active_beat], self.beatmap.times[self.timer.active_beat]
            t = (self.timer.global_timer - tt) / (nt - tt) if nt != tt else 0
            x = tp[0] + t * (np[0] - tp[0])
            y = tp[1] + t * (np[1] - tp[1])

        pygame.draw.circle(screen, gfx.COLOURS[9], self._scale_position((x, y)), PLAYER_SIZE)
        # FIXME Don't update camera in render
        if self.mode == 0 or (self.mode == 1 and self.timer.active_beat != self.old_active_beat):
            self.cameraOffsetX = -x
            self.cameraOffsetY = -y
        self.old_active_beat = self.timer.active_beat
