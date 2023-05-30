import sys
sys.setrecursionlimit(10**6)
def dfs(m,n):
    M,N=len(h),len(h[0])
    if dp[m][n]!=None:
        return dp[m][n]
    if m==M-1 and n==N-1:
        return 1
    res=0
    for dm,dn in [(-1,0),(1,0),(0,1),(0,-1)]:
        if 0<=m+dm<M and 0<=n+dn<N and h[m+dm][n+dn]<h[m][n]:
            res+=dfs(m+dm,n+dn)
    dp[m][n]=res
    return res

M,N=map(int,input().split())
h=[]
for _ in range(M):
    h.append(list(map(int,input().split())))

dp=[[None for _ in range(N)] for _ in range(M)]
print(dfs(0,0))