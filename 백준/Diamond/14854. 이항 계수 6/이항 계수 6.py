import sys
import math
input = sys.stdin.readline

def work(binom,p):
    binom[0][0]=1
    for i in range(1, p):
        binom[i][0]=1
        for j in range(1, i+1):
            binom[i][j] = (binom[i-1][j-1]+binom[i-1][j])%p

def work2():
    res = 1
    fact27[0]=1
    for i in range(1,27):
        j = i
        if i%3==0:
            j=1
        res=(res*j)%27
        fact27[i]=res
    
    n= len(inv)
    for i in range(n):
        if math.gcd(i,n)>1:
            continue
        inv[i] = pow(i,-1,n)

def CRT(rem,mod):
    res = 0
    modtot = 1
    for m in mod:
        modtot*=m
    for r,m in zip(rem,mod):
        mi=modtot//m
        res += mi*pow(mi,-1,m)*r
    return res%modtot

def binom_rem(n,k,binom,p):
    res = 1
    while n:
        res*=binom[n%p][k%p]
        n//=p
        k//=p
    return res%p

def p_val(n,p):
    res = 0
    while n:
        n//=p
        res+=n
    return res

def fact27_rem(n):
    res = 1
    while n:
        q,r=n//27,n%27
        if q%2==0:
            res = (res*fact27[r])%27
        else:
            res = (-res*fact27[r])%27
        n//=3
    return res

def binom27_rem(n,k):
    e = p_val(n,3)-p_val(k,3)-p_val(n-k,3)
    if e>=3:
        return 0
    return (pow(3,e)*fact27_rem(n)*pow(fact27_rem(k)*fact27_rem(n-k),-1,27))%27

def solve(n,k):
    return CRT([binom27_rem(n,k),binom_rem(n,k,binom11,11),binom_rem(n,k,binom13,13),binom_rem(n,k,binom37,37)],[27,11,13,37])

if __name__=='__main__':
    binom11 = [[0 for _ in range(11+1)] for i in range(11)]
    binom13 = [[0 for _ in range(13+1)] for i in range(13)]
    binom37 = [[0 for _ in range(37+1)] for i in range(37)]
    fact27 = [0 for _ in range(27)]
    inv=[0 for _ in range(142857)]
    work(binom11,11)
    work(binom13,13)
    work(binom37,37)
    work2()
    for _ in range(int(input())):
        N,K=map(int, input().split())
        print(solve(N,K))