import time
from collections import deque

MAX_TOLERANCE = 0.20
PERFECT_TOLERANCE_FRAC = 0.2

class Timer:
    def __init__(self, beatmap):
        self.beatmap = deque(sorted(beatmap))

        self.last_time = time.time()
        self.global_timer = 0
        self.in_beat_window = False

    def update(self):
        now = time.time()
        prev_timer = self.global_timer
        self.global_timer += now - self.last_time
        self.last_time = now

        def just_crossed_time(prev, cur, time):
            return prev < time and cur >= time

        if len(self.beatmap) == 0:
            return

        next_beat_time = self.beatmap[0]
        if just_crossed_time(prev_timer, self.global_timer, next_beat_time - MAX_TOLERANCE / 2):
            self.in_beat_window = True
        if just_crossed_time(prev_timer, self.global_timer, next_beat_time):
            print("BEAT")
        if just_crossed_time(prev_timer, self.global_timer, next_beat_time + MAX_TOLERANCE / 2):
            self.in_beat_window = False

        if self.global_timer >= next_beat_time + MAX_TOLERANCE / 2:
            self.beatmap.popleft()

    def is_in_beat_window(self):
        return self.in_beat_window

    # Returns offset from perfect beat in range [-1, 1]
    # If not currently in beat window, don't rely on this output.
    def delta(self):
        if len(self.beatmap) > 0:
            return (self.global_timer - self.beatmap[0]) / (MAX_TOLERANCE / 2)
        else:
            return -100

    def calculate_score(self):
        delta = abs(self.delta())
        if delta < PERFECT_TOLERANCE_FRAC:
            return 1000
        elif delta < 1:
            return 1000 * (1 - delta)
        else:
            return -1000
