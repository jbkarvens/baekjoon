import sys
input=sys.stdin.readline

N = int(input())
W = []
for _ in range(N):
    W.append(list(map(int,input().split())))

INF = 10**9
# dp[i][c][d] : i번째 집 c색, 1번집 d색으로 칠했을 때 i번째까지 최소비용
# dp[i][c][d] = W[i][c] + min dp[i-1][c'][d] for c'!=c
dp = [[[INF for _ in range(3)] for _ in range(3)]for _ in range(N)]

for c in range(3):
    dp[0][c][c] = W[0][c]

for i in range(1, N):
    for c in range(3):
        for d in range(3):
            res = INF
            for cp in range(3):
                if cp == c:
                    continue
                res = min(res, dp[i - 1][cp][d])
            dp[i][c][d] = W[i][c] + res
ans = INF
for c in range(3):
    for d in range(3):
        if c == d:
            continue
        ans = min(ans, dp[-1][c][d])
print(ans)