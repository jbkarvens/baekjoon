import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
M=int(input())
adj=[[] for _ in range(N+1)]
for _ in range(M):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
q=deque()
visited=[False for _ in range(N+1)]

visited[1]=True
cout=0
q.append(1)
while q:
    x=q.popleft()
    if not visited[x]:
        visited[x]=True
        cout+=1
    for v in adj[x]:
        if not visited[v]:
            q.append(v)
print(cout)