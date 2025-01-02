import sys
input=sys.stdin.readline

N=int(input())
dd=[]
for i in range(N):
    dd.append(list(map(int,input().split())))
d=[[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        d[i][j]=dd[i][j]
for _ in range(N):
    for i in range(N):
        for j in range(N):
            if d[i][j]:
                continue
            for k in range(N):
                if d[i][k] and d[k][j]:
                    d[i][j]=1
for i in range(N):
    print(*d[i])