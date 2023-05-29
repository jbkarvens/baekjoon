N,M=map(int,input().split())
lst=list(range(1,N+1))
for _ in range(M):
    i,j,k=map(int,input().split())
    lst[i-1:j]=lst[k-1:j]+lst[i-1:k-1]
print(*lst)