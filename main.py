import pgzrun
import pgzero
from pgzhelper import *

from system.mainloop import Mainloop

WIDTH = 1024
HEIGHT = 1024

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