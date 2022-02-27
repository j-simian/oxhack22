import pygame
import math
from collections import deque
from pygame.locals import *
from const import EDITOR_MODE
from gfx import SCREEN_WIDTH, SCREEN_HEIGHT, COMPASSCOLOURS, COLOURS


msgs = ["Just Dance", "Spid Dance","Snowdin", "Gentlemen in Paris66","rish's theme"]
kolor = [2]*len(msgs)
sizes = [(0,0)] * len(msgs)
class GfxMenu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Hackathon rhythm game")
        self.clearScreen()
        self.swapBuffers()
    
    def clearScreen(self):
        self.screen.fill(COLOURS[0])

    def swapBuffers(self):
        pygame.display.flip()

    def handleUIMenu(self, events):
        global kolor, sizes, msgs
        mouse = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                # FIXME Correctly handle this
                pygame.quit()
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 2:
                    return 1
                if event.button == 1:
                    return 2
                if event.button == 3:
                    return 3
                if event.button == 0:
                    return 4
                if event.button == 7:
                    return 5
            for i in range(len(msgs)):
                if (SCREEN_WIDTH/2 - sizes[i][0]/2 <= mouse[0] <= SCREEN_WIDTH/2 + sizes[i][0]/2) and (20+70*i<=mouse[1]<=20+70*i+sizes[i][1]):
                    kolor[i] = 3
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        return i+1
                else:
                    kolor[i] = 2
        return 0

    def render(self):
        global kolor, sizes, msgs
        self.clearScreen() 
        myfont = pygame.font.SysFont("Comic Sans MS", 48)
        imgs = [None]*(len(msgs))
        for i in range(len(msgs)):
            sizes[i] = myfont.size(msgs[i])
            imgs[i] = myfont.render(msgs[i], 1, COLOURS[6])
            pygame.draw.rect(self.screen, COMPASSCOLOURS[kolor[i]], pygame.Rect(SCREEN_WIDTH/2-sizes[i][0]/2,20+70*i,sizes[i][0],sizes[i][1]))
            self.screen.blit(imgs[i], (SCREEN_WIDTH/2 - sizes[i][0]/2, 20+70*i))

        self.swapBuffers()
