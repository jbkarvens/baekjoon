PROBABILISTIC_LIMIT = 10000
SMALL_PRIME=1000
MR_TEST_LIST=[2,3,5,7]
import math
from random import randint

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
    for _ in range(PROBABILISTIC_LIMIT):
        d=brent(n)
        if d==n:
            continue
        else:
            return factor(d)+factor(n//d)

NUM=10**9+7
n,x,y,m=map(int,input().split())
x_fac=factor(abs(x))
y_fac=factor(abs(y))
p_lst=dict()
for p in factor(abs(x+y)):
    if p in p_lst:
        p_lst[p]+=1
    elif not(p in x_fac) and not(p in y_fac):
        p_lst[p]=1
for q in factor(n):
    if q in p_lst:
        p_lst[q]+=1
rst=[]
for p in p_lst:
    rst.append((p,p_lst[p]//m))
z_cout=1
for p,r in rst:
    z_cout=(z_cout*(r+1))%NUM
z_sum=1
for p,r in rst:
    tmp=0
    for i in range(r+1):
        tmp+=pow(p,m*i,NUM)
    z_sum=(z_sum*tmp)%NUM
print(z_cout,z_sum)