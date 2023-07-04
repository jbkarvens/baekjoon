import sys
from random import randint
from math import gcd
input=sys.stdin.readline
SMALL_NUM = 1000

def isPrime(n):
    s,d=0,n-1
    while not d&1:
        s+=1
        d>>=1
    for a in [2,3,5,7,11,13,17,19,23]:
        ap=pow(a,d,n)
        if ap==1:
            continue
        a_witness=False
        for i in range(s):
            if ap==n-1:
                a_witness=True
                break
            else:
                ap=pow(ap,2,n)
        if a_witness:
            continue
        else:
            return False
    return True

def factor(n):
    if n==1:
        return []
    for i in range(2,SMALL_NUM):
        if n%i==0:
            if n==i:
                return [n]
            else:
                return sorted(factor(i)+factor(n//i))
    if isPrime(n):
        return [n]
    for _ in range(100):
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
            g=gcd(q,n)
            r*=2
        if g==n:
            while True:
                ys=(ys*ys+c)%n
                g=gcd(x-ys,n)
                if g>1:
                    break
        if g==1 or g==n:
            continue
        else:
            break
    return sorted(factor(g)+factor(n//g))

def solve(n,A):
    prime_dict={}
    for index,number in enumerate(A):
        prime_factors = set(factor(number))
        for p in prime_factors:
            if p in prime_dict:
                prime_dict[p].append(index)
            else:
                prime_dict[p]=[index]
    for p in prime_dict:
        prime_dict[p].sort()
    sg = 0
    for p in prime_dict:
        sg_p=0
        count = 0
        i_before=prime_dict[p][0]-1
        for i in prime_dict[p]:
            if i - i_before==1:
                count+=1
            else:
                sg_p^=count
                count=1
            i_before=i
        sg_p^=count
        sg^=sg_p
    if sg!=0:
        return 0
    else:
        return 1

if __name__=='__main__':
    n = int(input())
    A = map(int,input().split())
    if solve(n,A):
        print('Second')
    else:
        print('First')