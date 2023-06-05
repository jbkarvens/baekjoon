import math
N=10**18
A=dict()
def pib(n,m):
    if (n,m) in A:
        return A[(n,m)]
    if n+m*math.pi<=math.pi:
        A[(n,m)]=1
        return 1
    x=(pib(n,m-1)+pib(n-1,m))%N
    A[(n,m)]=x
    return x
print(pib(int(input()),0))