N=int(input())
A=list(map(int,input().split()))
stack=[(A[0],0)]
ans=[-1 for _ in range(N)]
for i in range(1,N):
    while len(stack)>0:
        val,idx=stack[-1]
        if val<A[i]:
            ans[idx]=A[i]
            stack.pop()
        else:
            break
    stack.append((A[i],i))
print(*ans)