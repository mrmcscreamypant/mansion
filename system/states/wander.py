from .state import State

from system.utils.vec import Vec

from pgzero.builtins import Rect

class Entity:
    pos = Vec(0,0)
    def __init__(self,main):
        self.main = main
        self.main.entities.append(self)

    def draw(self):
        self.main.screen.draw.filled_circle(self.pos,10,"red")

    def update(self):
        pass

class Player(Entity):
    def update(self):
        self.pos = Vec(self.pos.x+0.1,self.pos.y+0.2)

class WanderState(State):
    def __init__(self,main):
        super().__init__(main)
        Player(self)
    
    entities = []
    
    def update(self):
        for entity in self.entities:
            entity.update()

    def draw(self):
        super().draw()
        self.screen.fill("black")

        for entity in self.entities:
            entity.draw()