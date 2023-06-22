import sys
input=sys.stdin.readline
import math

def solve(n):
    a,b,c=n,n+1,-(n+2)
    D=b*b-4*a*c
    sD=int(D**0.5)
    if sD*sD!=D:
        return [-1]
    u1,u2=2*a,b-sD
    v1,v2=2*a,b+sD
    gu=math.gcd(u1,u2)
    gv=math.gcd(v1,v2)
    if a%((2*a)//gu*(2*a)//gv)!=0:
        return [-1]
    k=a//((2*a)//gu*(2*a)//gv)
    u1,u2=u1//gu*k,u2//gu*k
    v1,v2=v1//gv,v2//gv
    return [u1,u2,v1,v2]

if __name__=='__main__':
    n=int(input())
    print(*solve(n))