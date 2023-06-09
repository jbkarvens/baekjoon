import sys
input=sys.stdin.readline

def LIS(A):
    N=len(A)
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
    return ans[::-1]

N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int,input().split())))
A.sort()
lis_set = set(LIS([b[1] for b in A]))
print(N - len(lis_set))
for a,b in A:
    if b not in lis_set:
        print(a)