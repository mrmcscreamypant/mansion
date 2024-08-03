from .screen import getscreen
from .states.menu import MenuState

from.states.wander import WanderState

from pygame.time import Clock

clock = Clock()

class Mainloop:
    def __init__(self):
        self.state = MenuState(self)

    def update(self):
        self.state.update()

        clock.tick()

    def draw(self):
        self.state.draw()

        self.state.screen.draw.text("FPS: "+str(int(clock.get_fps())),(10,10))