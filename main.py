import pgzrun
from system.mainloop import Mainloop

main = Mainloop()

def update():
    main.update()

def draw():
    main.draw()

pgzrun.go()