import pygame
from pygame.locals import *

SCREEN_WIDTH = 1920/2
SCREEN_HEIGHT = 1080/2

COLOURS = [
        Color("#2E3440"), Color("#3B4252"), Color("#434C5E"), Color("#4C566A"), # DARK GREY COLOURS, INCREASING BRIGHTNESS
        Color("#D8DEE9"), Color("#E5E9F0"), Color("#ECEFF4"), # WHITE COLOURS, INCREASING BRIGHTNESS
        Color("#8FBCBB"), Color("#88C0D0"), Color("#81A1C1"), Color("#5E81AC"), # BLUE COLOURS, INCREASING BRIGHTNESS
        Color("#BF616A"), Color("#D08770"), Color("#EBCB8B"), Color("#A3BE8C"), Color("#B48EAD") # RED, ORANGE, YELLOW, GREEN, PURPLE
        ]


class Gfx:
    def __init__(self, timer):
        self.timer = timer
        self.delta = 0
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Hackathon rhythm game")
        self.clearScreen()
        self.swapBuffers()
    
    def clearScreen(self):
        if self.timer.is_in_beat_window():
            delta = self.timer.delta()
            self.screen.fill(COLOURS[0].lerp(COLOURS[4], 1-abs(delta)))
        else:
            self.screen.fill(COLOURS[0])

    def swapBuffers(self):
        pygame.display.flip()

    def updateDelta(self):
        if self.timer.is_in_beat_window():
            self.delta = self.timer.delta()
        else:
            self.delta = -2

        self.swapBuffers()

    def render(self,score, board, delta):
        self.clearScreen() 
        board.render(self.screen, delta)
        
        pygame.draw.rect(self.screen, COLOURS[2], pygame.Rect(0,0,200,50))
        pygame.draw.rect(self.screen, COLOURS[7], pygame.Rect(90*(self.delta+1),0,20,50))

        myfont = pygame.font.SysFont("Comic Sans MS", 30)
        img = myfont.render(f"score: {int(score)}", 1, COLOURS[3])
        self.screen.blit(img, (100, 100))

        self.swapBuffers()
