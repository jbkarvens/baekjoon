import sys
import math
input_func = sys.stdin.readline

for _ in range(int(input_func())):
    L,v1,v2,t,s=map(int, input_func().split())
    vmax,todo,k=v2,1,0
    while t*todo<vmax-v1 and todo>0:
        vcut = L/(s*(k+1))
        cut = max(0,math.ceil((vmax-vcut-t)/t))
        vmax -= cut*t
        todo = 2*(todo - cut)
        k+=1
    if todo<=0:
        print('impossible')
    else:
        print(k)    