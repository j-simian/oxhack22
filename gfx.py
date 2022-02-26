import pygame
import main

screen_width = 1920/2
screen_height = 1080/2

colours = [
        ("#2E3440"), ("#3B4252"), ("#434C5E"), ("#4C566A"),
        ("#D8DEE9"), ("#E5E9F0"), ("#ECEFF4"),
        ("#8FBCBB"), ("#88C0D0"), ("#81A1C1"), ("#5E81AC"),
        ("#BF616A"), ("#D08770"), ("#EBCB8B"), ("#A3BE8C"), ("#B48EAD")
        ]

def initGfx():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Hackathon rhythm game")
    clearScreen()
    swapBuffers()
    
def clearScreen():
    if main.global_timer <= 0.1:
        screen.fill(colours[4])
    else:
        screen.fill(colours[0])

def swapBuffers():
    pygame.display.flip()


def render():
    global screen
    pygame.draw.rect(screen, colours[11], pygame.Rect(50, 50, 100, 100))
    clearScreen() 
