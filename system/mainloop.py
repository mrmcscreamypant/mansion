from .screen import getscreen
from .states.menu import MenuState

class Mainloop:
    state = MenuState()

    def update(self):
        self.state.update()

    def draw(self):
        self.state.draw()