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
    global running
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                startMusic()


def startMusic():
    pygame.mixer.init()
    pygame.mixer.music.load("song.mp3")
    pygame.mixer.music.play(loops=-1)
    # pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()
    print('a')

def main():
    global running
    print("Hello world")
    initGfx()
    # startMusic()
    running = True
    while running:
        handleUI(pygame.event.get())
    print("Done")

if __name__ == "__main__":
    main()


