import math
x,y=3,1
n=int(input())
while math.log(x)<n*math.log(10):
    x,y=3*x+8*y,3*y+x
print(y,2)
print(x,1)