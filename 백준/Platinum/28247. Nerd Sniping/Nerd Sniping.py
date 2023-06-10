import sys
input_func = sys.stdin.readline

A,B=[],[]
T=int(input_func())
for _ in range(T):
    a, b = map(int, input_func().split())
    a, b = abs(a), abs(b)
    if a > b:
        a, b = b, a
    A.append(a)
    B.append(b)

X_MAX = max(B)
NUM = 998244353

R = [[[0 for _ in range(X_MAX + 1)] for _ in range(X_MAX + 1)] for _ in range(2)]
for i in range(1, X_MAX + 1):
    R[1][i][i] = (R[1][i-1][i-1] + pow(2*i - 1, -1, NUM))%NUM

R[0][0][1] = pow(2, -1, NUM)
for i in range(2, X_MAX + 1):
    R[0][0][i] = (4 * R[0][0][i-1] - R[0][0][i-2] - 2 * R[0][1][i-1])%NUM
    R[1][0][i] = (4 * R[1][0][i-1] - R[1][0][i-2] - 2 * R[1][1][i-1])%NUM
    for j in range(1, i-1):
        R[0][j][i] = (4 * R[0][j][i-1] - R[0][j][i-2] - R[0][j+1][i-1] - R[0][j-1][i-1])%NUM
        R[1][j][i] = (4 * R[1][j][i-1] - R[1][j][i-2] - R[1][j+1][i-1] - R[1][j-1][i-1])%NUM
    R[0][i-1][i] = (2 * R[0][i-1][i-1] - R[0][i-2][i-1])%NUM
    R[1][i-1][i] = (2 * R[1][i-1][i-1] - R[1][i-2][i-1])%NUM

for a,b in zip(A,B):
    print(R[0][a][b], R[1][a][b])