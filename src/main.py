from timer import Timer
from gfx import Gfx
from gfxResults import GfxResults
from gfxMenu import GfxMenu
from music import Music
from const import EDITOR_MODE
from beatmap import Beatmap
import time
import pygame 
from board import Board

HEALTH_LOSS = 0.1
ANGLE_MAP = {0:180, 6:225, 2:270, 7:315, 3:0, 4:45 ,1:90, 5:135}
KEY_MAP = {'a': 180, 'q': 225, 'w': 270, 'e': 315, 'd': 0, 'x': 45, 's': 90, 'z': 135}
gfx = None
gfxResults = None
board = None
running = False
timer = None
music = None
score = 0
whichHits = [0,0,0] #perfects, non-perfect hits, misses
pressedKey = None
paused = False
ended = False
completed = False


def startJoystick():
    pygame.joystick.init()
    if pygame.joystick.get_count() > 0:
        return pygame.joystick.Joystick(0)
    else:
        return 0

def handleUI(events):
    global running, timer, score, gfx, board, started, pressedKey, ended
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        elif (event.type == pygame.KEYDOWN) or (event.type == pygame.JOYBUTTONDOWN):
            if not started:
                started = True
                unpause()
                continue

            try:
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 9:
                        score = 0
                        ended = False
                        main()
                    dir = ANGLE_MAP[event.button]
                else:
                    if event.key == pygame.K_r:
                        score = 0
                        completed=False
                        ended = False
                        whichHits=[0,0,0]
                        main()
                    dir = KEY_MAP[chr(event.key)]
            except (KeyError, ValueError):
                print("Invalid key", event)
                continue
            pressedKey = dir

def update():
    global timer, score, gfx, pressedKey, beatmap
    if not EDITOR_MODE and timer.was_last_missed_oneshot():
        print("Skipped")
        gfx.health -= HEALTH_LOSS
        score -= 1000

    if pressedKey is not None:
        dir = pressedKey
        pressedKey = None
        if EDITOR_MODE:
            beatmap.add(timer.global_timer, dir, True, True)
        else:
            gfx.updateDelta(dir)
            music.play_hihat()
            if timer.is_valid_hit(dir):
                print(f"On time {timer.delta()}")
            else:
                music.play_fail()
                gfx.health -= HEALTH_LOSS
                print(f"Miss {timer.delta()}")
            scoreIncrement = timer.register_hit(dir)
            score += scoreIncrement
            if scoreIncrement<0:
                whichHits[2]+=1
            elif scoreIncrement<1000:
                whichHits[1]+=1
            else:
                whichHits[0]+=1

def pause():
    global paused, music, ended
    music.stop()
    paused = True
    ended=True

def unpause():
    global paused, music
    music.start()
    paused = False

def main():
    global running, timer, music, score, gfx, gfxResults, board, paused, started, completed, beatmap

    joystick = startJoystick()

    if EDITOR_MODE:
        beatmap = Beatmap()
    else:
        beatmap = Beatmap("res/map.json")
    timer = Timer(beatmap)
    gfx = Gfx(timer, beatmap)
    gfxResults = GfxResults(timer)
    gfxMenu = GfxMenu(timer, beatmap)
    music = Music()
    board = Board(beatmap, timer)

    running = True
    started = False
    while running and not started:
        gfxMenu.render()
        started  = gfxMenu.handleUIMenu(pygame.event.get())
        # handleUI(pygame.event.get())

    last_time = time.time()
    while running:
        if not ended:
            now = time.time()
            delta = now - last_time
            last_time = now

            if not paused:
                if timer.update(delta):
                    pause()
                    completed=True
                elif gfx.update(delta):
                    pause()
                else:
                    update()

            gfx.render(score, board)
        else:
            gfxResults.render(score, completed, whichHits, board)
        handleUI(pygame.event.get())

    if EDITOR_MODE:
        print(beatmap.to_json())

if __name__ == "__main__":
    main()
