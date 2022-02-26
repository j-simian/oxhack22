import pygame
from pygame.locals import *


SCREEN_WIDTH = 1920/2
SCREEN_HEIGHT = 1080/2

COLOURS = [
        ("#2E3440"), ("#3B4252"), ("#434C5E"), ("#4C566A"),
        ("#D8DEE9"), ("#E5E9F0"), ("#ECEFF4"),
        ("#8FBCBB"), ("#88C0D0"), ("#81A1C1"), ("#5E81AC"),
        ("#BF616A"), ("#D08770"), ("#EBCB8B"), ("#A3BE8C"), ("#B48EAD")
        ]

class Gfx:
    def __init__(self, timer, score):
        self.timer = timer
        self.score = score
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Hackathon rhythm game")
        self.clearScreen()
        self.swapBuffers()
    
    def clearScreen(self):
        if self.timer.is_in_beat_window():
            self.screen.fill(COLOURS[4])
        else:
            self.screen.fill(COLOURS[0])

    def swapBuffers(self):
        pygame.display.flip()

    def render(self,score):
        self.score = score
        global COLOURS
        self.clearScreen() 
        pygame.draw.rect(self.screen, ("#FFFFFF"), pygame.Rect(10, 10, 50, 50))
        
        myfont = pygame.font.SysFont("Comic Sans MS", 30)
        img = myfont.render(f"score: {self.score*1000}", 1, COLOURS[3])
        self.screen.blit(img, (100, 100))

        self.swapBuffers()
