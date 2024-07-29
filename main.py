import pgzrun
import pygame

from pgzhelper import *
from system.mainloop import Mainloop

WIDTH,HEIGHT = 600,512

TITLE = "Mansion..."

main = Mainloop()

frame = 0

def update():
    global frame
    if frame == 0:
        pygame.display.set_mode((WIDTH,HEIGHT), pygame.FULLSCREEN|pygame.SCALED)
        hide_mouse()
    main.update()
    frame += 1

def draw():
    main.draw()

pgzrun.go()