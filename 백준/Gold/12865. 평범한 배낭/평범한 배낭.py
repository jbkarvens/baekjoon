N,K=map(int,input().split())
lst=[]
for _ in range(N):
    lst.append(list(map(int,input().split())))
A=[[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(K+1):
        if j>=lst[i-1][0]:
            A[i][j]=max(A[i-1][j],A[i-1][j-lst[i-1][0]]+lst[i-1][1])
        else:
            A[i][j]=A[i-1][j]
print(A[N][K])