import time

BPM = 128
TIME_PER_BEAT = 60 / BPM

PERFECT_TOLERANCE = 0.03
MAX_TOLERANCE = 0.20

class Timer:
    def __init__(self):
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
        if just_crossed_time(prev_timer, self.global_timer, TIME_PER_BEAT / 2 - MAX_TOLERANCE / 2):
            self.in_beat_window = True
            print("Beat start")
        if just_crossed_time(prev_timer, self.global_timer, TIME_PER_BEAT / 2):
            print("BEAT")
        if just_crossed_time(prev_timer, self.global_timer, TIME_PER_BEAT / 2 + MAX_TOLERANCE / 2):
            self.in_beat_window = False
            print("Beat end")

        if self.global_timer >= TIME_PER_BEAT:
            self.global_timer -= TIME_PER_BEAT

    def is_in_beat_window(self):
        return self.in_beat_window

    def delta(self):
        return abs(self.global_timer - TIME_PER_BEAT / 2)

    def calculate_score(self):
        delta = self.delta()
        if delta < PERFECT_TOLERANCE:
            return 1000
        elif delta < MAX_TOLERANCE:
            return 1000 * (1 - delta / (MAX_TOLERANCE / 2))
        else:
            return -1000
