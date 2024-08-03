import pyjoycon as pjc
from threading import Thread

con = None

import time

class Type:
    def set_mappings(self):
        self.mappings = {
            "up":None,
            "down":None,
        }

    def check_mappings(self):
        for key in self.mappings:
            if self.mappings[key] == None:
                raise Exception(f"Controller {self.__class__.__name__}'s mapping for key '{key}' is not properly configured")

    def update(self):
        for key in self.mappings:
            self.parent.states[self.id][key] = self.mappings[key]()

    def __init__(self,parent):
        self.parent = parent
        self.set_mappings()
        self.check_mappings()

class Joycon(Type):
    joycons = []

    def __init__(self,*args):
        super().__init__(*args)
        
        self.set_mappings()

        self.connect()
    
    def update(self):
        for id in range(len(self.joycons)):
            for key in self.mappings:
                try:
                    self.parent.states[id][key] = self.mappings[key](id)
                except Exception:
                    pass

    def connect(self):
        ids = [pjc.get_L_id(),pjc.get_R_id()]
        print(ids)
        for joycon in ids:
            print(joycon)
            try:
                self.joycons.append(pjc.JoyCon(*joycon))
                self.parent.states.append({})
            except Exception as e:
                print(e)
        print(self.joycons)

    def check_up(self,id):
        joycon = self.joycons[id].get_status()
        return joycon["analog-sticks"]["left"]["horizontal"] >= 3000
    
    def check_down(self,id=0):
        joycon = self.joycons[id].get_status()
        return joycon["analog-sticks"]["left"]["horizontal"] <= 1500
    
    def check_left(self,id=0):
        joycon = self.joycons[id].get_status()
        return joycon["analog-sticks"]["left"]["vertical"] >= 3000

    def check_right(self,id=0):
        joycon = self.joycons[id].get_status()
        return joycon["analog-sticks"]["left"]["vertical"] <= 1500
    
    def check_a(self,id=0):
        joycon = self.joycons[id].get_status()
        return joycon["buttons"]["left"]["down"]
    
    def check_b(self,id=0):
        joycon = self.joycons[id].get_status()
        return joycon["buttons"]["left"]["left"]

    def set_mappings(self):
        self.mappings = {
            "up":self.check_up,
            "down":self.check_down,
            "left":self.check_left,
            "right":self.check_right,
            "a":self.check_a,
            "b":self.check_b
        }

class Controler:
    states = []

    def __init__(self,**flags):
        if flags["joycon"]:
            self.type = Joycon(self)
        else:
            self.type = Keyboard(self)
    
    def update(self):
        self.type.update()

def setup(**args):
    global con
    con = Controler(**args)
    return con.update

def get_key(key,id=0):
    try:
        return con.states[id][key]
    except Exception as e:
        return None