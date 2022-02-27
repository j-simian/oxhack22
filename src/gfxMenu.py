import pygame
import math
from collections import deque
from pygame.locals import *
from const import EDITOR_MODE
from gfx import SCREEN_WIDTH, SCREEN_HEIGHT, COMPASSCOLOURS, COLOURS

kolor = [2, 2]
w1 = 0
w2 = 0
h1 = 0
h2 = 0

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
        global kolor, w1, w2, h1, h2
        mouse = pygame.mouse.get_pos()
        for event in events:
            if (SCREEN_WIDTH/2 - w1/2 <= mouse[0] <= SCREEN_WIDTH/2 + w1/2) and (20<=mouse[1]<=20+h1):
                kolor[0] = 3
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 1
            else:
                kolor[0] = 2
            if (SCREEN_WIDTH/2 - w2/2 <= mouse[0] <= SCREEN_WIDTH/2 + w2/2) and (90<=mouse[1]<=90+h2):
                kolor[1] = 3
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 2
            else:
                kolor[1] = 2
        return 0

    def render(self):
        global kolor, w1, w2, h1, h2
        self.clearScreen() 
        myfont = pygame.font.SysFont("Comic Sans MS", 48)

        w1,h1 = myfont.size("Just Dance")
        w2,h2 = myfont.size("Spid Dance")
        pygame.draw.rect(self.screen, COMPASSCOLOURS[kolor[0]], pygame.Rect(SCREEN_WIDTH/2-w1/2,20,w1,h1))
        pygame.draw.rect(self.screen, COMPASSCOLOURS[kolor[1]], pygame.Rect(SCREEN_WIDTH/2-w2/2,90,w2,h2))

        img = myfont.render("Just Dance", 1, COLOURS[6])
        img2 = myfont.render("Spid Dance", 1, COLOURS[6])
        self.screen.blit(img, (SCREEN_WIDTH/2 - w1/2, 20))
        self.screen.blit(img2, (SCREEN_WIDTH/2 - w2/2, 90))

        self.swapBuffers()
