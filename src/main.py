from timer import Timer
from gfx import Gfx
from music import Music
from beatmap import Beatmap
import time
import pygame 
from board import Board

HEALTH_LOSS = 0.1
ANGLE_MAP = {0:180, 6:225, 2:270, 7:315, 3:0, 4:45 ,1:90, 5:135}
KEY_MAP = {'a': 180, 'q': 225, 'w': 270, 'e': 315, 'd': 0, 'x': 45, 's': 90, 'z': 135}
gfx = None
board = None
running = False
timer = None
music = None
score = 0

def startJoystick():
    pygame.joystick.init()
    if pygame.joystick.get_count() > 0:
        return pygame.joystick.Joystick(0)
    else:
        return 0

def handleUI(events):
    global running, timer, score, gfx, board
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        elif (event.type == pygame.KEYDOWN) or (event.type == pygame.JOYBUTTONDOWN):
            try:
                if event.type == pygame.JOYBUTTONDOWN:
                    dir = ANGLE_MAP[event.button]
                else:
                    dir = KEY_MAP[chr(event.key)]
            except (KeyError, ValueError):
                print("Invalid key", event)
                continue
            gfx.updateDelta()
            music.play_hihat()
            if timer.is_valid_hit(dir):
                print(f"On time {timer.delta()}")
            else:
                gfx.health -= HEALTH_LOSS
                print(f"Miss {timer.delta()}")
            score += timer.register_hit(dir)

def update():
    global timer, score, gfx
    if timer.was_last_missed_oneshot():
        print("Skipped")
        gfx.health -= HEALTH_LOSS
        score -= 1000

def main():
    global running, timer, music, score, gfx, board

    joystick = startJoystick()

    beatmap = Beatmap("res/map.json")
    timer = Timer(beatmap)
    gfx = Gfx(timer)
    music = Music()
    board = Board(beatmap)

    music.start_music()
    running = True
    last_time = time.time()
    while running:
        now = time.time()
        delta = now - last_time
        last_time = now
        timer.update(delta)
        update()
        gfx.render(score, board, delta)
        handleUI(pygame.event.get())

if __name__ == "__main__":
    main()
