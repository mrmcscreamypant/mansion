from pgzero.keyboard import keyboard

from .state import State
from system.screen import getscale

from .wander import WanderState

with open("./data/menu/disclaimer.txt") as file:
    instructions = file.read().split("\n")

class Disclaimer(State):
    hack = True

    def update(self):
        global instructions

        if keyboard.x and not self.hack:
            self.mainloop.state = WanderState(self.mainloop)

        if not keyboard.x:
            self.hack = False

    def draw_instructions(self):
        for y,text in enumerate(instructions):
            width,height = getscale()
            self.screen.draw.text(text,center=(width/2,height/2+y*20-len(instructions)*10),fontname="dosvga")

    def draw(self):
        super().draw()
        self.screen.fill("black")
        self.draw_instructions()