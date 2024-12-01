import sys
input=sys.stdin.readline

N,M=map(int,input().split())
A=[None for _ in range(N)]
for i in range(N):
    A[i] = list(map(int,input().split()))
tetro=[[[0,1,2,3],[0,0,0,0]],
       [[0,0,0,0],[0,1,2,3]],
       
       [[0,1,0,1],[0,0,1,1]],
       
       [[0,1,0,0],[0,0,1,2]],
       [[0,0,1,2],[0,1,1,1]],
       [[1,1,0,1],[0,1,2,2]],
       [[0,1,2,2],[0,0,0,1]],
       [[0,1,1,1],[0,0,1,2]],
       [[0,1,2,0],[0,0,0,1]],
       [[0,0,0,1],[0,1,2,2]],
       [[0,1,2,2],[1,1,1,0]],
       
       [[1,0,1,0],[0,1,1,2]],
       [[0,1,1,2],[0,0,1,1]],
       [[0,0,1,1],[0,1,1,2]],
       [[1,2,0,1],[0,0,1,1]],
       
       [[1,0,1,2],[0,1,1,1]],
       [[0,0,1,0],[0,1,1,2]],
       [[1,0,1,1],[0,1,1,2]],
       [[0,1,2,1],[0,0,0,1]]]
score = 0
for mino in tetro:
    x,y=mino[0],mino[1]
    for i in range(N):
        for j in range(M):
            fit = True
            for k in range(4):
                if i+x[k]>=N or j+y[k]>=M:
                    fit = False
            if not fit:
                continue
            temp = 0
            for k in range(4):
                temp += A[i+x[k]][j+y[k]]
            score = max(score,temp)
print(score)