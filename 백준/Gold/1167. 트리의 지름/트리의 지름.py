import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
adj=[[] for _ in range(n+1)]
for _ in range(1,n+1):
    lst=list(map(int,input().split()))
    i=lst[0]
    j=1
    while lst[j]!=-1:
        adj[i].append([lst[j],lst[j+1]])
        j+=2

a=1
q=deque([a])
dist=[None for _ in range(n+1)]
dist[a]=0
far_from_a,record=a,0
while q:
    x=q.popleft()
    for v,c in adj[x]:
        if dist[v]!=None:
            continue
        dist[v]=dist[x]+c
        if dist[v]>record:
            far_from_a=v
            record=dist[v]
        q.append(v)

b=far_from_a
q=deque([b])
dist=[None for _ in range(n+1)]
dist[b]=0
while q:
    x=q.popleft()
    for v,c in adj[x]:
        if dist[v]!=None:
            continue
        dist[v]=dist[x]+c
        q.append(v)
print(max(dist[1:]))