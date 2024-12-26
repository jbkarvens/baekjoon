import sys
input=sys.stdin.readline

import math
for _ in range(int(input())):
    W,L=map(int,input().split())
    res=set([1,2])
    a=1
    g=math.gcd(W,L-2)
    while a*a<=g:
        if g%a==0:
            res.add(a)
            res.add(g//a)
        a+=1
    a=1
    g=math.gcd(W-1,L-1)
    while a*a<=g:
        if g%a==0:
            res.add(a)
            res.add(g//a)
        a+=1
    a=1
    g=math.gcd(W-2,L)
    while a*a<=g:
        if g%a==0:
            res.add(a)
            res.add(g//a)
        a+=1
    res=list(res)
    res.sort()
    res=[len(res)]+res
    print(*res)