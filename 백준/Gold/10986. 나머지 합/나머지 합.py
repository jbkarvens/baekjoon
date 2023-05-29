N,M=map(int,input().split())
A=list(map(int,input().split()))
R=[0 for _ in range(M)]
s=0
R[0]=1
for i in range(N):
    s=(s+A[i])%M
    R[s]+=1
ans=0
for i in range(M):
    ans+=R[i]*(R[i]-1)//2
print(ans)