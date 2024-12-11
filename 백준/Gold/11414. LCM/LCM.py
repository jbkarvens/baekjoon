import sys
import math
input=sys.stdin.readline

def solve(A,B):
    if A==B:
        return 1
    if A>B:
        A,B=B,A
    d=B-A
    gg=[]
    i=1
    while i*i<=d:
        if d%i==0:
            gg.append(i)
            gg.append(d//i)
        i+=1
    i-=1
    if i*i==d:
        gg.pop()
    res,low=None,None
    for g in gg:
        k=(A+g)//g
        while math.gcd(k,d//g)!=1:
            k+=1
        llcm=k*(g*k+d)
        if low==None or llcm<low:
            res,low=g*k,llcm
        elif llcm==low and res>k*g:
            res=k*g
    return res-A

A,B=map(int,input().split())
print(solve(A,B))
