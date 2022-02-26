import pygame 

screen_width = 1920/2
screen_height = 1080/2


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

def handleUI(events):
    global softDrop
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()


def main():
    print("Hello world")
    initGfx()
    while True:
        handleUI(pygame.event.get())

if __name__ == "__main__":
    main()


