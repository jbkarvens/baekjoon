import sys
input=sys.stdin.readline

from collections import deque

N,M=map(int,input().split())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))
dist=[[None]*M for _ in range(N)]
que=deque()
for i in range(N):
    for j in range(M):
        if arr[i][j]==2:
            que.append((i,j))
            dist[i][j]=0
while que:
    x,y=que.popleft()
    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx=x+dx
            ny=y+dy
            if not(0<=nx<N and 0<=ny<M):
                continue
            if arr[nx][ny]==0:
                continue
            if dist[nx][ny]==None or dist[nx][ny]>dist[x][y]+1:
                dist[nx][ny]=dist[x][y]+1
                que.append(((nx,ny)))
for i in range(N):
    for j in range(M):
        if dist[i][j]==None:
            if arr[i][j]==0:
                dist[i][j]=0
            else:
                dist[i][j]=-1
for line in dist:
    print(*line)