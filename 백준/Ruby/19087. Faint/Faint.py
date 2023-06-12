import sys
input_func = sys.stdin.readline

n,k,m=map(int,input_func().split())
if m>=2:
    mod=10**9+7
    a,b = (n-k)*(n-k-1)//2, (n-k+1)*(n-k)//2
    ans = a
    for i in range(3,m+1):
        a=(a*(n-k-2+i)*pow(i,-1,mod))%mod
        b=(b*(n-k-1+i)*pow(i,-1,mod))%mod
        ans=(ans+a)%mod
    ans=(ans+b)%mod
else:
    ans = n-k
print(ans)