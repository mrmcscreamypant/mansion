import pgzrun
import pygame

from pgzhelper import *
from system.mainloop import Mainloop
import controller

import os

try:
    import splashscreen
except Exception as e:
    print(e)

WIDTH,HEIGHT = 600,512

TITLE = "Mansion..."

main = Mainloop()
controller_update = controller.setup(joycon=True)

frame = 0

def update():
    global frame
    if frame == 0:
        pygame.display.set_mode((WIDTH,HEIGHT), pygame.FULLSCREEN|pygame.SCALED)
        hide_mouse()
    main.update()

    controller_update()

    frame += 1

def draw():
    main.draw()

pgzrun.go()