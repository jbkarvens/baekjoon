from random import randint
import math

MILLER_RABIN_TEST_LIST = [2,3,5,7,11,13,17,19,23]
MAX_NUM = 10**19
ECM_PRECISION = int(math.e**(1/2*math.sqrt(math.log(MAX_NUM)*math.log(math.log(MAX_NUM)))))
LITTLEWOOD_CONJECTURE_FALSE_LIST=[10, 34, 58, 85, 91, 130, 214, 226, 370, 526, 706, 730, 771, 1255, 1351, 1414, 1906, 2986, 3676, 9634, 21679]
SUM_OF_TWO_SQUARES_SMALL_BOUND=10000
PROBABILISTIC_TEST_LIMIT = 10000
PRIME_TEST_BOUND = 1000000

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

def factor_prime(n):
    if n<PRIME_TEST_BOUND:
        return sorted(factor_small(n))
    if n%2==0:
        result = [2]+factor_prime(n//2)
        return sorted(result)
    else:
        k=3
        while k<100:
            if n%k==0:
                result = [k]+factor_prime(n//k)
                return sorted(result)
            k+=2
    if isPrime(n):
        return [n]
    a=brent(n)
    b=n//a
    result=factor_prime(a)+factor_prime(b)
    return sorted(result)

def solve_sum_of_squares(n):
    if n==int(n**0.5)**2:
        return 1
    
    lst=factor_prime(n)
    while len(lst)>0:
        if len(lst)>=2:
            if lst[0]==lst[1]:
                lst.remove(lst[0])
                lst.remove(lst[0])
                continue
        if lst[0]==2 or lst[0]%4==1:
            lst.remove(lst[0])
        else:
            break
    if len(lst)==0:
        return 2
    
    s,tmp=0,n
    while tmp%4==0:
        tmp>>=2
        s+=1
    d=n>>(2*s)
    if d%8!=7:
        return 3
    else:
        return 4

if __name__=='__main__':
    print(solve_sum_of_squares(int(input())))