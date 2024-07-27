from .state import State
import random

class MenuState(State):
    def update(self):
        pass

    def draw(self):
        super().draw()
        self.screen.fill(random.choice(["red","yellow","blue","green"]))