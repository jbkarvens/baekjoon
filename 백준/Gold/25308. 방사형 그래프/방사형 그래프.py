import sys
import math
import itertools
input = sys.stdin.readline

def ccw(a,b,c):
    x1 = c[0] - b[0]
    y1 = c[1] - b[1]
    x2 = a[0] - b[0]
    y2 = a[1] - b[1]
    z = x1 * y2 - x2 * y1
    if z == 0:
        return 0
    elif z > 0:
        return 1
    else:
        return -1

A = list(map(int,input().split()))
N = len(A)
perm = itertools.permutations(A, N)
x = [None for _ in range(N+2)]
y = [None for _ in range(N+2)]
ans = 0
for lst in perm:
    for i in range(N):
        x[i] = lst[i] * math.cos(2 * math.pi * i / N)
        y[i] = lst[i] * math.sin(2 * math.pi * i / N)
    x[N], y[N] = x[0], y[0]
    x[N+1], y[N+1] = x[1], y[1]
    chk = True
    for i in range(N):
        if ccw((x[i], y[i]), (x[i + 1], y[i + 1]), (x[i + 2], y[i + 2])) < 0:
            chk = False
            break
    if chk:
        ans += 1
print(ans)