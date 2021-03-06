#Jack Robey
#10/20/17
#colorChangeWindow.py - pops up a window that changes to a random color every time you click it

from ggame import *
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
lightBlueOutline = LineStyle(1,lightBlue)
blueOutline = LineStyle(1,blue)
purpleOutline = LineStyle(1,purple)

def mouseClick(event):
    num = randint(1,7)
    if num == 1:
        color = red
        outline = redOutline
    elif num == 2:
        color = orange
        outline = orangeOutline
    elif num == 3:
        color = yellow
        outline = yellowOutline
    elif num == 4:
        color = green
        outline = greenOutline
    elif num == 5:
        color = lightBlue
        outline = lightBlueOutline
    elif num == 6:
        color = blue
        outline = blueOutline
    else:
        color = purple
        outline = purpleOutline
    rectangle = RectangleAsset(1000,1000,outline,color)
    Sprite(rectangle)

App().listenMouseEvent('click', mouseClick)
App().run()

