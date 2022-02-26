import pygame 
import gfx
from time import time

hitArray=[]

def handleUI(events):
    global running, beat_count
    global hitArray
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hitArray.append(time())
            else:
                n=len(hitArray)
                if n>1:
                    gap=(hitArray[-1]-hitArray[0])/(n-1)
                    print("BPM: "+str(60/gap))
                    #sum(hitArray) == (o) + (o+gap) + (o+2*gap) + (o+3*gap) + ... = n * o + nC2 * gap
                    timeOfFirstBeat=(sum(hitArray)-gap*(n*(n-1)/2))/n #uses bpm to find out when the first beat was supposed to be
                    print("offset:"+str(timeOfFirstBeat%gap)) #this is the time of the very first beat
                hitArray=[]


def startMusic():
    pygame.mixer.init()
    pygame.mixer.music.load("song.mp3")
    pygame.mixer.music.play(loops=-1)
    # pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()
    print('a')

def main():
    global running, start_time, beat_count
    print("Hello world")
    gfx.initGfx()
    startMusic()
    running = True
    start_time = time()
    beat_count = 0
    while running:
        gfx.render()
        handleUI(pygame.event.get())
    print("Done")

if __name__ == "__main__":
    main()


