N=int(input())
A=list(map(int,input().split()))
# val[i] : A[i]로 끝나는 가장 긴 증가하는 부분 수열 길이
val=[1]
for i in range(1,N):
    lst=[val[j] for j in range(i) if A[j]<A[i]]
    if len(lst)==0:
        lst.append(0)
    val.append(max(lst)+1)
print(max(val))