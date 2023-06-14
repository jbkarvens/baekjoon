def getfirst(M):
    nmax=3
    while M>(nmax-2)*nmax**3:
        nmax+=1
    M-=(nmax-3)*(nmax-1)**3
    a=(M-1)//(nmax*nmax*(nmax-2)-(nmax-1)*(nmax-1)*(nmax-3))+1
    a=min(a,nmax)
    M-=(a-1)*(nmax*nmax*(nmax-2)-(nmax-1)*(nmax-1)*(nmax-3))
    if a!=nmax:
        b=(M-1)//(nmax*(nmax-2)-(nmax-1)*(nmax-3))+1
        b=min(b,nmax)
        M-=(b-1)*(nmax*(nmax-2)-(nmax-1)*(nmax-3))
    else:
        b=(M-1)//(nmax*(nmax-2))+1
        M-=(b-1)*(nmax*(nmax-2))
    if a!=nmax and b!=nmax:
        if M<=nmax-1:
            c,n=M,nmax
        else:
            c,n=nmax,M-nmax+3
    else:
        c=(M-1)//(nmax-2)+1
        n=M-(c-1)*(nmax-2)+2
    return a,b,c,n

def getnext(a,b,c,n):
    if max(a,b,c)>n:
        return a,b,c,n+1
    elif max(a,b,c)<n:
        if c==n-1:
            return a,b,n,3
        else:
            return a,b,c+1,n
    else:
        if c==n:
            if b==n:
                if a==n:
                    return 1,1,1,n+1
                else:
                    if a<n-1:
                        return a+1,1,1,n
                    else:
                        return a+1,1,1,3
            else:
                if a==n:
                    return n,b+1,1,3
                else:
                    if b<n-1:
                        return a,b+1,1,n
                    else:
                        return a,n,1,3
        else:
            return a,b,c+1,3

def cmp(a,b,c,n):
    if a>=c or b>=c:
        return '>'
    if pow(a/c,n)+pow(b/c,n)>1:
        return '>'
    return '<'

if __name__=='__main__':
    l,r=map(int,input().split())
    a,b,c,n=getfirst(l)
    for _ in range(r-l+1):
        print(f'{a}^{n}+{b}^{n}{cmp(a,b,c,n)}{c}^{n}')
        a,b,c,n=getnext(a,b,c,n)