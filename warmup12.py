#Jack Robey
#10/27/17
#warmup12.py

def GCF(x,y):
    for i in range(y,1,-1):
        if x%i == 0 and y%i == 0:
            return i

print(GCF(56,40))
