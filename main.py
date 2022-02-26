from timer import Timer
from gfx import Gfx
from music import Music
import time
import pygame 

running = False
timer = None
music = None
score = 0

def handleUI(events):
    global running, timer, score
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        elif event.type == pygame.KEYDOWN:
            music.play_hihat()
            score+=1
            if timer.is_in_beat_window():
                print(f"On time {timer}")
            else:
                print(f"Miss {timer}")

def main():
    global running, timer, music, score

    timer = Timer()
    gfx = Gfx(timer,score)
    music = Music()

    running = True
    while running:
        timer.update()
        gfx.render(score)
        handleUI(pygame.event.get())

if __name__ == "__main__":
    main()
