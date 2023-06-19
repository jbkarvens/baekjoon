import sys
input = sys.stdin.readline

def resultant(A,B,mod):
    n,m = len(A)-1,len(B)-1
    res = 1

    if m<n:
        n,m=m,n
        A,B=B,A
        if (n*m)&1:
            res = -1
    if n==0:
        return (res*pow(A[0],m,mod))%mod

    R = B[:]
    a_inv = pow(A[-1],-1,mod)
    for i in reversed(range(n,m+1)):
        if R[i]:
            t = (R[i]*a_inv)%mod
            for j in range(n+1):
                R[i-j] = (R[i-j]-t*A[n-j])%mod

    while len(R)>0 and R[-1]==0:
        R.pop()
        if len(R)==0:
            return 0
    res = (res*pow(A[-1],m-len(R)+1,mod))%mod
    return (res*resultant(A,R,mod))%mod

def poly_mult(f,g,p):
    n=len(f)-1
    m=len(g)-1
    res = [0 for _ in range(n+m+1)]
    for i in range(n+1):
        for j in range(m+1):
            res[i+j]+=f[i]*g[j]
    for i in range(len(res)):
        res[i]%=p
    while len(res)>1 and res[-1]==0:
        res.pop()
    return res

def poly_add(f,g,p):
    n=len(f)-1
    m=len(g)-1
    res=[0 for _ in range(max(n,m)+1)]
    for i in range(n+1):
        res[i]=f[i]
    for j in range(m+1):
        res[j]=(res[j]+g[j])%p
    while len(res)>1 and res[-1]==0:
        res.pop()
    return res

def poly_sub(f,g,p):
    n=len(f)-1
    m=len(g)-1
    res=[0 for _ in range(max(n,m)+1)]
    for i in range(n+1):
        res[i]=f[i]
    for j in range(m+1):
        res[j]=(res[j]-g[j])%p
    while len(res)>1 and res[-1]==0:
        res.pop()
    return res

def poly_mod(f,g,p):
    n=len(f)-1
    m=len(g)-1
    res = f[:]
    a0=pow(g[-1],-1,p)
    for i in reversed(range(n-m+1)):
        a = res[i+m]*a0
        for j in range(m+1):
            res[i+j]-=a*g[j]
    for i in range(len(res)):
        res[i]%=p
    while len(res)>1 and res[-1]==0:
        res.pop()
    return res

def get_poly(n,p):
    s=[]
    tmp = n
    while tmp>1:
        s.append(tmp&1)
        tmp>>=1
    s.reverse()
    A0=[[[0],[1]],[[-1],[2,1]]]
    A=[[[0],[1]],[[-1],[2,1]]]
    for t in s:
        a00 = poly_add(poly_mult(A[0][0], A[0][0],p),poly_mult(A[0][1],A[1][0],p),p)
        a01 = poly_add(poly_mult(A[0][0], A[0][1],p),poly_mult(A[0][1],A[1][1],p),p)
        a10 = poly_add(poly_mult(A[1][0], A[0][0],p),poly_mult(A[1][1],A[1][0],p),p)
        a11 = poly_add(poly_mult(A[1][0], A[0][1],p),poly_mult(A[1][1],A[1][1],p),p)
        A[0][0],A[0][1],A[1][0],A[1][1]=a00,a01,a10,a11
        if t:
            a00 = poly_add(poly_mult(A[0][0], A0[0][0],p),poly_mult(A[0][1],A0[1][0],p),p)
            a01 = poly_add(poly_mult(A[0][0], A0[0][1],p),poly_mult(A[0][1],A0[1][1],p),p)
            a10 = poly_add(poly_mult(A[1][0], A0[0][0],p),poly_mult(A[1][1],A0[1][0],p),p)
            a11 = poly_add(poly_mult(A[1][0], A0[0][1],p),poly_mult(A[1][1],A0[1][1],p),p)
            A[0][0],A[0][1],A[1][0],A[1][1]=a00,a01,a10,a11
    return poly_add(A[0][0],poly_mult(A[0][1],[1,1],p),p)

# f_m%f_n
def get_poly_mod(n,g,p,mode=-1):
    s=[]
    tmp = n
    while tmp>1:
        s.append(tmp&1)
        tmp>>=1
    s.reverse()
    A0=[[[0],[1]],[[-1],[2,mode]]]
    A=[[[0],[1]],[[-1],[2,mode]]]
    for t in s:
        a00 = poly_add(poly_mult(A[0][0], A[0][0],p),poly_mult(A[0][1],A[1][0],p),p)
        a01 = poly_add(poly_mult(A[0][0], A[0][1],p),poly_mult(A[0][1],A[1][1],p),p)
        a10 = poly_add(poly_mult(A[1][0], A[0][0],p),poly_mult(A[1][1],A[1][0],p),p)
        a11 = poly_add(poly_mult(A[1][0], A[0][1],p),poly_mult(A[1][1],A[1][1],p),p)
        a00 = poly_mod(a00,g,p)
        a01 = poly_mod(a01,g,p)
        a10 = poly_mod(a10,g,p)
        a11 = poly_mod(a11,g,p)
        A[0][0],A[0][1],A[1][0],A[1][1]=a00,a01,a10,a11
        if t:
            a00 = poly_add(poly_mult(A[0][0], A0[0][0],p),poly_mult(A[0][1],A0[1][0],p),p)
            a01 = poly_add(poly_mult(A[0][0], A0[0][1],p),poly_mult(A[0][1],A0[1][1],p),p)
            a10 = poly_add(poly_mult(A[1][0], A0[0][0],p),poly_mult(A[1][1],A0[1][0],p),p)
            a11 = poly_add(poly_mult(A[1][0], A0[0][1],p),poly_mult(A[1][1],A0[1][1],p),p)
            a00 = poly_mod(a00,g,p)
            a01 = poly_mod(a01,g,p)
            a10 = poly_mod(a10,g,p)
            a11 = poly_mod(a11,g,p)
            A[0][0],A[0][1],A[1][0],A[1][1]=a00,a01,a10,a11
    if mode==-1:
        return poly_add(A[0][0],poly_mult(A[0][1],[1,-1],p),p)
    else:
        return poly_add(poly_mult(A[0][0],[0,1],p),poly_mult(A[0][1],[0,2,1],p),p)

def solve(n,m,p):
    if n==1:
        return 1-m%2
    elif m==1:
        return 1-n%2
    if n%2==m%2==0:
        n,m=n//2,m//2
        f = get_poly(n,p)
        g = get_poly_mod(m,f,p)
        return resultant(f,g,p)
    elif n%2==0 and m%2==1:
        n,m=n//2,(m+1)//2
        f = get_poly(n,p)
        for i in range(len(f)):
            if i&1:
                f[i]=-f[i]
        g = get_poly_mod(m-1,f,p,1)
        return resultant(g,f,p)
    elif n%2==1 and m%2==0:
        n,m=(n+1)//2,m//2
        f = poly_sub(get_poly(n,p),get_poly(n-1,p),p)
        g = get_poly_mod(m,f,p)
        return resultant(f,g,p)
    else:
        return 0


if __name__=='__main__':
    for _ in range(int(input())):
        n,m,p = map(int, input().split())
        sys.stdout.write(f'{solve(n,m,p)}\n')