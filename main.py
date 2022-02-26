import pygame 

screen_width = 1920
screen_height = 1080


def initGfx():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Hackathon rhythm game")
    clearScreen()
    swapBuffers()
    
def clearScreen():
    screen.fill((0, 0, 0))

def swapBuffers():
    pygame.display.flip()

def main():
    print("Hello world")
    initGfx()
    while True:
        continue

if __name__ == "__main__":
    main()
