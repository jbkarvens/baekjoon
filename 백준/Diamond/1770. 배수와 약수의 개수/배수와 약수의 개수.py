from random import randint
import math
MILLER_RABIN_TEST_LIST = [2,3,5,7,11,13,17,19,23,29,31,37,41]
PRIME_TEST_BOUND = 10000

def Miller_Rabin(n):
    if n<=MILLER_RABIN_TEST_LIST[-1]:
        if n in MILLER_RABIN_TEST_LIST:
            return True
        else: return False
    s,tmp=0,n-1
    while tmp&1==0:
        tmp>>=1
        s+=1
    d=(n-1)>>s
    for a in MILLER_RABIN_TEST_LIST:
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
    if n<PRIME_TEST_BOUND:
        if n<=1:
            return False
        elif n==2:
            return True
        elif n%2==0:
            return False
        i=3
        while i*i<=n:
            if n%i==0: return False
            if i%6==1:
                i+=4
            else:
                i+=2
        return True
    else:
        if n%2==0:
            return False
        for k in range(3,100,2):
            if n%k==0:
                return False
    return Miller_Rabin(n)

def brent(N):
        if N%2==0:
                return 2
        y,c,m = randint(1, N-1),randint(1, N-1),randint(1, N-1)
        g,r,q = 1,1,1
        while g==1:             
                x = y
                for i in range(r):
                        y = ((y*y)%N+c)%N
                k = 0
                while (k<r and g==1):
                        ys = y
                        for i in range(min(m,r-k)):
                                y = ((y*y)%N+c)%N
                                q = q*(abs(x-y))%N
                        g = math.gcd(q,N)
                        k = k + m
                r = r*2
        if g==N:
                while True:
                        ys = ((ys*ys)%N+c)%N
                        g = math.gcd(abs(x-ys),N)
                        if g>1:
                                break
        
        return g 

def factor_small(n):
    if 1<=n<=3:
        return [n]
    if n%2==0:
        return [2]+factor_small(n//2)
    i=3
    while i*i<=n:
        if n%i==0: return [i]+factor_small(n//i)
        if i%6==1:
            i+=4
        else:
            i+=2
    return [n]

def factor(n):
    if n<PRIME_TEST_BOUND:
        return factor_small(n)
    if n%2==0:
        result = [2]+factor(n//2)
        return sorted(result)
    else:
        k=3
        while k<100:
            if n%k==0:
                result = [k]+factor(n//k)
                return sorted(result)
            k+=2
    if isPrime(n):
        return [n]
    a=brent(n)
    b=n//a
    while a==n:
        a=brent(n)
        b=n//a
    result=factor(a)+factor(b)
    return sorted(result)

def solve(n):
    if n==1 or n==4:
        return 1
    if isPrime(n):
        return 1
    fac=factor(n)
    fac=sorted(fac)
    for i in range(len(fac)-1):
        if fac[i]==fac[i+1]:
            return -1
    ans=1
    for i in range(1,len(fac)+1):
        ans*=i
    return ans
    

if __name__=='__main__':
    for _ in range(int(input())):
        print(solve(int(input())))