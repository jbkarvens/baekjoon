import sys
from random import randint
import math
input=sys.stdin.readline
MR_TEST_LIST = [2,3,5,7,11]
SMALL_PRIME = 100

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
    m=40
    while g==1:
        x=y
        for _ in range(r):
            y=(y*y+c)%n
        k=0
        while k<r and g==1:
            ys=y
            for i in range(min(m,r-k)):
                y=(y*y+c)%n
                q=(q*(x-y))%n
            g=math.gcd(q,n)
            k+=m
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

def r4(n):
    if n==0:
        return 1
    factor_list=factor(n)
    factors=dict()
    for prime in factor_list:
        if prime in factors:
            factors[prime]+=1
        else:
            factors[prime]=1
    if 2 in factors:
        k=factors[2]
    else:
        k=0
    result=2**(min(k,1)+1)-1
    for prime in factors:
        if prime==2:
            continue
        result*=(prime**(factors[prime]+1)-1)//(prime-1)
    return 8*result

def r5(n):
    result=r4(n)
    i=1
    while i*i<=n:
        result+=2*r4(n-i*i)
        i+=1
    return result

if __name__=='__main__':
    n=int(input())
    print(r4(n))
    print(r5(n))