import sys
sys.setrecursionlimit(2*10**5+1)
input=sys.stdin.readline

def dfs(R):
    ans[R]=cout[0]
    visited[R]=True
    cout[0]+=1
    for x in edge[R]:
        if not visited[x]:
            dfs(x)

N,M,R=map(int,input().split())
edge=[[] for _ in range(N+1)]
visited=[False for _ in range(N+1)]
ans=[0 for _ in range(N+1)]
cout=[1]
for _ in range(M):
    u,v=map(int,input().split())
    edge[u].append(v)
    edge[v].append(u)
for v in edge:
    v.sort(reverse=True)
dfs(R)
for i in range(1,N+1):
    print(ans[i])