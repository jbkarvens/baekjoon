N=int(input())
A=list(map(int,input().split()))
M=[A[0]]
for i in range(N):
    if M[-1]<A[i]:
        M.append(A[i])
    else:
        low,high=0,len(M)-1
        while low<=high:
            mid=(low+high)//2
            if M[mid]<A[i]:
                low=mid+1
            else:
                high=mid-1
        M[high+1]=A[i]
print(len(M))