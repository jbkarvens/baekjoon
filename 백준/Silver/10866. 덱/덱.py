import sys
from collections import deque
input=sys.stdin.readline
d=deque()
for _ in range(int(input())):
    order=input().split()
    if order[0]=='push_front':
        d.appendleft(int(order[1]))
    elif order[0]=='push_back':
        d.append(int(order[1]))
    elif order[0]=='pop_front' and len(d)!=0:
        print(d.popleft())
    elif order[0]=='pop_back' and len(d)!=0:
        print(d.pop())
    elif order[0]=='size':
        print(len(d))
    elif order[0]=='empty':
        if len(d)==0:
            print(1)
        else:
            print(0)
    elif order[0]=='front' and len(d)!=0:
        print(d[0])
    elif order[0]=='back' and len(d)!=0:
        print(d[-1])
    else:
        print(-1)