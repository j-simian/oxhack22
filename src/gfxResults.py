import pygame
import math
from collections import deque
from pygame.locals import *

SCREEN_WIDTH = 1920/2
SCREEN_HEIGHT = 1080/2

ERROR_WIDTH = SCREEN_WIDTH/2 - 100
ERROR_HEIGHT = SCREEN_HEIGHT - 100

COLOURS = [
        Color("#2E3440"), Color("#3B4252"), Color("#434C5E"), Color("#4C566A"), # DARK GREY COLOURS, INCREASING BRIGHTNESS
        Color("#D8DEE9"), Color("#E5E9F0"), Color("#ECEFF4"), # WHITE COLOURS, INCREASING BRIGHTNESS
        Color("#8FBCBB"), Color("#88C0D0"), Color("#81A1C1"), Color("#5E81AC"), # BLUE COLOURS, INCREASING BRIGHTNESS
        Color("#BF616A"), Color("#D08770"), Color("#EBCB8B"), Color("#A3BE8C"), Color("#B48EAD") # RED, ORANGE, YELLOW, GREEN, PURPLE
        ]

COMPASSCOLOURS = [
    Color("#B48EAD"), Color("#B48EAD"), Color("#B48EAD"), Color("#B48EAD"),
    Color("#B48EAD"), Color("#B48EAD"), Color("#B48EAD"), Color("#B48EAD")
]


class GfxResults:
    def __init__(self, timer):
        self.health = 1
        self.timer = timer
        self.existence = 2
        self.deltas = deque(([(-10,self.timer.global_timer)]*5))
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Hackathon rhythm game")
        self.clearScreen()
        self.swapBuffers()
    
    def clearScreen(self):
        self.screen.fill(COLOURS[0])

    def swapBuffers(self):
        pygame.display.flip()

    def updateDelta(self,dir):
        self.deltas.popleft()
        if self.timer.is_valid_hit(dir):
            self.deltas.append((self.timer.delta(), self.timer.global_timer))
        else:
            self.deltas.append((-10, self.timer.global_timer))

        self.swapBuffers()

    def drawErrorTimer(self):
        pygame.draw.rect(self.screen, COLOURS[2], pygame.Rect(ERROR_WIDTH,ERROR_HEIGHT,200,50))
        for i in range(5):
            if abs(self.deltas[i][0])<=1:
                lerpAmount = abs(self.deltas[i][0])
            else:
                lerpAmount = 0.5
            timeDif = self.timer.global_timer - self.deltas[i][1]
            if timeDif <= self.existence:
                h = ((self.existence-timeDif)*50)/self.existence
            else:
                h = 0
            pygame.draw.rect(self.screen, COLOURS[10].lerp(COLOURS[11],lerpAmount), pygame.Rect(ERROR_WIDTH+  95*(self.deltas[i][0]+1),ERROR_HEIGHT,10,h))        
        
    def drawHealthBar(self):
        pygame.draw.rect(self.screen, COLOURS[11], pygame.Rect(0,0,SCREEN_WIDTH*self.health,20))

    def drawCompass(self):
        centreX = 120
        centreY = 120
        for i in range(8):
            xdif = math.sin(i*(math.pi/4))*60
            ydif = math.cos(i*(math.pi/4))*60
            pygame.draw.circle(self.screen, COMPASSCOLOURS[i], (centreX+xdif, centreY+ydif), 20)
    def update(self, delta):
        if self.health < 0:
            return True
        else:
            self.health = min(1, self.health + 0.06*delta)
        return False

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
