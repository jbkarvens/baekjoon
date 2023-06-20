import sys
input=sys.stdin.readline

import math
from random import randint

PROBABILISTIC_LIMIT = 10000
SMALL_PRIME=1000
MR_TEST_LIST=[2,3,5,7,11,13,17,19,23,29]

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

def get_div(pfac,idx,div):
    k=len(idx)
    if len(idx)==len(pfac):
        cur = 1
        for i in range(k):
            cur*=pow(pfac[i][0],idx[i])
        div.append(cur)
        return
    for i in range(pfac[k][1]+1):
        get_div(pfac,idx+[i],div)

def divisor(prime_list):
    div = []
    pfac = []
    for p in prime_list:
        if len(pfac)==0 or pfac[-1][0]!=p:
            pfac.append([p,1])
        else:
            pfac[-1][1]+=1
    get_div(pfac,[],div)
    div.sort()
    return div

def find(x,lst):
    low,high=0,len(lst)-1
    while low<=high:
        mid = (low+high)//2
        if lst[mid]<=x:
            low = mid+1
        else:
            high = mid-1
    return high

def solve(prime_list):
    divisors = divisor(prime_list)
    N = divisors[-1]
    ans = 2+N
    for d in divisors:
        if d+2*math.sqrt(N/d)>ans:
            continue
        if d**3>N:
            break
        if ans<3*d:
            break
        for u in reversed(divisors[:1 + find(int(math.sqrt(N/d)),divisors)]):
            if N%(d*u)!=0:
                continue
            v = N//(d*u)
            ans = min(d+u+v,ans)
            break
    return ans

if __name__=='__main__':
    while True:
        N = int(input())
        if N==0:
            break
        sys.stdout.write(f'{solve(factor(N))}\n')
        