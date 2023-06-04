import sys
import heapq
input=sys.stdin.readline

INF=10**7
N,M=map(int,input().split())
adj=[[] for _ in range(N+1)]
for _ in range(M):
    u,v,w=map(int,input().split())
    adj[u].append((v,w))
    adj[v].append((u,w))
K,L=map(int,input().split())

def dijk(node,d):
    heap=[(0,node)]
    while heap:
        cost_v,v=heapq.heappop(heap)
        if cost_v>d[v]:
            continue
        for w,cost_vw in adj[v]:
            dist=cost_v+cost_vw
            if dist<d[w]:
                heapq.heappush(heap,(dist,w))
                d[w]=dist      

d=[INF for _ in range(N+1)]
d[1]=0
dijk(1,d)
d_1K=d[K]
d_1L=d[L]

d=[INF for _ in range(N+1)]
d[K]=0
dijk(K,d)
d_KL=d[L]
d_KN=d[N]

d=[INF for _ in range(N+1)]
d[L]=0
dijk(L,d)
d_LK=d[K]
d_LN=d[N]

ans=min(d_1K+d_KL+d_LN,d_1L+d_LK+d_KN)
if ans>=INF:
    print(-1)
else:
    print(ans)