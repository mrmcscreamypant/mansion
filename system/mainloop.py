from .screen import getscreen
from .states.menu import MenuState

from.states.wander import WanderState

class Mainloop:
    def __init__(self):
        self.state = WanderState(self)

    def update(self):
        self.state.update()

    def draw(self):
        self.state.draw()