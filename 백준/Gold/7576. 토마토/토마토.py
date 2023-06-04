import sys
from collections import deque
input=sys.stdin.readline

MOVES=[(1,0),(-1,0),(0,1),(0,-1)]
M,N=map(int,input().split())
lst=[]
for _ in range(N):
    lst.append(list(map(int,input().split())))

q=deque()
q_set=set()
for i in range(N):
    for j in range(M):
        if lst[i][j]==1:
            q.append((i,j,0))
            q_set.add((i,j))
ans=[[-1 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if lst[i][j]==-1:
            ans[i][j]=0
            
while q:
    x,y,d=q.popleft()
    q_set.remove((x,y))
    ans[x][y]=d
    for dx,dy in MOVES:
        u,v=x+dx,y+dy
        if 0<=u<N and 0<=v<M and not ((u,v) in q_set) and lst[u][v]!=-1 and ans[u][v]==-1:
            q.append((u,v,d+1))
            q_set.add((u,v))

days=0
for i in range(N):
    chk=False
    for j in range(M):
        if ans[i][j]==-1:
            chk=True
            days=-1
            break
        days=max(days,ans[i][j])
    if chk:
        break
print(days)