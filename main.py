import pygame 
import gfx
import time

bpm = 128
time_per_beat = 60 / bpm
CORRECT_HIT_TOLERANCE = 0.01


global_timer = 0
in_beat_window = False
# last_time, running

MILLIS_EVT = pygame.USEREVENT + 1


def handleUI(events):
    global running, global_timer, last_time, in_beat_window
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        elif event.type == pygame.KEYDOWN:
            pygame.mixer.Sound("./res/hat.mp3").play()
            if in_beat_window:
                print(f"On time {global_timer}")
            else:
                print(f"Miss {global_timer}")

        elif event.type == MILLIS_EVT:
            now = time.time()
            prev_timer = global_timer
            global_timer += now - last_time
            last_time = now

            def just_crossed_time(prev, cur, time):
                return prev < time and cur >= time
            if just_crossed_time(prev_timer, global_timer, time_per_beat / 2 - CORRECT_HIT_TOLERANCE):
                in_beat_window = True
                print("Beat start")
            if just_crossed_time(prev_timer, global_timer, time_per_beat / 2):
                print("BEAT")
            if just_crossed_time(prev_timer, global_timer, time_per_beat / 2 + CORRECT_HIT_TOLERANCE):
                in_beat_window = False
                print("Beat end")

            if global_timer >= time_per_beat:
                global_timer -= time_per_beat

def startMusic():
    pygame.mixer.init()
    pygame.mixer.music.load("./res/song.mp3")
    pygame.mixer.music.play(loops=-1)
    # pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()

def main():
    global running, last_time
    print("Hello world")
    gfx.initGfx()
    startMusic()
    running = True
    last_time = time.time()
    pygame.time.set_timer(MILLIS_EVT, 1)
    while running:
        gfx.render()
        handleUI(pygame.event.get())
    print("Done")

if __name__ == "__main__":
    main()


