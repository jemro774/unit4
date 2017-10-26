#Jack Robey
#10/25/17
#printSquares.py - prints out a grid of squares


def printSquares(x,y):
    for i in range(0,y):
        print('+'+x*'--+')
        print('|  '+x*'|  ')
    print('+'+x*'--+')

printSquares(5,6)

