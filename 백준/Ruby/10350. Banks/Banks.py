import sys
import math
input=sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

A_sum = [0]
for i in range(N):
    A_sum.append(A_sum[-1]+A[i])

A_tot = A_sum[-1]

ans = 0
for i in range(N + 1):
    for j in range(i + 1, N + 1):
        if A_sum[i] > A_sum[j]:
            ans += math.ceil((A_sum[i] - A_sum[j]) / A_tot)
for i in range(1, N):
    for j in range(i + 1, N):
        if A_sum[-1] < A_sum[j] - A_sum[i]:
            ans += math.ceil((A_sum[j] - A_sum[i] - A_sum[-1]) / A_tot)
print(ans)