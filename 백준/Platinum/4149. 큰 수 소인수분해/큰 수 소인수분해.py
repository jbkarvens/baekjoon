from random import randint
import math

MILLER_RABIN_TEST_LIST = [2,3,5,7,11,13,17,19,23]
MAX_NUM = 2**62
ECM_PRECISION = int(math.e**(1/2*math.sqrt(math.log(MAX_NUM)*math.log(math.log(MAX_NUM)))))
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

def prime_sieve(n):
    prime_chk=[True for _ in range(n+1)]
    for i in range(2,n+1):
        if prime_chk[i]:
            j=i+i
            while j<=n:
                prime_chk[j]=False
                j+=i
    return [i for i in range(2,n+1) if prime_chk[i]]

class InvException(Exception):
    def __init__(self,d):
        self.d=d

def inv(a,n):
    d=math.gcd(a,n)
    if d>1:
        raise InvException(d)
    else:
        return pow(a,-1,n)

class elliptic_point:
    def __init__(self,N,A,B,X,Y):
        if (Y*Y-X*X*X-A*X-B)%N!=0:
            raise Exception('ERROR : Point not on Elliptic Curve')
        self.N = N
        self.A, self.B = A, B
        self.X, self.Y = X, Y
        
    def __add__(self,other):
        N,A,B=self.N,self.A,self.B
        x0,y0,x1,y1=self.X,self.Y,other.X,other.Y
        if x0==x1 and y0==y1:
            s = ((3*x0*x0+A)*inv(2*y0,N))%N
        else:
            s = ((y1-y0)*inv(x1-x0,N))%N
        x=(s*s-x0-x1)%N
        y=(s*(x-x0)+y0)%N
        return elliptic_point(N,A,B,x,y)
    
    def __rmul__(self,other):
        k=other
        P=self
        if k&(k-1)==0:
            while k>1:
                P=P+P
                k>>=1
            return P
        k-=1
        while k>=1:
            P=P+P
            if k&1:
                P=P+self
            k>>=1
        return P
        
        

def ECM(n):
    prime_lst=prime_sieve(ECM_PRECISION)
    for _ in range(PROBABILISTIC_TEST_LIMIT):
        a=randint(1,n)
        x=randint(1,n)
        y=randint(1,n)
        b=(y*y-x**3-a*x)%n
        if a%n==0 or b%n==0:
            continue
        P=elliptic_point(n,a,b,x,y)
        for k in prime_lst:
            if k*k<=ECM_PRECISION:
                k=k**int(math.log(ECM_PRECISION)/math.log(k))
            try:
                P=k*P
            except InvException as e:
                d=e.d
                if d==n or d==1:
                    continue
                else:
                    return d, n//d
    raise Exception('ERROR : ECM Failed in Probabilistic limit')


def Pollard(n):
    b=2
    if n%b==0:
        return b,n//b
    k=2
    d=1
    while True:
        b=pow(b,k,n)
        d=math.gcd(n,b-1)
        if d>1:
            break
        k+=1
    return d,n//d

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
        return factor_small(n)
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
    a,b=ECM(n)
    # a=brent(n)
    b=n//a
    result=factor_prime(a)+factor_prime(b)
    return sorted(result)

if __name__=='__main__':
    n=int(input())
    lst=sorted(factor_prime(n))
    for p in lst:
        print(p)