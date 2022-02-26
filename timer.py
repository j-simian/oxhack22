import time

bpm = 128
time_per_beat = 60 / bpm
CORRECT_HIT_TOLERANCE = 0.03

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
        if just_crossed_time(prev_timer, self.global_timer, time_per_beat / 2 - CORRECT_HIT_TOLERANCE):
            self.in_beat_window = True
            print("Beat start")
        if just_crossed_time(prev_timer, self.global_timer, time_per_beat / 2):
            print("BEAT")
        if just_crossed_time(prev_timer, self.global_timer, time_per_beat / 2 + CORRECT_HIT_TOLERANCE):
            self.in_beat_window = False
            print("Beat end")

        if self.global_timer >= time_per_beat:
            self.global_timer -= time_per_beat

    def is_in_beat_window(self):
        return self.in_beat_window
