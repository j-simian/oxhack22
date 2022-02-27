import pygame

class Music:
    def __init__(self,filename):
        pygame.mixer.init()
        pygame.mixer.music.load("./res/"+filename)

    def start(self):
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.pause()

    def play_hihat(self):
        # pygame.mixer.Sound("./res/hat.mp3").play()
        pass

    def play_fail(self):
        pygame.mixer.Sound("./res/bonk.mp3").play()
        pass