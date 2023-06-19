import sys
input = sys.stdin.readline
if __name__=='__main__':
    N,K = map(int,input().split())
    ans=1
    binom = 1
    mod = 10**9+7
    for i in range(1, N+1):
        if i%2==1:
            ans = (ans*(K+1)-binom)%mod
            binom=(K*binom*4*i*pow(i+3,-1,mod))%mod
        else:
            ans = (ans*(K+1))%mod
    print(ans)