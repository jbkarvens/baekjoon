import sys
input=sys.stdin.readline

N = int(input())
K = int(input())
NUM = 10**9 + 3

# 한 블록이 두칸이라 생각
# dp[n][k] : 문제가 일직선일 때
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
for n in range(N+1):
    dp[n][0] = 1
for n in range(2, N+1):
    for k in range(1, K+1):
        dp[n][k] = (dp[n - 1][k] + dp[n - 2][k - 1])%NUM
if K>1:
    print((dp[N][K] + dp[N - 2][K - 1])%NUM)
else:
    print(N)