N=int(input())
A=list(map(int,input().split()))
M=[A[0]]
idx_lst=[0 for _ in range(N)]
for i in range(N):
    if M[-1]<A[i]:
        M.append(A[i])
        idx_lst[i]=len(M)-1
    else:
        low,high=0,len(M)-1
        while low<=high:
            mid=(low+high)//2
            if M[mid]<A[i]:
                low=mid+1
            else:
                high=mid-1
        M[high+1]=A[i]
        idx_lst[i]=high+1
print(len(M))
ans=[]
cur=len(M)-1
for i in reversed(range(N)):
    if cur==idx_lst[i]:
        ans.append(A[i])
        cur-=1
print(*ans[::-1])