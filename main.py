import pygame 
import gfx
import time

bpm = 128
time_per_beat = 60 / bpm
CORRECT_HIT_TOLERANCE = 0.01


global_timer = 0
# last_time, running

MILLIS_EVT = pygame.USEREVENT + 1


def handleUI(events):
    global running, global_timer, last_time
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        elif event.type == pygame.KEYDOWN:
            delta = global_timer - time_per_beat
            if abs(delta) < CORRECT_HIT_TOLERANCE:
                print(f"On time {delta}")
                global_timer -= time_per_beat
            else:
                print(f"Early {delta}")

        elif event.type == MILLIS_EVT:
            now = time.time()
            global_timer += now - last_time
            last_time = now

            if global_timer > time_per_beat + CORRECT_HIT_TOLERANCE:
                print(f"Missed beat {global_timer}")
                global_timer -= time_per_beat


def startMusic():
    pygame.mixer.init()
    pygame.mixer.music.load("./res/song.mp3")
    pygame.mixer.music.play(loops=-1)
    # pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()
    print('a')

def main():
    global running, last_time
    print("Hello world")
    gfx.initGfx()
    startMusic()
    running = True
    last_time = time.time()
    pygame.time.set_timer(MILLIS_EVT, 1)
    while running:
        handleUI(pygame.event.get())
        gfx.render()
    print("Done")

if __name__ == "__main__":
    main()


