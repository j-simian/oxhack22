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
from enum import Enum

HEALTH_LOSS = 0.1
ANGLE_MAP = {0:180, 6:225, 2:270, 7:315, 3:0, 4:45 ,1:90, 5:135}
KEY_MAP = {'a': 180, 'q': 225, 'w': 270, 'e': 315, 'd': 0, 'x': 45, 's': 90, 'z': 135}

class State(Enum):
    MENU = 1
    PRE = 2
    GAME = 3
    RESULT_WIN = 4
    RESULT_LOSS = 5
    QUIT = 6

state = State.MENU

def startJoystick():
    pygame.joystick.init()
    if pygame.joystick.get_count() > 0:
        return pygame.joystick.Joystick(0)
    else:
        return 0

def handleUI(events):
    global timer, score, gfx, board, started, pressedKey, ended, completed, whichHits, state
    for event in events:
        if event.type == pygame.QUIT:
            quit_game()
            return

        elif (event.type == pygame.KEYDOWN) or (event.type == pygame.JOYBUTTONDOWN):
            if state == State.PRE:
                start_game()
                continue

            try:
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 9:
                        reset()
                        return
                    dir = ANGLE_MAP[event.button]
                else:
                    if event.key == pygame.K_r:
                        reset()
                        return
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


def start_game():
    global state, music
    state = State.GAME
    music.start()

def quit_game():
    global state
    state = State.QUIT
    pygame.quit()

def reset():
    global state, timer, gfx, beatmap, gfxResults, music, board, gfxMenu, score, whichHits, pressedKey
    state = State.MENU
    gfxMenu = GfxMenu()
    timer = None
    gfx = None
    gfxResults = None
    beatmap = None
    if music:
        music.stop()
    music = None
    board = None
    score = 0
    whichHits = [0, 0, 0]
    pressedKey = None

def main():
    global timer, music, score, gfx, gfxResults, board, beatmap, state, pressedKey, whichHits

    joystick = startJoystick()
    gfxMenu = GfxMenu()
    timer = None
    gfx = None
    gfxResults = None
    beatmap = None
    music = None
    board = None
    score = 0
    whichHits = [0, 0, 0]
    pressedKey = None

    last_time = time.time()
    while True:
        now = time.time()
        delta = now - last_time
        last_time = now

        if state == State.MENU:
            gfxMenu.render()
            mapNum = gfxMenu.handleUIMenu(pygame.event.get())
            if mapNum > 0:
                map_name = {1: "res/map.json", 2: "res/spidermap.json"}[mapNum]
                beatmap = Beatmap(map_name, EDITOR_MODE)
                timer = Timer(beatmap)
                gfx = Gfx(timer, beatmap)
                gfxResults = GfxResults(timer)
                board = Board(beatmap, timer)
                music = Music(beatmap.songfile)
                state = State.PRE

        elif state == State.PRE:
            gfx.render(score, board)
            handleUI(pygame.event.get())

        elif state == State.GAME:
            if timer.update(delta):
                state = State.RESULT_WIN
                music.stop()
            elif gfx.update(delta):
                state = State.RESULT_LOSS
                music.stop()
            else:
                update()
            gfx.render(score, board)
            handleUI(pygame.event.get())
        
        elif state == State.RESULT_WIN:
            gfxResults.render(score, True, whichHits, board)
            handleUI(pygame.event.get())
        elif state == State.RESULT_LOSS:
            gfxResults.render(score, False, whichHits, board)
            handleUI(pygame.event.get())

        elif state == State.QUIT:
            break

    if EDITOR_MODE:
        print(beatmap.to_json())

if __name__ == "__main__":
    main()
