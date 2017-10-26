#Jack Robey
#10/25/17
#printSquares.py - prints out a grid of squares


def printSquares(y,x):
    for i in range(0,y):
        print('+'+x*'--+')
        print('|  '+x*'|  ')
    print('+'+x*'--+')

printSquares(2,4)
