import pygame
from const import EDITOR_MODE
import numpy as np

class Music:
    def __init__(self,filename):
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound("./res/"+filename)
        if EDITOR_MODE:
            buf = pygame.sndarray.array(self.sound)
            buf = np.repeat(buf, 2, axis=0)
            self.sound = pygame.mixer.Sound(buffer=pygame.sndarray.make_sound(buf))

    def start(self):
        self.sound.play()

    def stop(self):
        self.sound.stop()

    def play_hihat(self):
        # pygame.mixer.Sound("./res/hat.mp3").play()
        pass

    def play_fail(self):
        pygame.mixer.Sound("./res/bonk.mp3").play()
