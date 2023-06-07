import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
adj=[[] for _ in range(n+1)]
for _ in range(n-1):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
q=deque([1])
parent=[None for _ in range(n+1)]
parent[1]=1
while q:
    x=q.popleft()
    for v in adj[x]:
        if parent[v]!=None:
            continue
        parent[v]=x
        q.append(v)
for i in range(2,n+1):
    print(parent[i])