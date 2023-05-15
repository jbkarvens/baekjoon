from collections import deque
d=deque()
N,M=map(int,input().split())
lst=list(map(int,input().split()))
result=0
for i in range(1,N+1):
    d.append(i)
for i in range(M):
    idx=d.index(lst[i])
    if idx<len(d)-idx:
        result+=idx
        for _ in range(idx):
            d.append(d[0])
            d.popleft()
    else:
        result+=len(d)-idx
        for _ in range(len(d)-idx):
            d.appendleft(d[-1])
            d.pop()
    d.popleft()
print(result)