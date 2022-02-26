import pygame

def startMusic():
    pygame.mixer.init()
    pygame.mixer.music.load("./res/song.mp3")
    pygame.mixer.music.play(loops=-1)
    # pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()