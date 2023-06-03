import sys
from collections import deque
sys.setrecursionlimit(2*10**5+1)
input=sys.stdin.readline

def bfs(V,E,R):
    for v in V:
        if v==R:continue
        visited[v]=False
    visited[R]=True
    ans[R]=cout[0]
    cout[0]+=1
    q=deque()
    q.append(R)
    while q:
        u=q.popleft()
        for v in E[u]:
            if not visited[v]:
                visited[v]=True
                ans[v]=cout[0]
                cout[0]+=1
                q.append(v)
    

N,M,R=map(int,input().split())
edge=[[] for _ in range(N+1)]
visited=[None for _ in range(N+1)]
ans=[0 for _ in range(N+1)]
cout=[1]
for _ in range(M):
    u,v=map(int,input().split())
    edge[u].append(v)
    edge[v].append(u)
for v in edge:
    v.sort()
bfs(list(range(1,N+1)),edge,R)
for i in range(1,N+1):
    print(ans[i])