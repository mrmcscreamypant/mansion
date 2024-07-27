from .state import State
import CONSTS
from system.screen import getscale

instructions = []

class MenuState(State):
    frame = 0

    def update(self):
        global instructions

        if self.frame == 20:
            instructions.append("MANSION")

        self.frame += 1

    def draw_instructions(self):
        for y,text in enumerate(instructions):
            width,height = getscale()
            self.screen.draw.text(text,center=(width/2,height/2+y*20),fontname="dosvga")

    def draw(self):
        super().draw()
        self.screen.fill("black")
        self.draw_instructions()