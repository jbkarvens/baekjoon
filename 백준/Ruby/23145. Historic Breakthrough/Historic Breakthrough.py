import sys
from random import randint
import math

MR_TEST_LIST = [2,3,5,7,11,13,17,19,23]
PROBABILISTIC_LIMIT = 1000
SMALL_PRIME = 10000
input_func = sys.stdin.readline

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

def factor(n,m):
    if n<=1:
        return []
    if n%2==0:
        return [2]+factor(n//2,m)
    for i in range(3,SMALL_PRIME,2):
        if n%i==0:
            return [i]+factor(n//i,m)
    if isPrime(n):
        return [n]
    if n > 10**8:
        # phi(n)의 p-1, q-1들이 보통 2-지수가 다를 것임을 이용
        for _ in range(100):
            g = randint(2,m-2)
            gg = math.gcd(g,n)
            if 1<gg<n:
                return factor(gg,m) + factor(n//gg,m)
            g = pow(g, m, n)
            for _ in range(100):
                gg = math.gcd(g-1, n)
                if 1<gg<n:
                    return factor(gg,m) + factor(n//gg,m)
                g = (g*g)%n
        
    for _ in range(PROBABILISTIC_LIMIT):
        d = brent(n)
        if d!=1 and d!=n:
            break
    return factor(d,m) + factor(n//d,m)

def totient(n):
    tot = list(range(n + 1))
    for i in range(2, n + 1):
        if tot[i] != i:
            continue
        p = tot[i]
        for j in range(i, n + 1, i):
            tot[j] -= tot[j] // p
    return tot

def mysqrt(n):
    x = int(n**0.5)
    for _ in range(5):
        x = (x + n//x)//2
    if x**2<=n<(x+1)**2:
        return x
    else:
        return x+1

def solve(m,m_or):
    if m>2*10**28:
        for i in range(1,len(tot)):
            n = i*tot[i]
            if m%n==0:
                p = int(mysqrt(m//n))+1
                if m%p==0:
                    return solve(m//(p*(p-1)),m_or)*p
    if m==1:
        return 1
    plst = sorted(factor(m,m_or))
    p = plst.pop()
    e = 1
    while len(plst)>0 and plst[-1]==p:
        plst.pop()
        e+=1
    if p==2:
        return pow(2,(e+1)//2)
    return solve(m // (pow(p, e) * (p - 1)),m_or) * pow(p, (e + 1)//2)
    
if __name__=='__main__':
    tot = totient(10**4)
    for _ in range(int(input_func())):
        M = int(input_func())
        M_or=M
        while M_or%2==0:
            M_or//=2
        print(solve(2*M,M_or))