from collections import deque
for _ in range(int(input())):
    p=input().rstrip()
    n=int(input())
    lst=list(input().rstrip()[1:-1].split(','))
    if lst[0]=='':
        lst=[]
    d=deque()
    rvs=False
    noError=True
    for i in lst:
        d.append(i)
    for i in range(len(p)):
        if p[i]=='R':
            rvs=not rvs
        elif p[i]=='D':
            try:
                if rvs:
                    d.pop()
                else:
                    d.popleft()
            except IndexError:
                noError=False
                break
    if noError:
        print('[',end='')
        if rvs:            
            for i,v in enumerate(reversed(d)):
                if i>0:
                    print(',',end='')
                print(v,end='')
        else:
            for i,v in enumerate(d):
                if i>0:
                    print(',',end='')
                print(v,end='')
        print(']')
    else:
        print('error')