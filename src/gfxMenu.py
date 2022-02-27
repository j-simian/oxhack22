import pygame
import math
from collections import deque
from pygame.locals import *
from const import EDITOR_MODE

SCREEN_WIDTH = 1920/2
SCREEN_HEIGHT = 1080/2

kolor = 2

ERROR_WIDTH = SCREEN_WIDTH/2 - 100
ERROR_HEIGHT = SCREEN_HEIGHT - 100

COLOURS = [
        Color("#2A2D34"), Color("#3B4252"), Color("#434C5E"), Color("#4C566A"), # DARK GREY COLOURS, INCREASING BRIGHTNESS
        Color("#D8DEE9"), Color("#E5E9F0"), Color("#ECEFF4"), # WHITE COLOURS, INCREASING BRIGHTNESS
        Color("#8FBCBB"), Color("#88C0D0"), Color("#81A1C1"), Color("#5E81AC"), # BLUE COLOURS, INCREASING BRIGHTNESS
        Color("#BF616A"), Color("#D08770"), Color("#EBCB8B"), Color("#A3BE8C"), Color("#B48EAD") # RED, ORANGE, YELLOW, GREEN, PURPLE
        ]

COMPASSCOLOURS = [
        Color("#FFFFFF"), #White
        Color("#FF8800"), #orange
        Color("#FF0000"), 
        Color("#FF00FF"), 
        Color("#0000FF"), 
        Color("#00FFFF"), 
        Color("#00FF00"), 
        Color("#FFFF00") 
]


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
                kolor = 3
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 1
            else:
                kolor = 2
        return 0
    def render(self):
        global kolor
        self.clearScreen() 

        pygame.draw.rect(self.screen, COMPASSCOLOURS[kolor], pygame.Rect(SCREEN_WIDTH/2-140,20,260,50))

        myfont = pygame.font.SysFont("Comic Sans MS", 48)
        img = myfont.render("Just Dance", 1, COLOURS[6])
        self.screen.blit(img, (SCREEN_WIDTH/2 - 140, 10))



        self.swapBuffers()
def lerp(a, b, t):
    return ((a*t) + (b*(1-t)))
