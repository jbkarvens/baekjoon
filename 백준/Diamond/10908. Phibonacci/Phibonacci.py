import sys
input_func=sys.stdin.readline

mod = 10**9+7
modsq = mod**2

def fib(n,m):
    if n==0:
        return 0
    a,b=1,1
    ls=[]
    while n>1:
        ls.append(n%2==1)
        n>>=1
    ls.reverse()
    for tf in ls:
        a,b=(a*(2*b-a))%m,(a*a+b*b)%m
        if tf:
            a,b=b,(a+b)%m
    return a

if __name__=='__main__':
    n,k=map(int,input_func().split())
    fkn=fib(k*n,modsq)
    fk=fib(k,modsq)
    if fk%mod==0:
        div = (fkn//mod * pow(fk//mod,-1,mod))%mod
    else:
        div = (fkn * pow(fk,-1,mod))%mod
    fknb = fib(k*n-1,mod)
    fkb = fib(k-1,mod)
    
    A = div
    B = (fknb - div*fkb)%mod
    print(A,B)