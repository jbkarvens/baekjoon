import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
q=deque()
q.append((N,[N]))
while q:
    x,lst=q.popleft()
    if x==1:
        ans=lst
        break
    if x%3==0:
        q.append((x//3,lst+[x//3]))
    if x%2==0:
        q.append((x//2,lst+[x//2]))
    q.append((x-1,lst+[x-1]))
print(len(ans)-1)
print(*ans)