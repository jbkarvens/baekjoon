import sys
input_func=sys.stdin.readline

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

n=int(input_func())
mod=10**9+7
print((fib(n+(n+1)%2,mod)-1)%mod)