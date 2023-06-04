import sys
import heapq
input=sys.stdin.readline

INF=10**7
N,M=map(int,input().split())
K=int(input())
adj=[[] for _ in range(N+1)]
for _ in range(M):
    u,v,w=map(int,input().split())
    adj[u].append((v,w))
d=[INF for _ in range(N+1)]

d[K]=0
heap=[(0,K)]
while heap:
    cost_v,v=heapq.heappop(heap)
    if cost_v>d[v]:
        continue
    for w,cost_vw in adj[v]:
        dist=cost_v+cost_vw
        if dist<d[w]:
            heapq.heappush(heap,(dist,w))
            d[w]=dist
for v in range(1,N+1):
    if d[v]==INF:
        print('INF')
    else:
        print(d[v])