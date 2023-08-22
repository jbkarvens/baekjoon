import sys
input=sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))
stack_=[]
turn=1
for i in range(n):
    now=A[i]
    while stack_:
        if turn==stack_[-1]:
            stack_.pop()
            turn+=1
        else:
            break
    if now!=turn:
        stack_.append(now)
    else:
        turn+=1
while stack_:
    if turn==stack_[-1]:
        stack_.pop()
        turn+=1
    else:
        break
if stack_:
    print("Sad")
else:
    print("Nice")