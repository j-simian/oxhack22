import pygame 
import gfx
from time import time

bpm = 128
time_per_beat = 60 / bpm
# running, start_time, beat_count



def handleUI(events):
    global running, beat_count
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:
            # TODO adjust beat_count on missed beat
            beat_count += 1
            now = time()
            exp = start_time + time_per_beat * beat_count
            print(now - exp)


def main():
    global running, start_time, beat_count
    print("Hello world")
    gfx.initGfx()
    running = True
    start_time = time()
    beat_count = 0
    while running:
        handleUI(pygame.event.get())
    print("Done")

if __name__ == "__main__":
    main()


