import sys
input=sys.stdin.readline
MR_TEST_LIST = [2,3,5,7,11]

def MR(n):
    s,tmp=0,n-1
    while tmp&1==0:
        tmp>>=1
        s+=1
    d=(n-1)>>s
    for a in MR_TEST_LIST:
        a_witness=False
        cal=pow(a,d,n)
        if cal==1 or cal==n-1:
            a_witness=True
            continue
        for _ in range(1,s):
            cal=pow(cal,2,n)
            if cal==n-1:
                a_witness=True
        if not a_witness:
            return False
    return True

def sieve(n):
    pchk=[True for _ in range(n+1)]
    primes=[]
    for i in range(2,n+1):
        if pchk[i]:
            primes.append(i)
            for j in range(i+i,n+1,i):
                pchk[j]=False
    return primes

def factor(n):
    if n<=1:
        return []
    for p in pfront:
        if n%p==0:
            return [p] + factor(n//p)
    if MR(n):
        return [n]
    for p in pback:
        if n%p==0:
            return [p] + factor(n//p)

def r4(n):
    if n==0:
        return 1
    factor_list=factor(n)
    factors=dict()
    for prime in factor_list:
        if prime in factors:
            factors[prime]+=1
        else:
            factors[prime]=1
    if 2 in factors:
        k=factors[2]
    else:
        k=0
    result=2**(min(k,1)+1)-1
    for prime in factors:
        if prime==2:
            continue
        result*=(prime**(factors[prime]+1)-1)//(prime-1)
    return 8*result

def r5(n):
    result=r4(n)
    i=1
    while i*i<=n:
        result+=2*r4(n-i*i)
        i+=1
    return result

if __name__=='__main__':
    plst=sieve(10**5)
    cut=6
    pfront=plst[:cut]
    pback=plst[cut:]
    n=int(input())
    sys.stdout.write(f'{r4(n)}\n')
    sys.stdout.write(f'{r5(n)}\n')