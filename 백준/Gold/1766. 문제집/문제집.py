import sys
input=sys.stdin.readline
import heapq

if __name__=='__main__':
    N,M=map(int,input().split())
    adj = [[] for _ in range(N+1)]
    in_degree = [0 for _ in range(N+1)]
    for _ in range(M):
        a,b=map(int, input().split())
        adj[a].append(b)
        in_degree[b]+=1
    q=[]
    for node in range(1,N+1):
        if in_degree[node]==0:
            heapq.heappush(q,node)
    ans = []
    while q:
        node = heapq.heappop(q)
        ans.append(node)
        for v in adj[node]:
            in_degree[v]-=1
            if in_degree[v]==0:
                heapq.heappush(q,v)
    print(*ans)