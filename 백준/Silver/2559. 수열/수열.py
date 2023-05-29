N,K=map(int,input().split())
A=list(map(int,input().split()))
B=[0 for _ in range(N+1)]
for i in range(1,N+1):
    B[i]=B[i-1]+A[i-1]
print(max([B[i+K]-B[i] for i in range(0,N-K+1)]))