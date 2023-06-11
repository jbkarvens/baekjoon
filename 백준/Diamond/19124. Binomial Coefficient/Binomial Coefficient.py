import sys
input_func=sys.stdin.readline

def fact_odd_naive(n,mod):
    res = 1
    for i in range(1,n+1,2):
        res = (res * i)%mod
    return res

def fact_odd(n,e):
    k = (e+1)//2
    mod = 1<<(2*k)
    kpow = 1<<k
    q = n//(kpow)
    ans = pow(fact_odd_naive(kpow,mod),q,mod)%(1<<e)
    for i in range(kpow*q+1,n+1,2):
        ans = (ans*i)%(1<<e)
    return ans

def fact(n,e):
    ans = 1
    mod=1<<e
    while n>1:
        ans=(ans*fact_odd(n,e))%mod
        n//=2
    return ans

def fact_exp(n):
    res = 0
    while n>0:
        n//=2
        res+=n
    return res

n,k=map(int,input_func().split())
m=32
mod = 1<<m
e = fact_exp(n)-fact_exp(k)-fact_exp(n-k)
if e<m:
    ans = (fact(n,m)*pow(fact(k,m)*fact(n-k,m),-1,mod)*(1<<e))%mod
else:
    ans = 0
print(ans)