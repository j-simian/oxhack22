import time

BPM = 128
TIME_PER_BEAT = 60 / BPM

MAX_TOLERANCE = 0.20
PERFECT_TOLERANCE_FRAC = 0.2

class Timer:
    def __init__(self, beatmap):
        self.beatmap = set(beatmap)
        self.beat_counter = 0

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

        if self.beat_counter in self.beatmap:
            if just_crossed_time(prev_timer, self.global_timer, TIME_PER_BEAT / 2 - MAX_TOLERANCE / 2):
                self.in_beat_window = True
            if just_crossed_time(prev_timer, self.global_timer, TIME_PER_BEAT / 2):
                print("BEAT")
            if just_crossed_time(prev_timer, self.global_timer, TIME_PER_BEAT / 2 + MAX_TOLERANCE / 2):
                self.in_beat_window = False
        else:
            if just_crossed_time(prev_timer, self.global_timer, TIME_PER_BEAT / 2):
                print("Beat ignored")

        if self.global_timer >= TIME_PER_BEAT:
            self.global_timer -= TIME_PER_BEAT
            self.beat_counter += 1

    def is_in_beat_window(self):
        return self.in_beat_window

    # Returns offset from perfect beat in range [-1, 1]
    # If not currently in beat window or the current beat is ignored, don't rely on this output.
    def delta(self):
        return (self.global_timer - TIME_PER_BEAT / 2) / (MAX_TOLERANCE / 2)

    def calculate_score(self):
        delta = abs(self.delta())
        if delta < PERFECT_TOLERANCE_FRAC:
            return 1000
        elif delta < 1:
            return 1000 * (1 - delta)
        else:
            return -1000
