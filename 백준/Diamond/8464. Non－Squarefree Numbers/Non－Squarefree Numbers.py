import sys
from random import randint
import math
input_func=sys.stdin.readline

MILLER_RABIN_TEST_LIST = [2,3,5,7,11,13,17,19,23]
ZETA2=1.6449340668482264
SMALL_NUM=100
PROBABILISTIC_TEST_LIMIT = 10000
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
    result=factor(a)+factor(b)
    return sorted(result)

def cal_for_small(N):
    plst=[True for i in range(N+1)]
    Mobius_lst=[1 for _ in range(N+1)]
    
    Mobius_lst[2]=-1
    for j in range(2+2,N+1,2):
        plst[j]=False
        if j%4!=0:
            Mobius_lst[j]=-Mobius_lst[j]
        else:
            Mobius_lst[j]=0
    for i in range(3,N+1,2):
        if plst[i]:
            Mobius_lst[i]=-1
            i2=i*i
            for j in range(i+i,N+1,i):
                plst[j]=False
                if j%i2!=0:
                    Mobius_lst[j]=-Mobius_lst[j]
                else:
                    Mobius_lst[j]=0
    del plst
    return Mobius_lst

def S(N):
    L=int(N**(1/5))//2
    D=int((N/L)**0.5)
    
    result=0
    
    Mobius_lst=cal_for_small(D)
    M_lst=[None for _ in range(D+1)]
    s=0
    for i in range(1,D+1):
        s+=Mobius_lst[i]
        M_lst[i]=s
    
    for i in range(1,D+1):
        result+=Mobius_lst[i]*(N//(i*i))

    M_other=[0 for _ in range(L+1)]
    for i in reversed(range(1,L)):
        Mx=1
        x=int((N/i)**0.5)
        cut=int(x**0.5)
        for j in range(1,x//(cut+1)+1):
            Mx-=M_lst[j]*(x//j-x//(j+1))
        for j in range(2,cut+1):
            if x//j<=D:
                Mx-=M_lst[x//j]
            else:
                Mx-=M_other[i*j*j]
        M_other[i]=Mx
        result+=Mx
        
    result-=(L-1)*M_lst[D]
    return result

def isSF(N):
    for i in range(2,100):
        if N%(i*i)==0:
            return False
    plst=factor(N)
    while len(plst)>=2:
        if plst[0]==plst[1]:
            return False
        else:
            plst.remove(plst[0])
            plst.remove(plst[0])
    return True

def get_ans(N):
    if N<=SMALL_NUM:
        Mobius_lst=cal_for_small(10*SMALL_NUM)
        s=0
        for i in range(1,len(Mobius_lst)):
            if Mobius_lst[i]==0:
                s+=1
            if s==N:
                return i
            
    M=int(1/(1-1/ZETA2)*N)
    N2=M-S(M)
    if N2==N:
        while isSF(M):
            M-=1
        return M
    elif N2<N:
        while N2<N:
            M+=1
            if not isSF(M):
                N2+=1
        return M
    else:
        while N2>=N:
            if not isSF(M):
                N2-=1
            M-=1    
        return M+1

if __name__=='__main__':
    print(get_ans(int(input_func())))