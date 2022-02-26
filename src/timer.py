from collections import deque

MAX_TOLERANCE = 0.20
PERFECT_TOLERANCE_FRAC = 0.2

class Timer:
    def __init__(self, beatmap):
        self.beatmap = deque(sorted(beatmap))

        self.global_timer = 0

    def update(self, delta):
        prev_timer = self.global_timer
        self.global_timer += delta

        def just_crossed_time(prev, cur, time):
            return prev < time and cur >= time

        if len(self.beatmap) == 0:
            return

        beat_time = self.beatmap[0]
        beat_tol = self._current_beat_tolerance_oneway()
        if just_crossed_time(prev_timer, self.global_timer, beat_time):
            print("BEAT")
        if self.global_timer >= beat_time + beat_tol:
            self.beatmap.popleft()
    
    def _current_beat_tolerance_oneway(self):
        # FIXME Consider distance to previous note as well, not just the next one.
        if len(self.beatmap) >= 2:
            return min(MAX_TOLERANCE / 2, (self.beatmap[1] - self.beatmap[0]) / 2)
        else:
            return MAX_TOLERANCE / 2

    def is_in_beat_window(self):
        return abs(self.delta()) < 1

    # Returns offset from perfect beat in range [-1, 1]
    # If not currently in beat window, don't rely on this output.
    def delta(self):
        if len(self.beatmap) > 0:
            tol = self._current_beat_tolerance_oneway()
            return (self.global_timer - self.beatmap[0]) / tol
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
