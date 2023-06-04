import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
DIRECTION=[(-1,0),(1,0),(0,-1),(0,1)]

def dfs(x,y,M,N):
    if label[x][y]!=None:
        return
    label[x][y]=cout[0]
    for dx,dy in DIRECTION:
        u,v=x+dx,y+dy
        if 0<=u<M and 0<=v<N and (u,v) in V and label[u][v]==None:
            dfs(u,v,M,N)
            
for _ in range(int(input())):
    M,N,K=map(int,input().split())
    V=set()
    for _ in range(K):
        x,y=map(int,input().split())
        V.add((x,y))
    label=[[None for _ in range(N)] for _ in range(M)]
    cout=[0]
    for x in range(M):
        for y in range(N):
            if (x,y) in V and label[x][y]==None:
                dfs(x,y,M,N)
                cout[0]+=1
    print(cout[0])