N,K=map(int,input().split())
stack=list(range(1,N+1))
start,end=0,N-1
i=0
print("<",end='')
while start<=end:
    i+=1
    if i%K==0:
        if i>K:
            print(", ",end='')
        print(stack[start],end='')
        start+=1
    else:
        stack.append(stack[start])
        end+=1
        start+=1
print(">")