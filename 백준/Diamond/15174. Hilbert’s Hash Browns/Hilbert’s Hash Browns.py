import sys
input=sys.stdin.readline

from random import randint
import math
SMALL_NUM = 100
MR_TEST_LIST=[2,3,5,7,11,13,17,19,23,29]

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


def isPrime(n):
    s,tmp = 0,n-1
    while not tmp&1:
        tmp>>=1
        s++1
    d=(n-1)>>s
    for a in MR_TEST_LIST:
        a_witness = False
        cal = pow(a,d,n)
        if cal==1 or cal==n-1:
            a_witness=True
            continue
        for _ in range(1,s):
            cal=pow(cal,2,n)
            if cal==n-1:
                a_witness = True
        if not a_witness:
            return False
    return True

def factor(n):
    if n<=1:
        return []
    for i in range(2,SMALL_NUM):
        if n%i==0:
            return [i]+factor(n//i)
    if isPrime(n):
        return [n]
    k = brent(n)
    return factor(k)+factor(n//k)

def solve_prime_power(m,p,e):
    if p==2:
        if e==1:
            return 2
        if m&1:
            if m>=e:
                return 1+pow(2,e-1)
            else:
                return pow(2,e-1)+solve_prime_power(m,p,e-m)
        else:
            a=pow(2,e-2)
            if m>=e:
                return 1+a//math.gcd(m,a)
            else:
                return a//math.gcd(m,a)+solve_prime_power(m,p,e-m)
                
    else:
        result = 0
        while e>0:
            a = (p-1)*pow(p,e-1)
            result+=a//math.gcd(a,m)
            e-=m
        result+=1
        return result

def solve(m,n):
    factor_list=factor(n)
    factors=dict()
    for p in factor_list:
        if p in factors:
            factors[p]+=1
        else:
            factors[p]=1
    result = 1
    for p in factors:
        result *= solve_prime_power(m,p,factors[p])
    return result

if __name__=="__main__":
    p,q,n=map(int,input().split())
    print(solve(p,n))