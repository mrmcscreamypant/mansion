from .state import State

from system.screen import getscale

class SaveFiles(State):
    def update(self):
        pass

    def draw(self):
        super().draw()
        self.screen.fill("black")
        width,height = getscale()
        self.screen.draw.text("save files",midtop=(width/2,height/20),fontname="dosvga")