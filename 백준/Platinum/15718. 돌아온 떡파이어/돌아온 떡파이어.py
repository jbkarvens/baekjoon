import sys
input=sys.stdin.readline

def factexp(n,p):
    x=0
    while n:
        n//=p
        x+=n
    return x

def factmod(n,p):
    if n<p:
        x=1
        for i in range(2,n+1):
            x=(x*i)%p
        return x
    return (factmod(n%p,p)*factmod(n//p,p))%p

def nCr(n,r,p):
    if factexp(n,p)-factexp(r,p)-factexp(n-r,p)>0:
        return 0
    return (factmod(n,p)*pow(factmod(r,p),-1,p)*pow(factmod(n-r,p),-1,p))%p

for _ in range(int(input())):
    N,M=map(int,input().split())
    if N+1<M or M==1:
        if N==0 and M==1:
            print(1)
        else:
            print(0)
        continue
    m1=97
    m2=1031
    r1=nCr(N-1,M-2,m1)
    r2=nCr(N-1,M-2,m2)
    r=(m2*r1*pow(m2,-1,m1)+m1*r2*pow(m1,-1,m2))%(m1*m2)
    print(r)