import json
import os

from system.screen import getscale

from pgzero.builtins import Rect
from pgzero.builtins import keyboard

from .state import State
from .disclaimer import Disclaimer

files = {}

for file in os.listdir("./saves"):
  try:
    if file[1:] != ".savefile":
      continue
    if int(file[0]) >= 0 and int(file[0]) < 3:
      with open("./saves/"+file) as f:
        files[int(file[0])] = json.load(f)
  except Exception as e:
    files

class SaveFiles(State):
    selected = 0
    keydown = False
    xdown = True
  
    def update(self):
        if keyboard.down:
            if not self.keydown:
                self.selected += 1
            self.keydown = True
        elif keyboard.up:
            if not self.keydown:
                self.selected -= 1
            self.keydown = True
        else:
            self.keydown = False
        self.selected = self.selected%3

        if keyboard.x and not self.xdown:
           self.mainloop.state = Disclaimer(self.mainloop)
          
        if not keyboard.x:
           self.xdown = False

    def draw_slots(self):
      def draw_slot(i):
        width,height = getscale()
        rect = Rect(width/5-10,i*height/4+140,width/5*3+10,height/5+10)
        if self.selected != i:
          self.screen.draw.rect(rect,"white")
        else:
          self.screen.draw.rect(rect,"yellow")
        if i in files:
          file = files[i]
          self.screen.draw.text(file["name"],
                                topleft=(width/5,i*height/4+150),
                                fontname="dosvga"
                               )
          self.screen.draw.text(file["location"],
                                center=(width/2,i*height/4+200),
                                fontname="dosvga"
                                )
          return
          
        self.screen.draw.text("empty slot",
                              center=(width/2,i*height/4+200),
                              fontname="dosvga",
                              color = "grey"
        )

      for i in range(3):
        try:
          draw_slot(i)
        except Exception as e:
          width,height = getscale()
          self.screen.draw.text(str(e),
                                center=(width/2,i*height/4+200),
                                color="red",
                                fontname="dosvga"
                                )

    def draw(self):
        super().draw()
        self.screen.fill("black")
        width,height = getscale()
        self.screen.draw.text("SAVE FILES",
                              midtop=(width/2,height/20),
                              fontname="dosvga",
                              fontsize=50
                             )
        self.draw_slots()