import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

casenum=1
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    adj=[[] for _ in range(n+1)]
    for i in range(m):
        u,v=map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)
    visited=[False for _ in range(n+1)]
    cout=0
    for i in range(1,n+1):
        if visited[i]:
            continue
        chktree=True
        q=deque()
        q.append(i)
        while q:
            x=q.popleft()
            if visited[x]:
                chktree=False
            visited[x]=True
            for v in adj[x]:
                if not visited[v]:
                    q.append(v)
        if chktree:
            cout+=1
    
    if cout==0:
        print(f'Case {casenum}: No trees.')
    elif cout==1:
        print(f'Case {casenum}: There is one tree.')
    else:
        print(f'Case {casenum}: A forest of {cout} trees.')
    
    casenum+=1