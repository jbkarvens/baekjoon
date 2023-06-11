import sys
from random import randint
import math

MR_TEST_LIST = [2,3,5,7,11,13,17,19,23,29]
PROBABILISTIC_LIMIT = 10000
SMALL_PRIME = 10000

input_func=sys.stdin.readline

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

def fib(n,m):
    if n==0:
        return 0
    a,b=1,1
    ls=[]
    while n>1:
        ls.append(n%2==1)
        n>>=1
    ls.reverse()
    for tf in ls:
        a,b=(a*(2*b-a))%m,(a*a+b*b)%m
        if tf:
            a,b=b,(a+b)%m
    return a

if __name__=='__main__':
    isstart=False
    while True:
        try:
            a,b=input_func().split()
            a=int(a,16)
            b=int(b,16)
            if a>=b:
                break
            if isstart:
                print()
            else:
                isstart=True
            print(f'Range {a} to {b}:')
            chk=False
            for i in range(94):
                f=fib(i,2**64)
                if a<=f<=b:
                    chk=True
                    if f!=0:
                        print(f'Fib({i}) = {f}, lg is {math.log2(f):.6f}')
                    else:
                        print(f'Fib({i}) = {f}, lg does not exist')
                    plst=sorted(factor(f))
                    if len(plst)==0:
                        print('No prime factors')
                    else:
                        print('Prime factors: ',end='')
                        print(*plst)
            if not chk:
                print('No Fibonacci numbers in the range')
        except:
            break