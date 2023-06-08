import sys
from collections import deque
from random import randint
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N,M=map(int,input().split())
board=[]
for _ in range(N):
    board.append(list(map(int,input().split())))

land_no=[[None for _ in range(M)] for _ in range(N)]

# 땅 구분
cout=0
for i in range(N):
    for j in range(M):
        if land_no[i][j]!=None or board[i][j]==0:
            continue
        q=deque()
        q.append((i,j))
        while q:
            x,y=q.popleft()
            land_no[x][y]=cout
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                u,v=x+dx,y+dy
                if not (0<=u<N and 0<=v<M) or not land_no[u][v]==None or board[u][v]==0:
                    continue
                q.append((u,v))
        cout+=1
land_num=cout

# 가능한 다리 찾기
# 가로
E=[]
for i in range(N):
    start_land_no=None
    cout=0
    for j in range(M):
        if board[i][j]:
            if start_land_no==None:
                start_land_no=land_no[i][j]
                cout=0
            else:
                end_land_no=land_no[i][j]
                if cout>=2 and end_land_no!=start_land_no:
                    E.append([cout,start_land_no,end_land_no])
                cout=0
                start_land_no=end_land_no
        else:
            cout+=1
# 세로
for j in range(M):
    start_land_no=None
    cout=0
    for i in range(N):
        if board[i][j]:
            if start_land_no==None:
                start_land_no=land_no[i][j]
                cout=0
            else:
                end_land_no=land_no[i][j]
                if cout>=2 and end_land_no!=start_land_no:
                    E.append([cout,start_land_no,end_land_no])
                cout=0
                start_land_no=end_land_no
        else:
            cout+=1
E.sort()

# MST
ans=0
root=list(range(land_num))
rank=[1 for _ in range(land_num)]

def find(x):
    if root[x]==x:
        return x
    root[x]=find(root[x])
    return root[x]

def union(x,y):
    rt_x=find(x)
    rt_y=find(y)
    if rt_x==rt_y:
        return
    if randint(0,1):
        rt_x,rt_y=rt_y,rt_x
    root[rt_x]=rt_y
    rank[rt_y]+=rank[rt_x]

chk=False
idx=0
while idx<len(E):
    if rank[find(0)]==land_num:
        chk=True
        break
    c,x,y=E[idx]
    rt_x=find(x)
    rt_y=find(y)
    if rt_x==rt_y:
        idx+=1
        continue
    union(x,y)
    ans+=c

if chk:
    print(ans)
else:
    print(-1)

