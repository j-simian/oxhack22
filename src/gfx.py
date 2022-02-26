import pygame
from pygame.locals import *

SCREEN_WIDTH = 1920/2
SCREEN_HEIGHT = 1080/2

COLOURS = [
        Color("#2E3440"), ("#3B4252"), ("#434C5E"), ("#4C566A"),
        Color("#D8DEE9"), ("#E5E9F0"), ("#ECEFF4"),
        ("#8FBCBB"), ("#88C0D0"), ("#81A1C1"), ("#5E81AC"),
        ("#BF616A"), ("#D08770"), ("#EBCB8B"), ("#A3BE8C"), ("#B48EAD")
        ]

class Gfx:
    def __init__(self, timer):
        self.timer = timer
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Hackathon rhythm game")
        self.clearScreen()
        self.swapBuffers()
    
    def clearScreen(self):
        if self.timer.is_in_beat_window():
            delta = self.timer.delta()
            self.screen.fill(COLOURS[4].lerp(COLOURS[0], delta))
        else:
            self.screen.fill(COLOURS[0])

    def swapBuffers(self):
        pygame.display.flip()

    def render(self,score, board):
        self.clearScreen() 
        board.render(self.screen)
        
        myfont = pygame.font.SysFont("Comic Sans MS", 30)
        img = myfont.render(f"score: {int(score)}", 1, COLOURS[3])
        self.screen.blit(img, (100, 100))

        self.swapBuffers()
