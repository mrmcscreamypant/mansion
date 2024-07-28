from .state import State
from system.screen import HEIGHT, getscale

from system.utils.vec import Vec

from pgzero.builtins import Rect

class Entity:
    pos = Vec(0,0)
    vel = Vec(5,0)
    def __init__(self,main):
        self.main = main
        self.main.entities.append(self)

    def draw(self):
        self.main.screen.draw.filled_circle(Vec(self.pos.x-self.main.camera.x,self.pos.y-self.main.camera.y),10,"red")

    def update(self):
        pass

class TileGrid(Entity):
    def __init__(self, main):
        super().__init__(main)
        self.new_grid()
    
    grid = [
        [0,0,0,0,0],
        [0,1,0,1,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,1,1,1,0],
        [0,0,0,0,0]
           ]

    colors = ["red","green","blue"]
    
    def draw(self):
        width,height = getscale()
        for y in range(17):
            for x in range(17):
                pos = Vec(
                    x*width/16+self.main.camera.x,
                    y*height/16+self.main.camera.y
                   )

                
                tile = self.get_tile(pos)
                
                self.main.screen.draw.filled_circle(
                    Vec(
                        x*width/16-self.main.camera.x%(width/16)+8,
                        y*height/16-self.main.camera.y%(height/16)+8
                       ),
                    16,
                    self.colors[tile]
                )
                
    def get_tile(self,pos):
        try:
            return self.grid[int(pos.y/32)][int(pos.x/32)]
        except IndexError:
            return -1
                
    def new_grid(self):
        for y in range(10):
            tmp = []
            for x in range(10):
                tmp.append(0)
            self.grid.append(tmp)

class PlatformingEntity(Entity):
    def check_collide_ground(self):
        return self.pos.y >= 493
    
    def update(self):
        self.pos = Vec(self.pos.x+self.vel.x,
                       self.pos.y+self.vel.y)
        if not self.check_collide_ground():
            self.vel = Vec(self.vel.x*0.99,
                           self.vel.y+0.1)
        else:
            self.vel = Vec(self.vel.x*0.95,
                           0)

class Player(PlatformingEntity):
    def update(self):
        super().update()

class WanderState(State):
    def __init__(self,main):
        super().__init__(main)
        Player(self)
        TileGrid(self)
    
    entities = []
    camera = Vec(-10,-50)
    
    def update(self):
        for entity in self.entities:
            entity.update()

        self.camera = Vec(self.camera.x+0.5,self.camera.y)

    def draw(self):
        super().draw()
        self.screen.fill("black")

        for entity in self.entities:
            entity.draw()