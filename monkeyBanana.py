#Jack Robey
#10/19/17
#monkeyBanana.py - best game ever

from ggame import *

#constants
ROWS = 15
COLS = 20
CELL_SIZE = 20

if __name__ == '__main__':
    
    green = Color(0x006600,1)
    brown = Color(0x8B4513,1)
    yellow = Color(0xFFFF00,1)
    
    jungleBox = RectangleAsset(COLS*CELL_SIZE,ROWS*CELL_SIZE,LineStyle(1,green),green)
    monkeyBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown),brown)
    bananaBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,yellow),yellow)
    
    Sprite(jungleBox)
    Sprite(monkeyBox)
    Sprite(bananaBox,(COLS*CELL_SIZE/2,ROWS*CELL_SIZE/2))
    
    App().litsenKeyEvent('keydown','right arrow',moveRight)
    App().run()
