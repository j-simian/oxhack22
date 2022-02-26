from timer import Timer
from gfx import Gfx
import time
import music
import pygame 

running = False
timer = None


def handleUI(events):
    global running, timer
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        elif event.type == pygame.KEYDOWN:
            pygame.mixer.Sound("./res/hat.mp3").play()
            if timer.is_in_beat_window():
                print(f"On time {timer}")
            else:
                print(f"Miss {timer}")

def main():
    global running, timer

    timer = Timer()
    gfx = Gfx(timer)
    music.startMusic()

    running = True
    while running:
        timer.update()
        gfx.render()
        handleUI(pygame.event.get())

if __name__ == "__main__":
    main()
