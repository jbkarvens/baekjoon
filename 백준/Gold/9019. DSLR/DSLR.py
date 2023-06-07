import sys
from collections import deque
input=sys.stdin.readline

for _ in range(int(input())):
    A,B=map(int,input().split())
    q=deque()
    q.append((A,''))
    visit=set()
    visit.add(A)
    while q:
        x,ans=q.popleft()
        if x==B:
            break
        y=(2*x)%10000
        if not y in visit:
            visit.add(y)
            q.append((y,ans+'D'))
        if x==0:
            y=9999
        else:
            y=x-1
        if not y in visit:
            visit.add(y)
            q.append((y,ans+'S'))
        y=10*(x%1000)+x//1000
        if not y in visit:
            visit.add(y)
            q.append((y,ans+'L'))
        y=(x%10)*1000+x//10
        if not y in visit:
            visit.add(y)
            q.append((y,ans+'R'))
    print(ans)