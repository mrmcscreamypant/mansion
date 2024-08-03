from pgzero.keyboard import keyboard

from .savefiles import SaveFiles
from .state import State
from system.screen import getscale

import controller

with open("data/menu/instructions.txt") as file:
    instructions = file.read().split("\n")

class MenuState(State):
    frame = 0

    def update(self):
        global instructions

        if controller.get_key("a"):
            self.mainloop.state = SaveFiles(self.mainloop)

        self.frame += 1

    def draw_instructions(self):
        for y,text in enumerate(instructions):
            width,height = getscale()
            self.screen.draw.text(text,center=(width/2,height/2+y*20-len(instructions)*10),fontname="dosvga")

    def draw(self):
        super().draw()
        self.screen.fill("black")
        self.draw_instructions()