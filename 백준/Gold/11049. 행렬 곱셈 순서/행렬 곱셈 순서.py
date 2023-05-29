MAX_NUM=2**31
N=int(input())
A=[]
for _ in range(N):
    A.append(list(map(int,input().split())))
dp=[[None for _ in range(N)] for _ in range(N)]
for i in range(N):
    dp[i][i]=0
for j in range(N):
    for i in reversed(range(j)):
        m=MAX_NUM
        for k in range(i,j):
            m=min(m,dp[i][k]+dp[k+1][j]+A[i][0]*A[k][1]*A[j][1])
        dp[i][j]=m
print(dp[0][-1])