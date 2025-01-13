import sys
input=sys.stdin.readline

def initmax(s,e,n):
    if s==e:
        treemax[n]=arr[s]
        return treemax[n]
    m=(s+e)//2
    treemax[n]=max(initmax(s,m,2*n),initmax(m+1,e,2*n+1))
    return treemax[n]

def getmax(s,e,n,l,r):
    if r<s or e<l:
        return 0
    if l<=s<=e<=r:
        return treemax[n]
    m=(s+e)//2
    return max(getmax(s,m,2*n,l,r),getmax(m+1,e,2*n+1,l,r))

def initmin(s,e,n):
    if s==e:
        treemin[n]=arr[s]
        return treemin[n]
    m=(s+e)//2
    treemin[n]=min(initmin(s,m,2*n),initmin(m+1,e,2*n+1))
    return treemin[n]

def getmin(s,e,n,l,r):
    if r<s or e<l:
        return 10**10
    if l<=s<=e<=r:
        return treemin[n]
    m=(s+e)//2
    return min(getmin(s,m,2*n,l,r),getmin(m+1,e,2*n+1,l,r))

N,M=map(int,input().split())
arr=[]
treemax=[None]*(4*N)
treemin=[None]*(4*N)
for _ in range(N):
    arr.append(int(input()))
initmax(0,N-1,1)
initmin(0,N-1,1)
for _ in range(M):
    a,b=map(int,input().split())
    sys.stdout.write(f'{getmin(0,N-1,1,a-1,b-1)} {getmax(0,N-1,1,a-1,b-1)}\n')
    