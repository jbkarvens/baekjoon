import sys
input_func=sys.stdin.readline
sys.setrecursionlimit(10**6)

def resultant(A,B):
    mod = 10**9+7
    n,m = len(A)-1,len(B)-1
    res = 1

    if m>n:
        n,m=m,n
        A,B=B,A
        if (n*m)&1:
            res = -1
    if m==0:
        return (res*pow(B[0],n,mod))%mod

    R = A[:]
    b_inv = pow(B[-1],-1,mod)
    for i in reversed(range(m,n+1)):
        if R[i]:
            t = (R[i]*b_inv)%mod
            for j in range(m+1):
                R[i-j] = (R[i-j]-t*B[m-j])%mod

    while len(R)>0 and R[-1]==0:
        R.pop()
        if len(R)==0:
            return 0
    res = (res*pow(B[-1],n-len(R)+1,mod))%mod
    return (res*resultant(R,B))%mod
    

def solve(A,P,N):
    mod = 10**9+7
    start = 1
    parity = 0
    onepos = [None for _ in range(N)]
    onepos[0] = 0
    oneposidx = [None for _ in range(N)]
    oneposidx[0]=0
    flow = []
    for i in range(N-1):
        start = P[start-1]
        flow.append(start-1)
        if start == 1:
            return 0
    flow = flow[::-1]
    for i in range(N-1):
        onepos[i+1] = flow[i]
        oneposidx[flow[i]]=i+1
    for i in range(N):
        j = onepos[i]
        if i==j:
            continue
        parity+=1
        A[i],A[j] = A[j],A[i]
        k = oneposidx[i]
        onepos[i],onepos[k] = i,j
        oneposidx[i],oneposidx[j] = i, k
    parity%=2
    B = [0 for _ in range(N+1)]
    B[0],B[N] = mod-1,1
    
    if parity==0:
        return resultant(A,B)
    else:
        return (-resultant(A,B))%mod

if __name__=='__main__':
    N = int(input_func())
    A = [*map(int, input_func().split())]
    P = [*map(int, input_func().split())]
    ans = solve(A,P,N)
    print(ans)