import sys
from collections import deque
input=sys.stdin.readline

def bfs(N):
    color=[None for _ in range(N+1)]
    for i in range(1,N+1):
        if color[i]!=None:
            continue
        color[i]=0
        q=deque()
        q.append(i)
        while q:
            x=q.popleft()
            for y in adj[x]:
                if color[y]==None:
                    color[y]=1-color[x]
                    q.append(y)
                elif color[y]==color[x]:
                    return False
    return True

for _ in range(int(input())):
    N,M=map(int,input().split())
    adj=[[] for _ in range(N+1)]
    for _ in range(M):
        u,v=map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)
    if bfs(N):
        print("YES")
    else:
        print("NO")