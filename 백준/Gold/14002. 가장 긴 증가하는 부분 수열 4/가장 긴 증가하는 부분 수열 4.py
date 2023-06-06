import sys
input=sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))

mem=[A[0]]
idx_lst=[0 for _ in range(N)]
for i in range(1,N):
    if mem[-1]<A[i]:
        mem.append(A[i])
        idx_lst[i]=len(mem)-1
    else:
        start,end=0,len(mem)-1
        while start<=end:
            mid=(start+end)//2
            if mem[mid]<A[i]:
                start=mid+1
            else:
                end=mid-1
        mem[end+1]=A[i]
        idx_lst[i]=end+1
cur=len(mem)-1
ans=[]
for i in reversed(range(N)):
    if cur==idx_lst[i]:
        ans.append(A[i])
        cur-=1
print(len(ans))
print(*ans[::-1])