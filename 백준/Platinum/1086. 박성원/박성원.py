import sys
input=sys.stdin.readline

N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
K = int(input())

# dp[i][S] : S집합을 써서 나머지가 i인 것 갯수
# dp[i][S] = sum dp[i-u*10^t][S-{u}] for u in S
# S가 점점 작아짐을 이용

dp = [[0 for _ in range(1 << N)] for _ in range(K)]

dp[0][0] = 1

remlst = [[(A[u] + pow(10, len(str(A[u])), K) * i)%K for u in range(N)] for i in range(K)]

for S in range(1 << N):
    for i in range(K):
        for u in range(N):
            if S & (1 << u) == 0:
                dp[remlst[i][u]][S | (1 << u)] += dp[i][S]

u = 1
for i in range(1, N + 1):
    u *= i
v = dp[0][(1 << N) - 1]
u1, v1 = u, v
while v1 > 0:
    u1, v1 = v1, u1%v1
print(f'{v // u1}/{u // u1}')