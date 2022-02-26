from timer import Timer
from gfx import Gfx
from music import Music
from beatmap import Beatmap
import time
import pygame 
from board import Board

HEALTH_LOSS = 0.1
ANGLE_MAP = {0:180, 6:225, 2:270, 7:315, 3:0, 4:45 ,1:90, 5:135}
danceMode = False
gfx = None
board = None
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
    global running, timer, score, gfx, board, danceMode
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        elif (event.type == pygame.KEYDOWN) or (event.type == pygame.JOYBUTTONDOWN):
            if danceMode and (event.type == pygame.JOYBUTTONDOWN):
                if event.button < 8:
                    print(ANGLE_MAP[event.button])
            gfx.updateDelta()
            music.play_hihat()
            if timer.is_valid_hit():
                print(f"On time {timer.delta()}")
            else:
                gfx.health -= HEALTH_LOSS
                print(f"Miss {timer.delta()}")
            score += timer.register_hit()

def update():
    global timer, score, gfx
    if timer.was_last_missed_oneshot():
        print("Skipped")
        gfx.health -= HEALTH_LOSEE
        score -= 1000

def main():
    global running, timer, music, score, gfx, board, danceMode

    try:
        joystick = startJoystick()
        danceMode = True
    except pygame.error:
        pass

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
