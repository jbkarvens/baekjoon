import sys
from random import randint
import math
input=sys.stdin.readline
MR_TEST_LIST = [2,3,5,7,11,13,17,19,23,29]
SMALL_PRIME = 100
sys.setrecursionlimit(10**6)

def is_small_prime(n):
    if n<=1:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    i=3
    while i*i<=n:
        if n%i==0: return False
        i+=2
    return True

def MR(n):
    if n<SMALL_PRIME:
        return is_small_prime(n)
    s,tmp=0,n-1
    while tmp&1==0:
        tmp>>=1
        s+=1
    d=(n-1)>>s
    for a in MR_TEST_LIST:
        a_witness=False
        cal=pow(a,d,n)
        if cal==1 or cal==n-1:
            a_witness=True
            continue
        for _ in range(1,s):
            cal=pow(cal,2,n)
            if cal==n-1:
                a_witness=True
        if not a_witness:
            return False
    return True

def isPrime(n):
    if n<SMALL_PRIME:
        return is_small_prime(n)
    else:
        return MR(n)
    
def brent(n):
    y,c=randint(1,n-1),randint(1,n-1)
    g,r,q=1,1,1
    while g==1:
        x=y
        for _ in range(r):
            y=(y*y+c)%n
        ys=y
        for i in range(r):
            y=(y*y+c)%n
            q=(q*(x-y))%n
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
    for i in range(3,SMALL_PRIME,2):
        if n%i==0:
            return [i]+factor(n//i)
    if isPrime(n):
        return [n]
    d = brent(n)
    return factor(d) + factor(n//d)

def solve(n,m):
    if m==1:
        return 0
    factors = factor(m)
    m1,m2=1,m
    fac_m2=[]
    for p in factors:
        if p not in fac_m2 and n%p==0:
            while m2%p==0:
                m2//=p
                m1*=p
    phi_m2=m2
    for p in list(dict().fromkeys(factor(m2))):
        phi_m2-=phi_m2//p
    r1,r2=0,pow(n,solve(n,phi_m2),m2)
    result = r1*m2*pow(m2,-1,m1)+r2*m1*pow(m1,-1,m2)
    return result%m

if __name__=='__main__':
    for _ in range(int(input())):
        n,m=map(int, input().split())
        sys.stdout.write(str(solve(n,m))+'\n')