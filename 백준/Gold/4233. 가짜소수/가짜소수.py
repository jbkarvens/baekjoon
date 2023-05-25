from random import randint
import math
MILLER_RABIN_TEST_LIST = [2,3,5,7]
PRIME_TEST_BOUND = 10000

def MR(n):
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
    return MR(n)

if __name__=='__main__':
    while True:
        p,a=map(int,input().split())
        if a==0:
            break
        if pow(a,p,p)==a and not isPrime(p):
            print('yes')
        else:
            print('no')
