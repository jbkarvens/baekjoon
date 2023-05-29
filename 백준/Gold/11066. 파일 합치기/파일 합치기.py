import sys
input=sys.stdin.readline
for _ in range(int(input())):
    K=int(input())
    A=list(map(int,input().split()))
    S=[0 for _ in range(K+1)]
    for i in range(K):
        S[i+1]=S[i]+A[i]
    dp=[[None for _ in range(K)] for _ in range(K)]
    for i in range(K):
        dp[i][i]=0
    for j in range(K):
        for i in reversed(range(j)):
            dp[i][j]=min([dp[i][u]+dp[u+1][j] for u in range(i,j)])+S[j+1]-S[i]
    print(dp[0][K-1])