import sys
input=sys.stdin.readline

def solve(n,m):
    # mult f,g then mod poly
    def poly_mult(f,g,poly):
        mod=1999
        n = len(f)-1
        m = len(g)-1
        h=[0 for _ in range(n+m+1)]
        for i in range(n+1):
            for j in range(m+1):
                h[i+j]+=f[i]*g[j]
        n=len(h)-1
        m=len(poly)-1
        for i in reversed(range(n-m+1)):
            a=h[i+m]
            for j in range(m+1):
                h[i+j]-=a*poly[j]
        for i in range(n+1):
            h[i]%=mod
        while len(h)>1 and h[-1]==0:
            h.pop()
        return h
    
    mod = 1999
    A = [0 for _ in range(n+1)]
    for i in range(1,n):
        res = 1
        for j in range(1,i):
            res += A[j]
        A[i] = res%mod
    res = 1
    alpha = 1
    for j in range(1,n):
        alpha+=A[j]
        res+=2*A[j]
    A[n] = res%mod
    alpha%=mod
    if m<=n:
        return A[m]
    
    poly = [-1 for _ in range(n+2)]
    poly[-1]=1
    poly[1]=-alpha
    poly[0]=0
    
    e = []
    tmp = m
    while tmp>1:
        e.append(tmp&1)
        tmp>>=1
    e.reverse()
    
    res = [0,1]
    for t in e:
        res = poly_mult(res,res,poly)
        if t:
            res = poly_mult(res,[0,1],poly)
    ans = 0
    for i in range(n+1):
        ans += A[i]*res[i]
    return ans%mod
    

if __name__=='__main__':
    N,M=map(int,input().split())
    print(solve(N,M))