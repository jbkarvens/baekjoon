import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
Z=100
ldr=[]
snk=[]
for _ in range(N):
    ldr.append(list(map(int,input().split())))
for _ in range(M):
    snk.append(list(map(int,input().split())))
q=deque()
q.append(1)
visited=[None for _ in range(Z+1)]
visited[1]=0
while q:
    x=q.popleft()
    if x==Z:
        break
    for lst in ldr:
        if lst[0]==x:
            visited[lst[1]]=visited[x]
            x=lst[1]
    for lst in snk:
        if lst[0]==x:
            visited[lst[1]]=visited[x]
            x=lst[1]
    for dx in range(1,6+1):
        xp=x+dx
        if xp<=Z and visited[xp]==None:
            visited[xp]=visited[x]+1
            q.append(xp)
print(visited[Z])