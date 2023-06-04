import sys
from collections import deque
input=sys.stdin.readline

MOVES=[(2,-1),(2,1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
for _ in range(int(input())):
    I=int(input())
    X,Y=map(int,input().split())
    X2,Y2=map(int,input().split())
    q=deque()
    visited=set()
    q.append((X,Y,0))
    while q:
        x,y,d=q.popleft()
        if x==X2 and y==Y2:
            ans=d
            break
        if (x,y) in visited:
            continue
        visited.add((x,y))
        for dx,dy in MOVES:
            u,v=x+dx,y+dy
            if 0<=u<I and 0<=v<I and not ((u,v) in visited):
                q.append((u,v,d+1))
    print(ans)