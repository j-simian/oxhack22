import pygame

class Music:
    def start_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load("./res/song.mp3")
        pygame.mixer.music.play(loops=-1)
        # pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play()

    def play_hihat(self):
        pygame.mixer.Sound("./res/hat.mp3").play()
