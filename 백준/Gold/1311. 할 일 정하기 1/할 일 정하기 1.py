import sys
input = sys.stdin.readline

N = int(input())
D=[]
for _ in range(N):
    D.append(list(map(int,input().split())))

# dp[k-1][S] : 집합 S의 일을 k번째 사람까지만 고려했을 때 최소비용
# dp[k][S] = min(D[k-1][u] + dp[k-1][S-{u}] for u in S)
# 필요한 경우는 len(S) = k인 경우 뿐
dp = [None for _ in range(1 << N)]
dp[0] = 0

def get_dp(k, S):
    if dp[S] != None:
        return dp[S]
    ret = 10**10
    for i in range(N):
        if (S & (1 << i)) == (1 << i):
            ret = min(ret, D[k - 1][i] + get_dp(k - 1, S & (~(1 << i))))
    dp[S] = ret
    return ret

print(get_dp(N, (1 << N) - 1))