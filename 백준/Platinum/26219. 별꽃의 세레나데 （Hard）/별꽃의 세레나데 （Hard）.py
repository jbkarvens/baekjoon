import sys
input_func = sys.stdin.readline

if __name__=='__main__':
    mod = 998244353
    N = int(input_func())
    M,A = [], []
    for _ in range(N):
        mi, ai = map(int, input_func().split())
        M.append(mi)
        A.append(ai)
    sumA=sum(A)
    
    S_idx = []
    tmp = 1
    for i in range(N):
        S_idx.append(tmp)
        tmp*=(1+M[i])
    dp = dict()
    dp[0]=0
    tot= 1
    inv = dict()
    for S in range(1,1<<N):
        res = 0
        for i in range(N):
            if S&(1<<i):
                res+=A[i]
        inv[res] = pow(res,-1,mod)
    
    for i in range(N):
        tot *=(M[i]+1)
    for S in range(1,tot):
        S0=S
        div = sumA
        res = sumA
        for i in range(N):
            t = S%(1+M[i])
            if t==0:
                div-=A[i]
            else:
                res+=A[i]*dp[S0-S_idx[i]]
            S//=(1+M[i])
        dp[S0] = (res*inv[div])%mod
    print(dp[tot-1])