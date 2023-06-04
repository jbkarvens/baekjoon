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
q_set=set()
for k in range(H):
    for i in range(N):
        for j in range(M):
            if lst[k][i][j]==1:
                q.append((k,i,j,0))
                q_set.add((k,i,j))
ans=[[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]
for k in range(H):
    for i in range(N):
        for j in range(M):
            if lst[k][i][j]==-1:
                ans[k][i][j]=0
            
while q:
    z,x,y,d=q.popleft()
    q_set.remove((z,x,y))
    ans[z][x][y]=d
    for dz,dx,dy in MOVES:
        w,u,v=z+dz,x+dx,y+dy
        if 0<=u<N and 0<=v<M and 0<=w<H and not ((w,u,v) in q_set) and lst[w][u][v]!=-1 and ans[w][u][v]==-1:
            q.append((w,u,v,d+1))
            q_set.add((w,u,v))

days=0
chk=False
for k in range(H):
    for i in range(N):
        for j in range(M):
            if ans[k][i][j]==-1:
                chk=True
                days=-1
                break
            days=max(days,ans[k][i][j])
        if chk:
            break
    if chk:
        break
print(days)