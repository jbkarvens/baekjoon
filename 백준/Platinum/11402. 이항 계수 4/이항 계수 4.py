N,K,M=map(int,input().split())
res=1
def fac(n,k):
    res=1
    for i in range(1,n+1):
        res=(res*i)%k
    return res
while N:
    n=N%M
    k=K%M
    N//=M
    K//=M
    if n==k==0:
        continue
    elif n<k:
        res=0
        break
    res=(res*fac(n,M)*pow(fac(k,M)*fac(n-k,M),-1,M))%M
print(res)