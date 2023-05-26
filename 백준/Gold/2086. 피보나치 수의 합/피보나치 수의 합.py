def fib(n,m):
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
k,n=map(int,input().split())
m=10**9
print((fib(n+2,m)-fib(k+1,m))%m)