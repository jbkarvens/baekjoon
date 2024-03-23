import sys
input=sys.stdin.readline

N = int(input())
M = 1000000+10
deq = [None for _ in range(M)]
front, end = 1, 0
cnt = 0
for _ in range(N):
    ss = list(map(int,input().split()))
    if ss[0] == 1:
        if front == 0:
            front = M-1
        else:
            front -= 1
        deq[front] = ss[1]
        cnt +=1
    elif ss[0] == 2:
        if end == M-1:
            end = 0
        else:
            end += 1
        deq[end] = ss[1]
        cnt +=1
    elif ss[0] == 3:
        if cnt > 0:
            print(deq[front])
            if front == M-1:
                front = 0
            else:
                front += 1
            cnt-=1
        else:
            print(-1)
    elif ss[0] == 4:
        if cnt > 0:
            print(deq[end])
            if end == 0:
                end = M-1
            else:
                end -= 1
            cnt-=1
        else:
            print(-1)
    elif ss[0] == 5:
        print(cnt)
    elif ss[0] == 6:
        if cnt>0:
            print(0)
        else:
            print(1)
    elif ss[0] == 7:
        if cnt>0:
            print(deq[front])
        else:
            print(-1)
    elif ss[0] == 8:
        if cnt>0:
            print(deq[end])
        else:
            print(-1)
    