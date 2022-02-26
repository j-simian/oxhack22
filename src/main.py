from timer import Timer
from gfx import Gfx
from music import Music
from beatmap import load_beatmap
import time
import pygame 
from board import Board

gfx = None
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
    global running, timer, score, gfx
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        elif (event.type == pygame.KEYDOWN) or (event.type == pygame.JOYBUTTONDOWN):
            gfx.updateDelta()
            music.play_hihat()
            if timer.is_in_beat_window():
                print(f"On time {timer.delta()}")
            else:
                print(f"Miss {timer.delta()}")
            timer.register_hit()
            score += timer.calculate_score()

def update():
    global timer, score
    if timer.was_last_missed_oneshot():
        print("Skipped")
        score -= 1000

def main():
    global running, timer, music, score, gfx

    try:
        joystick = startJoystick()
    except pygame.error:
        pass

    timer = Timer([i for i in range(100) if i % 3 != 0])
    beatmap = load_beatmap()[0]
    timer = Timer(beatmap)
    gfx = Gfx(timer)
    music = Music()
    board = Board()

    music.start_music()
    running = True
    last_time = time.time()
    while running:
        now = time.time()
        delta = now - last_time
        last_time = now

        timer.update(delta)
        update()
        handleUI(pygame.event.get())
        gfx.render(score, board)

if __name__ == "__main__":
    main()
