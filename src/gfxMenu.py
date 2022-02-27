import pygame
import math
from collections import deque
from pygame.locals import *
from const import EDITOR_MODE
from gfx import SCREEN_WIDTH, SCREEN_HEIGHT, COMPASSCOLOURS, COLOURS

kolor = [2, 2]

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
        global kolor
        mouse = pygame.mouse.get_pos()
        for event in events:
            if (SCREEN_WIDTH/2 - 140 <= mouse[0] <= SCREEN_WIDTH/2 + 140) and (20<=mouse[1]<=70):
                kolor[0] = 3
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 1
            else:
                kolor[0] = 2
            if (SCREEN_WIDTH/2 - 140 <= mouse[0] <= SCREEN_WIDTH/2 + 140) and (80<=mouse[1]<=130):
                kolor[1] = 3
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 2
            else:
                kolor[1] = 2
        return 0

    def render(self):
        global kolor
        self.clearScreen() 

        pygame.draw.rect(self.screen, COMPASSCOLOURS[kolor[0]], pygame.Rect(SCREEN_WIDTH/2-140,20,260,50))
        pygame.draw.rect(self.screen, COMPASSCOLOURS[kolor[1]], pygame.Rect(SCREEN_WIDTH/2-140,90,260,50))

        myfont = pygame.font.SysFont("Comic Sans MS", 48)
        img = myfont.render("Just Dance", 1, COLOURS[6])
        img2 = myfont.render("Spid Dance", 1, COLOURS[6])
        self.screen.blit(img, (SCREEN_WIDTH/2 - 140, 10))
        self.screen.blit(img2, (SCREEN_WIDTH/2 - 140, 80))

        self.swapBuffers()
