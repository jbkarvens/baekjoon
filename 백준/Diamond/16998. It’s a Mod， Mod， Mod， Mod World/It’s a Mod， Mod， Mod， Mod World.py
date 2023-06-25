import sys
import math
input=sys.stdin.readline

def solve(p,q,n):
    if p==0:
        return 0
    if q==1:
        return n*(n+1)//2*p
    if n==0:
        return 0
    if p>q:
        return n*(n+1)//2*(p//q)+solve(p%q,q,n)
    return n*((n*p)//q)+n//q-solve(q,p,(n*p)//q)

if __name__=='__main__':
    for _ in range(int(input())):
        p,q,n=map(int, input().split())
        g=math.gcd(p,q)
        sys.stdout.write(str(n*(n+1)//2*p-q*solve(p//g,q//g,n))+'\n')