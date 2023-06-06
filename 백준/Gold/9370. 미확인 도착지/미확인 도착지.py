import sys
import heapq
input=sys.stdin.readline

INF=[10**8]

def dijk(node):
    N=len(adj)-1
    d=[INF[0] for _ in range(N+1)]
    d[node]=0
    h=[(0,node)]
    while h:
        c_v,v=heapq.heappop(h)
        if c_v>d[v]:
            continue
        for w,c_vw in adj[v]:
            c_w=c_v+c_vw
            if c_w<d[w]:
                d[w]=c_w
                heapq.heappush(h,(c_w,w))
    return d

for _ in range(int(input())):
    N,M,T=map(int,input().split())
    S,G,H=map(int,input().split())
    adj=[[] for _ in range(N+1)]
    for _ in range(M):
        a,b,d=map(int,input().split())
        adj[a].append((b,d))
        adj[b].append((a,d))
    end=[]
    for _ in range(T):
        end.append(int(input()))
    
    dS=dijk(S)
    dG=dijk(G)
    dH=dijk(H)
    for v,c in adj[G]:
        if v==H:
            dGH=c
    ans=[]
    for node in end:
        if dS[node]==dS[G]+dGH+dH[node] or dS[node]==dS[H]+dGH+dG[node]:
            ans.append(node)
    ans.sort()
    print(*ans)