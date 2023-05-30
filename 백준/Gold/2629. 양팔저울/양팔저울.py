MAX_MASS=40000+1
N=int(input())
A=list(map(int,input().split()))
M=int(input())
X=list(map(int,input().split()))

dp=[[False for _ in range(MAX_MASS)] for _ in range(N)]
dp[0][0],dp[0][A[0]]=True,True
for i in range(1,N):
    for j in range(MAX_MASS):
        if j+A[i]<MAX_MASS and dp[i-1][j+A[i]]:
            dp[i][j]=True
        elif abs(j-A[i])<MAX_MASS and dp[i-1][abs(j-A[i])]:
            dp[i][j]=True
        elif dp[i-1][j]:
            dp[i][j]=True
            
ans=['Y' if dp[-1][X[i]] else 'N' for i in range(M)]
print(*ans)