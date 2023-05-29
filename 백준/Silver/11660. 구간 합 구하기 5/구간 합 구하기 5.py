import sys
input=sys.stdin.readline
N,M=map(int,input().split())
A=[None for _ in range(N)]
for i in range(N):
    A[i]=list(map(int,input().split()))
S=[[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        S[i][j]=S[i][j-1]+A[i-1][j-1]
for i in range(1,N+1):
    for j in range(1,N+1):
        S[i][j]+=S[i-1][j]
for _ in range(M):
    x1,y1,x2,y2=map(int,input().split())
    print(S[x2][y2]-S[x1-1][y2]-S[x2][y1-1]+S[x1-1][y1-1])