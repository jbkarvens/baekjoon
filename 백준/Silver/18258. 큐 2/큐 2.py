import sys
input=sys.stdin.readline
N=int(input())
queue=[]
start=0
for _ in range(N):
    order=input().split()
    word=order[0]
    if word=='push':
        queue.append(order[1])
    elif word=='pop':
        if len(queue)!=start:
            print(queue[start])
            start+=1
        else:
            print(-1)
            queue=[]
            start=0
    elif word=='size':
        length=len(queue)-start
        print(length)
        if length==0:
            queue=[]
            start=0
    elif word=='empty':
        if len(queue)==start:
            print(1)
            queue=[]
            start=0
        else:
            print(0)
    elif word=='front':
        if len(queue)!=start:
            print(queue[start])
        else:
            print(-1)
            queue=[]
            start=0
    elif word=='back':
        if len(queue)!=start:
            print(queue[-1])
        else:
            print(-1)
            queue=[]
            start=0