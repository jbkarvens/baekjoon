import sys
input=sys.stdin.readline

while True:
    N=int(input())
    if N==0:
        break
    P=list(map(int,input().split()))
    X,Y=map(int,input().split())

    res=set()
    test=set([1])
    test_next=set()
    while test:
        for t in test:
            if X<=t and t<=Y:
                res.add(t)
            for pp in P:
                num=t*pp
                if num<=Y:
                    test_next.add(num)
        test=test_next.copy()
        test_next=set()
    res=list(res)
    res.sort()
    if res:
        print(*res,sep=',')
    else:
        print('none')