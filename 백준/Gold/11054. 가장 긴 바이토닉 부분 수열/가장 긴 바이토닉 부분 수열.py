N=int(input())
A=list(map(int,input().split()))
left=[None for _ in range(N)]
left[0]=1
for i in range(1,N):
    tmp=[left[j] for j in range(i) if A[j]<A[i]]
    if len(tmp)==0:
        left[i]=1
    else:
        left[i] = 1 + max(tmp)
right=[None for _ in range(N)]
right[-1]=1
for i in reversed(range(N-1)):
    tmp=[right[j] for j in range(i+1,N) if A[i]>A[j]]
    if len(tmp)==0:
        right[i]=1
    else:
        right[i] = 1 + max(tmp)
tot=[]
for i in range(N):
    tot.append(left[i]+right[i]-1)
print(max(tot))