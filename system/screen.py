import pgzero.game as pgzscreen
import pgzero.screen as pgzdraw

def getscreen():
    return pgzdraw.Screen(pgzscreen.screen)

def getscale():
    return (getscreen().width,getscreen().height)