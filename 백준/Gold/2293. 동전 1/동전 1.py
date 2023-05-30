n,k=map(int,input().split())
A=[int(input()) for _ in range(n)]
dp=[0 for _ in range(k+1)]
dp[0]=1
for i in range(n):
    for j in range(A[i],k+1):
        dp[j]+=dp[j-A[i]]
print(dp[k])