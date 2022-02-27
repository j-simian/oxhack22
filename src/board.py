import pygame
import gfx
import math
from const import EDITOR_MODE
from collections import namedtuple

SQUARE_SIZE = 10
PLAYER_SIZE = 15
START_TILE = [gfx.SCREEN_WIDTH/2, gfx.SCREEN_HEIGHT/2]
SCALE = 200
LOOKAHEAD_TIME = 2
LOOKAHEAD_OPACITY_MIN = 0.1

FloatText = namedtuple("FloatText", ("creation", "pos", "score"))
FLOAT_TEXT_LIFETIME = 1.0
FLOAT_OFFSET = -0.2
FLOAT_SPEED = -0.1

class Board:
    def __init__(self, beatmap, timer):
        self.timer = timer
        self.beatmap = beatmap
        self.mode = 0
        self.modes_ptr = 0
        self.cameraOffsetX = 0
        self.cameraOffsetY = 0
        self.old_active_beat = 0
        self.player_pos = (0, 0)
        self.float_list = []

    def _scale_position(self, p):
        x, y = p
        return (START_TILE[0] + x * SCALE + self.cameraOffsetX*SCALE, START_TILE[1] + y * SCALE+self.cameraOffsetY*SCALE)

    def add_float(self, score):
        self.float_list.append(FloatText(self.timer.global_timer, self.player_pos, score))

    def render(self, screen):
        if self.timer.active_beat > 0 and not EDITOR_MODE:
            pos, dir, time = self.beatmap.pos[self.timer.active_beat-1], self.beatmap.angles[self.timer.active_beat-1], self.beatmap.times[self.timer.active_beat-1]
            opacity = gfx.lerp(0,1,(max(0,min(1,-2*(time - self.timer.global_timer)))))
            if opacity > 0:
                c = gfx.COMPASSCOLOURS[dir//45]
                color = pygame.Color(c.r, c.g, c.b, int(255 * opacity))
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
                opacity = min(1,gfx.lerp(LOOKAHEAD_OPACITY_MIN, 1, min(1, (time - self.timer.global_timer) / LOOKAHEAD_TIME)))
            color = pygame.Color(color.r, color.g, color.b, int(255 * opacity))
            pygame.draw.circle(screen, color, self._scale_position(pos), SQUARE_SIZE)

        self.render_player(screen)
        self.render_floats(screen)

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
                self.cameraOffsetX = -x
                self.cameraOffsetY = -y
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

        self.player_pos = (x, y)
        pygame.draw.circle(screen, gfx.COLOURS[9], self._scale_position((x, y)), PLAYER_SIZE)

        changed_beat = self.timer.active_beat != self.old_active_beat
        if changed_beat and self.modes_ptr < len(self.beatmap.modes) and self.beatmap.modes[self.modes_ptr][1] <= self.timer.active_beat:
            self.mode = self.beatmap.modes[self.modes_ptr][0]
            self.modes_ptr += 1
        # FIXME Don't update camera in render
        if self.mode == 0 or (self.mode == 1 and changed_beat):
            self.cameraOffsetX = -x
            self.cameraOffsetY = -y
        self.old_active_beat = self.timer.active_beat

    def render_floats(self, screen):
        self.float_list = [f for f in self.float_list if self.timer.global_timer - f.creation < FLOAT_TEXT_LIFETIME]
        for f in self.float_list:
            font = pygame.font.SysFont("Comic Sans MS", 30)
            text = f"{int(f.score)}"
            width, height = font.size(text)
            if f.score == 1000:
                color = gfx.COLOURS[14]
            elif f.score > 0:
                color = gfx.COLOURS[13]
            else:
                color = gfx.COLOURS[11]
            img = font.render(text, 1, color)
            screen.blit(img, self._scale_position((f.pos[0] - width / 2 / SCALE, f.pos[1] + FLOAT_OFFSET + FLOAT_SPEED * (self.timer.global_timer - f.creation))))
