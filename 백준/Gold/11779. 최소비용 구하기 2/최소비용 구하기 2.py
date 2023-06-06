import sys
import heapq

def Dijkstra(start,N,adj,INF=10**18,give_dir=False):
    h=[(0,start)]
    d=[INF for _ in range(N+1)]
    d[start]=0
    if give_dir:
        path=[[] for _ in range(N+1)]
        path[start]=[start]
    while h:
        d_v,v=heapq.heappop(h)
        if d_v>d[v]:
            continue
        for w,d_vw in adj[v]:
            d_w=d_v+d_vw
            if d_w<d[w]:
                d[w]=d_w
                if give_dir:
                    path[w]=path[v]+[w]
                heapq.heappush(h,(d_w,w))
    if give_dir:
        return d,path
    else:
        return d
    
input=sys.stdin.readline
N=int(input())
M=int(input())
adj=[[] for _ in range(N+1)]
for _ in range(M):
    v,w,c=map(int,input().split())
    adj[v].append((w,c))
start,end=map(int,input().split())
d,path=Dijkstra(start,N,adj,give_dir=True)
print(d[end])
print(len(path[end]))
print(*path[end])