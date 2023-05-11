import sys
input=sys.stdin.readline
n=int(input())
stack=[]
stacklog=[]
i=1
poss=True
for _ in range(n):
    num=int(input())
    if not poss:
        continue
    if len(stack)==0 or stack[-1]!=num:
        if i>num:
            poss=False
        else:
            while i<=num:
                stack.append(i)
                stacklog.append('+')
                i+=1
            stack.pop()
            stacklog.append('-')
    else:
        stack.pop()
        stacklog.append('-')
if poss:
    for i in range(len(stacklog)):
        print(stacklog[i])
else:
    print('NO')