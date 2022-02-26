from collections import deque

MAX_TOLERANCE = 0.40
PERFECT_TOLERANCE_FRAC = 0.2
SMALL_TOLERANCE_FRAC = 0.6

class Timer:
    def __init__(self, beatmap):
        self.beatmap = beatmap
        self.current_beat = 0
        self.active_beat = 0
        self.hit_this_beat = False
        self.miss_last_beat = False
        self.global_timer = 0

    def update(self, delta):
        prev_timer = self.global_timer
        self.global_timer += delta

        if self.current_beat < self.beatmap.len:
            beat_time = self.beatmap.times[self.current_beat]
            beat_tol = self._current_beat_tolerance_oneway()
            if prev_timer < beat_time <= self.global_timer:
                print("BEAT")

            if self.global_timer >= beat_time + beat_tol:
                self.current_beat += 1
                self.miss_last_beat = not self.hit_this_beat
                self.hit_this_beat = False

        if self.active_beat < self.beatmap.len:
            if self.global_timer >= self.beatmap.times[self.active_beat]:
                self.active_beat += 1
                if self.active_beat == self.beatmap.len:
                    return True
        return False

    # Returns the score for this hit.
    # Handles double-hit on the same beat as a fail.
    def register_hit(self, dir):
        if not self.is_valid_hit(dir):
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
        if self.current_beat + 1 < self.beatmap.len:
            return min(MAX_TOLERANCE / 2, (self.beatmap.times[self.current_beat+1] - self.beatmap.times[self.current_beat]) / 2 * SMALL_TOLERANCE_FRAC)
        else:
            return MAX_TOLERANCE / 2

    def is_in_beat_window(self):
        return abs(self.delta()) < 1
    def is_valid_hit(self, dir):
        return (self.is_in_beat_window() and not self.hit_this_beat
            and self.current_beat < self.beatmap.len 
            and self.beatmap.angles_abs[self.current_beat] == dir)

    # Returns offset from perfect beat in range [-1, 1]
    # If not currently in beat window, don't rely on this output.
    def delta(self):
        if self.current_beat < self.beatmap.len:
            tol = self._current_beat_tolerance_oneway()
            return (self.global_timer - self.beatmap.times[self.current_beat]) / tol
        else:
            return -100
