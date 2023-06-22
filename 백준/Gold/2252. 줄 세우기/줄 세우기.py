import sys
input=sys.stdin.readline
from collections import deque

if __name__=='__main__':
    n,m = map(int, input().split())
    adj=[[] for _ in range(n+1)]
    in_degree = [0 for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int, input().split())
        adj[a].append(b)
        in_degree[b]+=1
    q = deque()
    result = []
    for i in range(1,n+1):
        if in_degree[i]==0:
            q.append(i)
    while q:
        node = q.popleft()
        result.append(node)
        for vertex in adj[node]:
            in_degree[vertex]-=1
            if in_degree[vertex]==0:
                q.append(vertex)
    print(*result)