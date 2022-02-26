from collections import deque

MAX_TOLERANCE = 0.40
PERFECT_TOLERANCE_FRAC = 0.2

class Timer:
    def __init__(self, beatmap):
        self.beatmap = deque(sorted(beatmap.times))
        self.hit_this_beat = False
        self.miss_last_beat = False

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
            self.miss_last_beat = not self.hit_this_beat
            self.hit_this_beat = False

    # Returns the score for this hit.
    # Handles double-hit on the same beat as a fail.
    def register_hit(self):
        if self.hit_this_beat:
            return -1000
        self.hit_this_beat = True

        delta = abs(self.delta())
        if delta < PERFECT_TOLERANCE_FRAC:
            return 1000
        elif delta < 1:
            return 1000 * (1 - delta)
        else:
            return -1000

    def was_last_missed_oneshot(self):
        tmp = self.miss_last_beat
        self.miss_last_beat = False
        return tmp
    
    def _current_beat_tolerance_oneway(self):
        # FIXME Consider distance to previous note as well, not just the next one.
        if len(self.beatmap) >= 2:
            return min(MAX_TOLERANCE / 2, (self.beatmap[1] - self.beatmap[0]) / 2)
        else:
            return MAX_TOLERANCE / 2

    def is_in_beat_window(self):
        return abs(self.delta()) < 1
    def is_valid_hit(self):
        return self.is_in_beat_window() and not self.hit_this_beat

    # Returns offset from perfect beat in range [-1, 1]
    # If not currently in beat window, don't rely on this output.
    def delta(self):
        if len(self.beatmap) > 0:
            tol = self._current_beat_tolerance_oneway()
            return (self.global_timer - self.beatmap[0]) / tol
        else:
            return -100
