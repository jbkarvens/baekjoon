import sys
input=sys.stdin.readline
import math
from random import randint

MR_TEST_LIST = [2,3,5,7,11,13,17,19]
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

def isPrime(n):
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

def crt(rem,mod):
    tot = 1
    for m in mod:
        tot *= m
    res = 0
    for r,m in zip(rem,mod):
        mm=tot//m
        res+=r*mm*pow(mm,-1,m)
    return res%tot

def naive_factorial(n,mod,p):
    res = 1
    for i in range(2,n+1):
        if i%p==0:
            continue
        res = (res*i)%mod
    return res

# p 배수 제외하고 곱한 팩토리얼
def factorial_without_p(n,p,e):
    if p==2:
        if e==1:
            return 1
        elif e==2:
            mod =4
            q,r=divmod(n,mod)
            res = pow(-1,q)
            if r==3:
                res = -res
            return res%mod
    pp=pow(p,(e+1)//2)
    q,r=divmod(n,pp)
    mod=pow(p,e)
    res = pow(naive_factorial(pp-1,mod,p),q,mod)
    for i in range(q*pp+1,n+1):
        if i%p==0:
            continue
        res = (res*i)%mod
    return res

def factorial_dmod(n,p,e):
    res = 1
    while n>0:
        res=(res*factorial_without_p(n, p,e))%pow(p,e)
        n//=p
    return res

def factorial_pval(n,p):
    res = 0
    while n>0:
        n//=p
        res+=n
    return res

def binom(m,n,d):
    primes=factor(d)
    factors=dict()
    for p in primes:
        if p in factors:
            factors[p]+=1
        else:
            factors[p]=1
    mod = []
    rem = []
    pval=[]
    pval_d = []
    prime_list = []
    for p in factors:
        e = factors[p]
        pp=pow(p,e)
        mod.append(pp)
        rem.append((factorial_dmod(m,p,e)*pow(factorial_dmod(n,p,e)*factorial_dmod(m-n,p,e),-1,pp))%pp)
        pval.append(factorial_pval(m,p)-factorial_pval(n,p)-factorial_pval(m-n, p))
        pval_d.append(factors[p])
        prime_list.append(p)
    h = min([e//f for e,f in zip(pval,pval_d)])
    for i in range(len(pval)):
        pval[i]-=h*pval_d[i]
        rem[i]=(rem[i]*pow(prime_list[i],pval[i])*pow(d//mod[i],-h,mod[i]))%mod[i]
    return crt(rem,mod)

if __name__=='__main__':
    f1,f2={},{}
    m,n,d=map(int, input().split())
    print(binom(m,n,d))