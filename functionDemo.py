#Jack Robey
#10/16/17
#functionDemo.py - learning functions 

def hw(): 
    print('Hello, world!')

def bigger(num1, num2): #prints which number is bigger
    if num1 > num2:
        print(num1)
    else:
        print(num2)

def slope (x1, y1, x2, y2): #calculate slope
    print((y2-y1)/(x2-x1))
    
#hw()
#bigger(13, 27) #test1
#bigger(-10,-15) #test2
#bigger('Jack', 'Andrew')
slope(1,2,2,4)
