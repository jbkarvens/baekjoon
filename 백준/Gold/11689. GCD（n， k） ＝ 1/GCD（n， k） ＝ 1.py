import sys
from random import randint
from math import gcd
input=sys.stdin.readline
MR_TEST = [2,3,5,7,11]
SMALL_NUM = 100

def isPrime(n):
    if n<=MR_TEST[-1]:
        if n in MR_TEST:
            return True
        else:
            return False
    s,d = 0,n-1
    while not d&1:
        s+=1
        d>>=1
    for a in MR_TEST:
        ap=pow(a,d,n)
        if ap==1:
            continue
        a_witness = False
        for i in range(s):
            if ap == n-1:
                a_witness = True
                break
            else:
                ap = (ap*ap)%n
        if a_witness:
            continue
        else:
            return False
    return True

def factor(n):
    if n == 1:
        return []
    for i in range(2,SMALL_NUM):
        if n%i == 0:
            if n == i:
                return [n]
            else:
                return factor(i) + factor(n//i)
    if isPrime(n):
        return [n]
    for _ in range(1000):
        y,c = randint(1,n-1), randint(1,n-1)
        if c == n-2:
            continue
        g,r,q = 1,1,1
        m = 1000
        while g==1:
            x = y
            for _ in range(r):
                y = (y*y+c)%n
            k = 0
            while k<r and g==1:
                ys = y
                for i in range(min(m,r-k)):
                    y = (y*y+c)%n
                    q = (q*(x-y))%n
                g = gcd(q,n)
                k+=m
            r*=2
        if g==n:
            while True:
                ys=(ys*ys+c)%n
                g = gcd(x-ys,n)
                if g>1:
                    break
        if g==1 or g==n:
            continue
        else:
            break
    return factor(g)+factor(n//g)

def tot(n):
    plst = dict.fromkeys(factor(n))
    res = n
    for p in plst:
        res -= res//p
    return res

print(tot(int(input())))