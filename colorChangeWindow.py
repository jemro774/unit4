#Jack Robey
#10/20/17
#colorChangeWindow.py - pops up a window that changes to a random color every time you click it

from random import randint

red = Color(0xff0000,1)
orange = Color(0xffa500,1)
yellow = Color(0xffff00,1)
green = Color(0x00ff00,1)
lightBlue = Color(0x00ffff,1)
blue = Color(0x0000ff,1)
purple = Color(0xa020f0,1)

redOutline = LineStyle(1,red)
orangeOutline = LineStyle(1,orange)
yellowOutline = LineStyle(1,yellow)
greenOutline = LineStyle(1,green)

def mouseClick(event):
    
    
App().listenMouseEvent('click', mouseClick)
App().run()
