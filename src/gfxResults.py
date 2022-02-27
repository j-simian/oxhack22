import pygame
import math
from collections import deque
from pygame.locals import *
from gfx import SCREEN_WIDTH, SCREEN_HEIGHT, COLOURS

class GfxResults:
    def __init__(self, timer):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clearScreen()
        self.swapBuffers()
    
    def clearScreen(self):
        self.screen.fill(COLOURS[0])

    def swapBuffers(self):
        pygame.display.flip()

    def render(self, score, completed, whichHits, board):
        self.clearScreen()
        scoreText = str(int(score))
        if completed:
            displayText = "You're win!"
            myfont = pygame.font.SysFont("Comic Sans MS", 96)
            myfontsmall = pygame.font.SysFont("Comic Sans MS", 48)

            width, height = myfont.size(scoreText)
            img = myfont.render(scoreText, 1, COLOURS[6])
            img2 = myfont.render(displayText, 1, COLOURS[6])
            perfects=str(whichHits[0])
            mediums=str(whichHits[1])
            misses=str(whichHits[2])
            imgperfects = myfontsmall.render(perfects, 1, COLOURS[14])
            imgmediums = myfontsmall.render(mediums, 1, COLOURS[13])
            imgmisses = myfontsmall.render(misses, 1, COLOURS[11])
            self.screen.blit(img2, (200, 20))
            self.screen.blit(img, (200, 120))
            self.screen.blit(imgperfects, (200, 220))
            self.screen.blit(imgmediums, (200, 280))
            self.screen.blit(imgmisses, (200, 340))


        else:
            displayText = "You're lose!"
            myfont = pygame.font.SysFont("Comic Sans MS", 96)
            width, height = myfont.size(scoreText)
            img = myfont.render(scoreText, 1, COLOURS[6])
            img2 = myfont.render(displayText, 1, COLOURS[6])
            self.screen.blit(img2, (200, 100))
            self.screen.blit(img, (200, 200))

        self.swapBuffers()
