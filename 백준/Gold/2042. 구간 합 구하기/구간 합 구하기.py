import sys
input=sys.stdin.readline

def init(s,e,n):
    if s==e:
        seg[n]=arr[s]
        return seg[n]
    m=(s+e)//2
    seg[n]=init(s,m,2*n)+init(m+1,e,2*n+1)
    return seg[n]

def getsum(s,e,n,l,r):
    if l>e or r<s:
        return 0
    if l<=s and e<=r:
        return seg[n]
    m=(s+e)//2
    return getsum(s,m,2*n,l,r)+getsum(m+1,e,2*n+1,l,r)

def doupdate(s,e,n,i,d):
    if i<s or i>e:
        return
    seg[n]+=d
    if s==e:
        return
    m=(s+e)//2
    doupdate(s,m,2*n,i,d)
    doupdate(m+1,e,2*n+1,i,d)

N,M,K=map(int,input().split())
seg=[None]*(4*N)
arr=[]
for _ in range(N):
    arr.append(int(input()))
init(0,N-1,1)
for _ in range(M+K):
    a,b,c=map(int,input().split())
    if a==1:
        doupdate(0,N-1,1,b-1,c-arr[b-1])
        arr[b-1]=c
    elif a==2:
        x=getsum(0,N-1,1,b-1,c-1)
        sys.stdout.write(f'{x}\n')
    