import sys
input = sys.stdin.readline

X, Y, D, T = map(float,input().split())

dist = (X**2 + Y**2)**0.5
ans = 0
k = int(dist / D)
if k >= 1:
    ans = min((k + 1) * T, dist - k * D + k * T, dist)
else:
    ans = min(dist, abs(D - dist) + T, 2 * T)
print(ans)