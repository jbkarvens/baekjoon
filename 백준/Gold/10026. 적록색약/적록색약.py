import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
arr=[]
for i in range(N):
    line=list(input().strip())
    arr.append(line)

visited = [[False for _ in range(N)] for _ in range(N)]
my=set()
rgb=0
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        stack=deque()
        stack.append((i,j))
        my.add((i,j))
        while stack:
            u,v=stack.popleft()
            my.remove((u,v))
            visited[u][v]=True
            for du,dv in [(-1,0),(1,0),(0,-1),(0,1)]:
                nu=u+du
                nv=v+dv
                if not(0<=nu<N and 0<=nv<N):
                    continue
                if visited[nu][nv]==False and arr[nu][nv]==arr[u][v]:
                    if not (nu,nv) in my:
                        stack.append((nu,nv))
                        my.add((nu,nv))
        rgb+=1
rb=0
visited = [[False for _ in range(N)] for _ in range(N)]
my=set()
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        stack=deque()
        stack.append((i,j))
        my.add((i,j))
        while stack:
            u,v=stack.popleft()
            my.remove((u,v))
            visited[u][v]=True
            for du,dv in [(-1,0),(1,0),(0,-1),(0,1)]:
                nu=u+du
                nv=v+dv
                if not(0<=nu<N and 0<=nv<N):
                    continue
                if visited[nu][nv]==False:
                    if arr[nu][nv]==arr[u][v] or (arr[nu][nv]!='B' and arr[u][v]!='B'):
                        if not (nu,nv) in my:
                            stack.append((nu,nv))
                            my.add((nu,nv))
        rb+=1
print(rgb,rb)