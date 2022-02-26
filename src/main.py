from timer import Timer
from gfx import Gfx
from music import Music
from beatmap import load_beatmap
import time
import pygame 
from board import Board

running = False
timer = None
music = None
score = 0

def startJoystick():
    pygame.joystick.init()
    if pygame.joystick.get_count:
        return pygame.joystick.Joystick(0)
    else:
        return 0

def handleUI(events):
    global running, timer, score
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        elif event.type == pygame.KEYDOWN:
            music.play_hihat()
            if timer.is_in_beat_window():
                print(f"On time {timer.delta()}")
            else:
                print(f"Miss {timer.delta()}")
            score += timer.calculate_score()

def main():
    global running, timer, music, score

    try:
        joystick = startJoystick()
    except pygame.error:
        pass

    timer = Timer([i for i in range(100) if i % 3 != 0])
    beatmap = load_beatmap()
    timer = Timer(beatmap)
    gfx = Gfx(timer)
    music = Music()
    board = Board()

    music.start_music()
    running = True
    while running:
        timer.update()
        gfx.render(score, board)
        handleUI(pygame.event.get())

if __name__ == "__main__":
    main()
