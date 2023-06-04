import sys
import heapq
input=sys.stdin.readline

INF=2*10**5
N,K=map(int,input().split())
M=max(N,K)*2+1
adj=[None for _ in range(M)]
for i in range(M):
    adj[i]=[(1,i-1),(1,i+1),(0,2*i)]
h=[(0,N)]
d=[INF for _ in range(M)]
d[N]=0
while h:
    cost_v,v=heapq.heappop(h)
    if cost_v>d[v]:
        continue
    for cost_vw,w in adj[v]:
        cost_w=cost_v+cost_vw
        if not 0<=w<M:
            continue
        if cost_w<d[w]:
            d[w]=cost_w
            heapq.heappush(h,(cost_w,w))
print(d[K])