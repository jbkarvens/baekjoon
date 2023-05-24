PROBABILISTIC_LIMIT = 10000
SMALL_PRIME=1000
MR_TEST_LIST=[2,3,5,7]
p_fac=[]
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
        
def get_gen(p):
    prime_in_p=dict.fromkeys(p_fac)
    for _ in range(PROBABILISTIC_LIMIT):
        g=randint(1,p-1)
        chk=True
        for q in prime_in_p:
            if pow(g,(p-1)//q,p)==1:
                chk=False
        if chk:
            return g

def solve_dl(a,g,p):
    for _ in range(PROBABILISTIC_LIMIT):  
        t=int(p**0.5)+1
        g_dict={}
        gi=1
        gt=pow(g,t,p)
        g_dict[gi]=0
        for i in range(1,t):
            gi=(gi*gt)%p
            g_dict[gi]=i
        hi=a
        for i in range(t):
            if hi in g_dict:
                return (g_dict[hi]*t-i)%(p-1)
            hi=(hi*g)%p
    
for _ in range(int(input())):
    p,a,m=map(int,input().split())
    if a==0:
        print('TAK '+str(p))
        continue
    if m%(p-1)==0 and a==1:
        print('NIE')
        continue
    if p<50:
        chk=True
        for i in range(1,50**3):
            if (pow(i,i,p)+pow(i,m,p))%p==a:
                print('TAK '+str(i))
                chk=False
                break
        if chk:
            print('NIE')
        continue
    p_fac=factor(p-1)
    for _ in range(PROBABILISTIC_LIMIT):
        g=get_gen(p)
        if pow(g,m,p)!=a:
            break
    d=solve_dl((a-pow(g,m,p))%p,g,p)
    n=(d-g)%(p-1)*p+g
    if (pow(n,n,p)+pow(n,m,p))%p!=a:
        print(f'p:{p} a:{a} m:{m} n:{n} d:{d} g:{g}')
        raise Exception('Failed2')
    print('TAK '+str(n))