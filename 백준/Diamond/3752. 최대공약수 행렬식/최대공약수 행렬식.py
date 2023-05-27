from random import randint
import math
NUM=10**9+7

def MR(n):
    for a in [2,3,5,7]:
        s,d=0,n-1
        while d&1==0:
            s+=1
            d>>=1
        b=pow(a,d,n)
        if b==1:
            continue
        chk=False
        for _ in range(s):
            if b==n-1:
                chk=True
                break
            b=(b*b)%n
        if not chk:
            return False
    return True

def brent(n):
    if n%2==0:
        return n
    y,c=randint(1,n-1),randint(1,n-1)
    g,r=1,1
    m=1000
    while g==1:
        x=y
        for _ in range(r):
            y=(y*y+c)%n
        k=0
        while g==1 and k<r:
            ys=y
            q=1
            for _ in range(max(m,r-k)):
                y=(y*y+c)%n
                q=((x-y)*q)%n
            k+=m
            g=math.gcd(q,n)
        r*=2
    if g==n:
        while True:
            ys=(ys*ys+c)%n
            g=math.gcd(x-ys,n)
            if g>1:
                break
    return g
        
def factor(n):
    if n<=1:
        return []
    if n%2==0:
        return [2]+factor(n//2)
    for i in range(3,100,2):
        if n%i==0:
            return [i]+factor(n//i)
    if MR(n):
        return [n]
    g=brent(n)
    while g==n:
        g=brent(n)
    return factor(g)+factor(n//g)

def phi(n):
    plst=list(dict().fromkeys(factor(n)))
    for p in plst:
        n=(n//p)*(p-1)
    return n

if __name__=='__main__':
    for _ in range(int(input())):
        n=int(input())
        x=list(map(int,input().split()))
        ans=1
        for i in range(n):
            ans=(ans*phi(x[i]))%NUM
        print(ans)