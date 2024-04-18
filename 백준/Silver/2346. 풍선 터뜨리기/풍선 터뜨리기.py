import sys
from collections import deque
input=sys.stdin.readline
N = int(input())
A = map(int,input().split())
deq = deque()
for i,a in enumerate(A):
    deq.append((i+1,a))
res = []
for i in range(N):
    idx,rot = deq.popleft()
    res.append(idx)
    if rot>0:
        deq.rotate(-(rot-1))
    elif rot<0:
        deq.rotate(-rot)
print(*res)
