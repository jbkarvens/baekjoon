NUM=10**6+1
N=int(input())
A=list(map(int,input().split()))
F=[0 for _ in range(NUM)]
for i in range(N):
    F[A[i]]+=1
stack=[0]
ans=[-1 for _ in range(N)]
for i in range(1,N):
    while len(stack)>0:
        idx=stack[-1]
        if F[A[idx]]<F[A[i]]:
            ans[idx]=A[i]
            stack.pop()
        else:
            break
    stack.append(i)
print(*ans)