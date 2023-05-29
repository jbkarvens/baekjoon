s1=input().rstrip()
s2=input().rstrip()
n1,n2=len(s1),len(s2)
dp=[[None for _ in range(n2+1)] for _ in range(n1+1)]
for i in range(n1+1):
    dp[i][0]=0
for i in range(n2+1):
    dp[0][i]=0
for i in range(1,n1+1):
    for j in range(1,n2+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[n1][n2])