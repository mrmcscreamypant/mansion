from .screen import getscreen

class Mainloop:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        screen = getscreen()
        screen.fill("white")