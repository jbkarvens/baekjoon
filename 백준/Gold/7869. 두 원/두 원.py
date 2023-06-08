import sys
import math
input = sys.stdin.readline

x1, y1, r1, x2, y2, r2 = map(float, input().split())
d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 )
if r1 < r2:
    (x1, y1, r1), (x2, y2, r2) = (x2, y2, r2), (x1, y1, r1)
if r1 == 0 or r2 ==0:
    ans = 0
elif r1 + r2 <= d:
    ans = 0
elif r2 + d <= r1:
    ans = math.pi * r2 * r2
else:
    theta1 = math.acos((r1**2 + d**2 - r2**2)/(2 * r1 * d))
    theta2 = math.acos((r2**2 + d**2 - r1**2)/(2 * r2 * d))
    area1 = r1 * r1 * theta1 - r1 * r1 * math.sin(2 * theta1) / 2
    area2 = r2 * r2 * theta2 - r2 * r2 * math.sin(2 * theta2) / 2
    ans = area1 + area2
print(f'{ans:.3f}')