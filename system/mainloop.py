from .screen import getscreen
from .states.menu import MenuState

class Mainloop:
    def __init__(self):
        self.state = MenuState(self)

    def update(self):
        self.state.update()

    def draw(self):
        self.state.draw()