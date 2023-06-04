import sys
from collections import deque
input=sys.stdin.readline
DIRECTION=[(-1,0),(1,0),(0,-1),(0,1)]

N,M=map(int,input().split())
lst=[[None for _ in range(M)] for _ in range(N)]
for i in range(N):
    sen=input().rstrip()
    for j in range(M):
        lst[i][j]=int(sen[j])

visited=[[False for _ in range(M)] for _ in range(N)]
q=deque()
q.append((0,0,1))
cout=0
while q:
    x,y,d=q.popleft()
    if x==N-1 and y==M-1:
        cout=d
    if visited[x][y]:
        continue
    visited[x][y]=True
    for dx,dy in DIRECTION:
        u,v=x+dx,y+dy
        if 0<=u<N and 0<=v<M and lst[u][v] and not visited[u][v]:
            q.append((u,v,d+1))
print(cout)