from system.screen import getscreen

class State:
    def __init__(self,mainloop):
        self.mainloop = mainloop
    
    def draw(self):
        self.screen = getscreen()