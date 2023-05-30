MAX_MASS=40000+1
N=int(input())
A=list(map(int,input().split()))
M=int(input())
X=list(map(int,input().split()))

dp=[False for _ in range(MAX_MASS)]
dp[0],dp[A[0]]=True,True
for i in range(1,N):
    tmp=dp[:]
    for j in range(MAX_MASS):
        if j+A[i]<MAX_MASS and dp[j+A[i]]:
            tmp[j]=True
        elif abs(j-A[i])<MAX_MASS and dp[abs(j-A[i])]:
            tmp[j]=True
    dp=[dp[i] or tmp[i] for i in range(MAX_MASS)]
            
ans=['Y' if dp[X[i]] else 'N' for i in range(M)]
print(*ans)