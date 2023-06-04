import sys
from collections import deque
MAX=2*10**5
input=sys.stdin.readline

N,K=map(int,input().split())
visited=set()
q=deque()
q.append((N,0))
ans=0
while q:
    x,d=q.popleft()
    if x>MAX:
        continue
    if x==K:
        ans=d
        break
    if x in visited:
        continue
    visited.add(x)
    for y in [x-1,x+1,2*x]:
        if not(y in visited):
            q.append((y,d+1))
print(ans)