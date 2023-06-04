import sys
from collections import deque
input=sys.stdin.readline

MOVES=[(1,0),(-1,0),(0,1),(0,-1)]
N,M=map(int,input().split())
lst=[]
for _ in range(N):
    lst.append([])
    sen=input().rstrip()
    for i in range(M):
        lst[-1].append(int(sen[i]))
q=deque()
dist=[[[None,None] for _ in range(M)] for _ in range(N)]
q.append((0,0,0))
dist[0][0][0]=1
while q:
    x,y,z=q.popleft()
    if x==N-1 and y==M-1:
        break
    for dx,dy in MOVES:
        u,v=x+dx,y+dy
        if not(0<=u<N and 0<=v<M):
            continue
        if lst[u][v]==1 and z==0:
            dist[u][v][1]=dist[x][y][0]+1
            q.append((u,v,1))
        elif lst[u][v]==0 and dist[u][v][z]==None:
            dist[u][v][z]=dist[x][y][z]+1
            q.append((u,v,z))

# for i in range(N):
#     for j in range(M):
#         print(dist[i][j][0],end=' ')
#     print()

ans=dist[-1][-1]
tmp=10**7
for i in range(2):
    if ans[i]!=None:
        tmp=min(tmp,ans[i])
if tmp==10**7:
    print(-1)
else:
    print(tmp)