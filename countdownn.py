#Jack Robey
#10/16/17
#countdownn.py - takes an integer as input and counts down to zero from that number

def countdownn(num):
    for i in range (num,0,-1):
        print(i)
    print('BOOM!')

countdownn(5)