import sys
input=sys.stdin.readline
s1=input().strip()
s2=input().strip()
s3=input().strip()
M1=len(s1)
M2=len(s2)
M3=len(s3)
dp=[[[0 for _ in range(M3+1)] for _ in range(M2+1)] for _ in range(M1+1)]
for i in range(1,M1+1):
    for j in range(1,M2+1):
        for k in range(1,M3+1):
            if s1[i-1]==s2[j-1]==s3[k-1]:
                dp[i][j][k]=dp[i-1][j-1][k-1]+1
            else:
                dp[i][j][k]=max(dp[i][j][k-1],dp[i][j-1][k],dp[i-1][j][k])
print(dp[M1][M2][M3])