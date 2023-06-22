import sys
input=sys.stdin.readline
from collections import deque

if __name__=='__main__':
    N = int(input())
    parent=[None for _ in range(N+1)]
    parent[1]=1
    adj=[[] for _ in range(N+1)]
    for _ in range(N-1):
        a,b=map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    q = deque()
    q.append(1)
    while q:
        node = q.popleft()
        for vertex in adj[node]:
            if parent[node]==vertex:
                continue
            parent[vertex]=node
            q.append(vertex)
    sparse_table = [[parent[i]] for i in range(N+1)]
    depth = 17
    for i in range(depth):
        for j in range(1,N+1):
            sparse_table[j].append(sparse_table[sparse_table[j][i]][i])
    M = int(input())
    for _ in range(M):
        x,y=map(int,input().split())
        depth_x,depth_y=0,0
        xc,yc=x,y
        for i in reversed(range(depth)):
            if sparse_table[xc][i]!=1:
                xc = sparse_table[xc][i]
                depth_x+=(1<<i)
            if sparse_table[yc][i]!=1:
                yc = sparse_table[yc][i]
                depth_y+=(1<<i)
        depth_x+=1
        depth_y+=1
        if depth_x<depth_y:
            x,y=y,x
            depth_x,depth_y=depth_y,depth_x
        diff = depth_x-depth_y
        i = depth
        while diff>0:
            if diff>=(1<<i):
                x=sparse_table[x][i]
                diff-=(1<<i)
            i-=1
        for i in reversed(range(depth)):
            if sparse_table[x][i]!=sparse_table[y][i]:
                x=sparse_table[x][i]
                y=sparse_table[y][i]
        if x!=y:
            x=sparse_table[x][0]
        sys.stdout.write(f'{x}\n')