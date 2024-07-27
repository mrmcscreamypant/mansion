import pgzrun
from pgzhelper import *

from system.mainloop import Mainloop

WIDTH,HEIGHT = 0,0

TITLE = "Mansion..."

main = Mainloop()

frame = 0

def update():
    global frame
    if frame == 0:
        set_fullscreen()
        hide_mouse()
    main.update()
    frame += 1

def draw():
    main.draw()

pgzrun.go()