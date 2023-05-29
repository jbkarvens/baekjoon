N=int(input())
lst=[]
for _ in range(N):
    lst.append(list(map(int,input().split())))
lst=sorted(lst,key=lambda x:x[0])
A=[]
for i in range(N):
    A.append(lst[i][1])
ans=[]
for i in range(N):
    tmp=[ans[j] for j in range(i) if A[j]<A[i]]
    if len(tmp)==0:
        ans.append(1)
    else:
        ans.append(max(tmp)+1)
print(N-max(ans))