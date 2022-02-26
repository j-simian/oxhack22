import pygame
from pygame.locals import *


screen_width = 1920/2
screen_height = 1080/2

colours = [
        ("#2E3440"), ("#3B4252"), ("#434C5E"), ("#4C566A"),
        ("#D8DEE9"), ("#E5E9F0"), ("#ECEFF4"),
        ("#8FBCBB"), ("#88C0D0"), ("#81A1C1"), ("#5E81AC"),
        ("#BF616A"), ("#D08770"), ("#EBCB8B"), ("#A3BE8C"), ("#B48EAD")
        ]

class Gfx:
    def __init__(self, timer):
        self.timer = timer
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Hackathon rhythm game")
        self.clearScreen()
        self.swapBuffers()
    
    def clearScreen(self):
        if self.timer.is_in_beat_window():
            self.screen.fill(colours[4])
        else:
            self.screen.fill(colours[0])

    def swapBuffers(self):
        pygame.display.flip()

    def render(self):
        global colours
        self.clearScreen() 
        pygame.draw.rect(self.screen, ("#FFFFFF"), pygame.Rect(10, 10, 50, 50))
        self.swapBuffers()
