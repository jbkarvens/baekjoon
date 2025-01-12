import sys
input=sys.stdin.readline

def init(s,e,n):
    global mod
    if s==e:
        seg[n]=arr[s]
        return seg[n]
    m=(s+e)//2
    seg[n]=(init(s,m,2*n)*init(m+1,e,2*n+1))%mod
    return seg[n]

def getprod(s,e,n,l,r):
    global mod
    if e<l or r<s:
        return 1
    if l<=s and e<=r:
        return seg[n]
    m=(s+e)//2
    return (getprod(s,m,2*n,l,r)*getprod(m+1,e,2*n+1,l,r))%mod

def doupdate(s,e,n,i,d):
    global mod
    if i<s or e<i:
        return
    seg[n]=(seg[n]*d)%mod
    if s==e:
        return
    m=(s+e)//2
    doupdate(s,m,2*n,i,d)
    doupdate(m+1,e,2*n+1,i,d)

mod=10**9+7
N,M,K=map(int,input().split())
seg=[None]*(4*N)
arr=[]
for _ in range(N):
    arr.append(int(input()))
init(0,N-1,1)
for _ in range(M+K):
    a,b,c=map(int,input().split())
    if a==1:
        if arr[b-1]==0:
            arr[b-1]=c
            init(0,N-1,1)
        else:
            doupdate(0,N-1,1,b-1,c*pow(arr[b-1],-1,mod))
            arr[b-1]=c
    elif a==2:
        x=getprod(0,N-1,1,b-1,c-1)
        sys.stdout.write(f'{x}\n')
    