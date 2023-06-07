import sys
import heapq
input=sys.stdin.readline

NUM=10**5
N,K=map(int,input().split())
h=[(0,N)]
parent=[None for _ in range(NUM+1)]
parent[N]=N
while h:
    d,x=heapq.heappop(h)
    if x-1>=0 and parent[x-1]==None:
        parent[x-1]=x
        heapq.heappush(h,(d+1,x-1))
    if x+1<=NUM and parent[x+1]==None:
        parent[x+1]=x
        heapq.heappush(h,(d+1,x+1))
    if 0<2*x<=NUM and parent[2*x]==None:
        parent[2*x]=x
        heapq.heappush(h,(d+1,2*x))
ans=[K]
cout=0
while K!=N:
    K=parent[K]
    ans.append(K)
    cout+=1
print(cout)
print(*ans[::-1])