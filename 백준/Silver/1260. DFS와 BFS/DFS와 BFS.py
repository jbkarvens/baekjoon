import sys
from collections import deque
sys.setrecursionlimit(10**4)
input=sys.stdin.readline

N,M,R=map(int,input().split())
adj=[[] for _ in range(N+1)]
for _ in range(M):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
for i in range(1,N+1):
    adj[i].sort()

ans_dfs=[]
visited=[False for _ in range(N+1)]

def dfs(R):
    visited[R]=True
    ans_dfs.append(R)
    for v in adj[R]:
        if not visited[v]:
            dfs(v)
            
dfs(R)

ans_bfs=[]
visited=[False for _ in range(N+1)]
q=deque()
q.append(R)
visited[R]=True
ans_bfs.append(R)
while q:
    x=q.popleft()
    if not visited[x]:
        visited[x]=True
        ans_bfs.append(x)
    for v in adj[x]:
        if not visited[v]:
            q.append(v)
print(*ans_dfs)
print(*ans_bfs)