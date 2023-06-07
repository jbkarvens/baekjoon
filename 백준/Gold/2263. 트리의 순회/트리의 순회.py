import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n=int(input())
inord=list(map(int,input().split()))
postord=list(map(int,input().split()))
idxlst=[None for _ in range(n+1)]
for i in range(n):
    idxlst[inord[i]]=i

ans=[]
def work(a,b,c,d):
    if a>b or c>d:
        return
    root=postord[d]
    idx=idxlst[root]
    ans.append(root)
    work(a,idx-1,c,idx-1+c-a)
    work(idx+1,b,idx+c-a,d-1)

work(0,n-1,0,n-1)
print(*ans)