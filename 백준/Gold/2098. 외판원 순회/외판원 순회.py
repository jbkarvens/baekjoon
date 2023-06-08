import sys
input = sys.stdin.readline

N = int(input())
W = []
for _ in range(N):
    W.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        if W[i][j] == 0:
            W[i][j] = 10**10

# dp[i][S] : N-1에서 출발해 i까지 도달. 방문한 점들 집합이 S일때 최소비용. 시작지점 N-1과 끝지점 i는 S에 포함X
# dp[i][S] = min W[u][i]+dp[u][S-{u}] for u in S
dp = [[None for _ in range(1 << (N-1))] for _ in range(N)]

for i in range(N):
    dp[i][0] = W[N - 1][i]

def get_dp(i, S):
    if dp[i][S] != None:
        return dp[i][S]
    res = 10**10
    for j in range(N):
        if (S & (1 << j)) != 0:
            tmp = W[j][i] + get_dp(j, S & (~(1 << j)))
            res = min(tmp, res)
    dp[i][S] = res
    return res

print(get_dp(N - 1, (1 << (N - 1)) - 1))