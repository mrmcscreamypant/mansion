import json
import os

from system.screen import getscale

from .state import State

files = {}

for file in os.listdir("./saves"):
  if file[1:] != ".savefile":
    continue
  if int(file[0]) >= 0 and int(file[0]) < 3:
    with open("./saves/"+file) as f:
      files[int(file[0])] = json.load(f)

print(files)

class SaveFiles(State):
    def update(self):
        pass

    def draw_slots(self):
      def draw_slot(i):
        if i in files.keys():
          file = files[i]
          width,height = getscale()
          self.screen.draw.text(file["name"],
                                topleft=(width/5,i*height/5+120),
                                fontname="dosvga"
                               )
          self.screen.draw.text(file["location"],
                                center=(width/2,i*height/5+150),
                                fontname="dosvga"
                                )

      for i in range(3):
        try:
          draw_slot(i)
        except Exception as e:
          width,height = getscale()
          self.screen.draw.text(str(e),
                                center=(width/2,i*height/5+150),
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