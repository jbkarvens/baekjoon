import sys
input_func = sys.stdin.readline

X_MAX = 2000
NUM = 998244353

R = [[[0,0] for _ in range(X_MAX + 1)] for i in range(X_MAX + 1)]
for i in range(1, X_MAX + 1):
    R[i][i][1] = (R[i-1][i-1][1] + pow(2*i - 1, -1, NUM))%NUM

R[0][1][0] = pow(2, -1, NUM)
for i in range(2, X_MAX + 1):
    R[0][i][0] = (4 * R[0][i-1][0] - R[0][i-2][0] - 2 * R[1][i-1][0])%NUM
    R[0][i][1] = (4 * R[0][i-1][1] - R[0][i-2][1] - 2 * R[1][i-1][1])%NUM
    for j in range(1, i-1):
        R[j][i][0] = (4 * R[j][i-1][0] - R[j][i-2][0] - R[j+1][i-1][0] - R[j-1][i-1][0])%NUM
        R[j][i][1] = (4 * R[j][i-1][1] - R[j][i-2][1] - R[j+1][i-1][1] - R[j-1][i-1][1])%NUM
    R[i-1][i][0] = (2 * R[i-1][i-1][0] - R[i-2][i-1][0])%NUM
    R[i-1][i][1] = (2 * R[i-1][i-1][1] - R[i-2][i-1][1])%NUM

for _ in range(int(input_func())):
    a, b = map(int, input_func().split())
    a, b = abs(a), abs(b)
    if a > b:
        a, b = b, a
    print(R[a][b][0], R[a][b][1])