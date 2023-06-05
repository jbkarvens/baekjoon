import sys
input=sys.stdin.readline
       
INF=10**8 
N=int(input())
M=int(input())
d=[[INF for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    d[i][i]=0
for _ in range(M):
    a,b,c=map(int,input().split())
    d[a][b]=min(d[a][b],c)
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            d[i][j]=min(d[i][j],d[i][k]+d[k][j])
for i in range(1,N+1):
    for j in range(1,N+1):
        if d[i][j]==INF:
            d[i][j]=0
for i in range(1,N+1):
    print(*d[i][1:])