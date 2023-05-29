import sys
import math
input=sys.stdin.readline

N=2**20
def fft(x,mode=True):
    n=len(x)
    n_log=int(math.log2(n))
    X=[None for _ in range(n)]
    for i in range(n):
        tmp=0
        j=i
        for _ in range(n_log):
            tmp=(tmp<<1)|(j&1)
            j>>=1
        X[tmp]=x[i]
    for s in range(n_log):
        m=2**(s+1)
        g=math.cos(-2*math.pi/m)+1j*math.sin(-2*math.pi/m)*(1 if mode==True else -1)
        for k in range(0,n,m):
            w=1
            for j in range(m//2):
                t=w*X[k+j+m//2]
                u=X[k+j]
                X[k+j]=u+t
                X[k+j+m//2]=u-t
                w*=g
    return X

def primes(n):
    lst=[1 for _ in range(n+1)]
    lst[0],lst[1]=0,0
    j=2+2
    while j<=n:
        lst[j]=0
        j+=2
    for i in range(3,n+1,2):
        if lst[i]==1:
            j=i+i
            while j<=n:
                lst[j]=0
                j+=i
    return lst

B=primes(N-1)
A=[0 for _ in range(N//2)]
for i in range(N//2):
    if B[2*i+1]==1:
        A[i]=1
    else:
        A[i]=0
A=A+[0 for _ in range(N//2)]
A=fft(A)
A=[A[i]*A[i] for i in range(len(A))]
A=[round(v.real/N) for v in fft(A,False)]
for _ in range(int(input())):
    n=int(input())
    if n==4:
        print(1)
    else:
        print((A[n//2-1]+1)//2)