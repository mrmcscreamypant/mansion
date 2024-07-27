from .state import State
import CONSTS

instructions = [
    "CONTROLS",
    "null",
    "foo"
]

class MenuState(State):
    def update(self):
        pass

    def draw_instructions(self):
        for y,text in enumerate(instructions):
            self.screen.draw.text(text,(CONSTS.WIDTH/2,CONSTS.HEIGHT/2-y*20))

    def draw(self):
        super().draw()
        self.screen.fill("black")
        self.draw_instructions()