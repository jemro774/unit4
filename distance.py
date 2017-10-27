#Jack Robey
#10/26/17
#distance.py - takes two points and returns the distance between the two points

def distance(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**(1/2)

print(distance(5,5,7,7))