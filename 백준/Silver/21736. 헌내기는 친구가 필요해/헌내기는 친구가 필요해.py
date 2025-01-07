import sys
input=sys.stdin.readline
from collections import deque
N,M=map(int,input().split())
arr=[]
for _ in range(N):
    arr.append(list(input().strip()))
sx,sy=None,None
cnt=0
for i in range(N):
    for j in range(M):
        if arr[i][j]=='I':
            sx,sy=i,j
            break

que=deque()
que.append((sx,sy))
visited=[[False for _ in range(M)] for _ in range(N)]
while que:
    x,y=que.popleft()
    visited[x][y]=True
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        nx=x+dx
        ny=y+dy
        if not(0<=nx<N and 0<=ny<M):
            continue
        if arr[nx][ny]=='X':
            continue
        if visited[nx][ny]:
            continue
        if arr[nx][ny]=='P':
            cnt+=1
        que.append((nx,ny))
        visited[nx][ny]=True
if cnt==0:
    print('TT')
else:
    print(cnt)