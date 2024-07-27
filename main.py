import pgzrun
from pgzhelper import *

from system.mainloop import Mainloop
import CONSTS

WIDTH,HEIGHT = CONSTS.WIDTH,CONSTS.HEIGHT

TITLE = "Mansion..."

main = Mainloop()

frame = 0

def update():
    global frame
    if frame == 0:
        set_fullscreen()
    main.update()
    frame += 1

def draw():
    main.draw()

pgzrun.go()