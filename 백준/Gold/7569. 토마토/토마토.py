import sys
from collections import deque
input=sys.stdin.readline

MOVES=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
M,N,H=map(int,input().split())
lst=[]
for z in range(H):
    lst.append([])
    for _ in range(N):
        lst[z].append(list(map(int,input().split())))

q=deque()
for k in range(H):
    for i in range(N):
        for j in range(M):
            if lst[k][i][j]==1:
                q.append((k,i,j))
ans=[[[None for _ in range(M)] for _ in range(N)] for _ in range(H)]
for k in range(H):
    for i in range(N):
        for j in range(M):
            if lst[k][i][j]!=0:
                ans[k][i][j]=0
            
while q:
    z,x,y=q.popleft()
    for dz,dx,dy in MOVES:
        w,u,v=z+dz,x+dx,y+dy
        if 0<=u<N and 0<=v<M and 0<=w<H and ans[w][u][v]==None:
            q.append((w,u,v))
            ans[w][u][v]=ans[z][x][y]+1
            
days=0
chk=False
for k in range(H):
    for i in range(N):
        for j in range(M):
            if ans[k][i][j]==None:
                chk=True
                days=-1
                break
        if chk:
            break
        days=max(days,max(ans[k][i]))
    if chk:
        break
print(days)