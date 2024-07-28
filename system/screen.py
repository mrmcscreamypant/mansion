import pgzero.game as pgzscreen
import pgzero.screen as pgzdraw

WIDTH,HEIGHT = 500,500

def getscreen():
    return pgzdraw.Screen(pgzscreen.screen)

def getscale():
    return (getscreen().width,getscreen().height)