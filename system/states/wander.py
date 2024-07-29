from .state import State
from system.screen import HEIGHT, getscale

from system.utils.vec import Vec

from pgzero.builtins import Rect, keyboard

class Entity:
    pos = Vec(0,0)
    vel = Vec(5,0)
    def __init__(self,main):
        self.main = main
        self.main.entities.append(self)

    def draw(self):
        self.main.screen.draw.filled_circle(Vec(self.pos.x-self.main.camera.x,
                                                self.pos.y-self.main.camera.y),
                                            10,
                                            "purple")

    def update(self):
        pass

class TileGrid(Entity):
    def __init__(self,main):
        self.main = main
        self.new_grid()
    
    grid = [
        "00000",
        "03010",
        "0000022232",
        "0333022232",
        "0000022232"
           ]

    colors = ["red","green","blue","yellow"]

    tilesize = 32
    
    def draw(self):
        width,height = getscale()
        for y in range(int(height/self.tilesize)+2):
            for x in range(int(width/self.tilesize)+2):
                pos = Vec(
                    x*self.tilesize+self.main.camera.x,
                    y*self.tilesize+self.main.camera.y
                   )

                
                tile = self.get_tile(pos)

                dpos = Vec(
                        x*self.tilesize-self.main.camera.x%(self.tilesize),
                        y*self.tilesize-self.main.camera.y%(self.tilesize)
                       )
                
                trect = Rect(dpos.x,dpos.y,self.tilesize,self.tilesize)
                
                self.main.screen.draw.filled_rect(
                    trect,
                    self.colors[tile]
                )
                
    def get_tile(self,pos):
        gpos = Vec(int(pos.x/self.tilesize),int(pos.y/self.tilesize))
        try:
            if pos.y < 0 or gpos.y > len(self.grid)-1:
                return 2
            if pos.x < 0 or gpos.x > len(self.grid[gpos.y])-1:
                return 2

            return int(self.grid[gpos.y][gpos.x])
        except IndexError:
            return 3
                
    def new_grid(self):
        for y in range(10):
            tmp = []
            for x in range(10):
                tmp.append(3)
            self.grid.append(tmp)

class PlatformingEntity(Entity):
    GROUND_FRIC = 0.6
    GRAV = 0.5
    AIR_FRIC = 0.9
    JUMP_STRENGTH = 7
    JUMP_TIME = 8
    CYOTE = 8

    jump_time = 0
    last_jump_time = 0

    cyote = 0

    on_ground = False

    def check_collide_ground(self):
        return self.main.tilegrid.get_tile(self.pos) == 3

    def jump(self):
        if self.jump_time > self.JUMP_TIME:
            return
        if self.jump_time > 0 or self.on_ground or self.cyote > 0:
            self.vel = Vec(self.vel.x,-self.JUMP_STRENGTH)
            self.on_ground = False
            self.jump_time += 1
            self.cyote = 0
            return
        
    
    def move_y(self):
        dir = 0.1
        if self.vel.y < 0:
            dir = -0.1

        self.pos = Vec(self.pos.x,self.pos.y+self.vel.y)
        if not self.check_collide_ground():
            self.vel = Vec(self.vel.x,
                           self.vel.y+self.GRAV)
            self.on_ground = False
            self.cyote -= 1
        else:
            while self.check_collide_ground():
                self.pos = Vec(self.pos.x,self.pos.y-dir)

            if self.vel.y > 0:
                self.on_ground = True
                self.jump_time = 0
                self.cyote = self.CYOTE

            self.vel = Vec(self.vel.x,
                           0)
    
    def move_x(self):
        dir = 0.1
        if self.vel.x < 0:
            dir = -0.1

        self.pos = Vec(self.pos.x+self.vel.x,self.pos.y)
        if self.check_collide_ground():
            self.vel = Vec(0,self.vel.y)
            while self.check_collide_ground():
                self.pos = Vec(self.pos.x-dir,self.pos.y)
            return
        if not self.on_ground:
            self.vel = Vec(self.vel.x*self.AIR_FRIC,
                           self.vel.y)
        else:
            self.vel = Vec(self.vel.x*self.GROUND_FRIC,
                           0)

    def update(self):
        self.move_x()
        self.move_y()

        if self.jump_time == self.last_jump_time:
            self.jump_time = 0
        self.last_jump_time = self.jump_time

class Player(PlatformingEntity):
    def controls(self):
        self.horizontal = 3
        if not self.on_ground:
            self.horizontal = 0.3

        if keyboard.z:
            self.jump()
        if keyboard.left:
            self.vel = Vec(self.vel.x-self.horizontal,self.vel.y)
        if keyboard.right:
            self.vel = Vec(self.vel.x+self.horizontal,self.vel.y)

    def update(self):
        super().update()
        
        self.controls()

class WanderState(State):
    def __init__(self,main):
        super().__init__(main)
        self.player = Player(self)
        self.tilegrid = TileGrid(self)
    
    entities = []
    camera = Vec(-100,-100)
    
    def update(self):
        for entity in self.entities:
            entity.update()

        width,height = getscale()
        self.camera = Vec(self.player.pos.x-width/2,self.player.pos.y-height/2)

    def draw(self):
        super().draw()
        self.screen.fill("black")

        self.tilegrid.draw()

        for entity in self.entities:
            entity.draw()