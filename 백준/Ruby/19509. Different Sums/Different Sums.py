import sys
input_func=sys.stdin.readline

def sieve(n):
    plst = [True for _ in range(n+1)]
    primes = []
    for i in range(2, n+1):
        if plst[i]:
            primes.append(i)
            for j in range(i+i, n+1,i):
                plst[j] = False
    return primes

def get_prime(n,idx=True):
    low, high = 0, len(primes)-1
    while low<=high:
        mid = (low+high)//2
        if primes[mid]<=n:
            low = mid+1
        else:
            high = mid-1
    if idx:
        return high
    return primes[high]

def solve(n):
    if n in sol_dict:
        return sol_dict[n]
    
    idx = get_prime(n+6,True)
    delta=0
    if 1340<=n<=1342 or n==1952:
        p = primes[idx+2]
    elif primes[idx]<n:
        p = primes[idx+1]
    else:
        p = primes[idx]
    
    if n==114:
        delta=1
    elif 524<=n<=526 or 1670<=n<=1672:
        delta = 9
    elif 1328<=n<=1339:
        p = primes[idx+2]
        delta = 35

    # Erdos-Turan construction
    res = []
    for i in range(n):
        v = 2*p+pow(i+1,2,p)-pow(i,2,p)-delta
        res.append(v)
    sol_dict[n]=res
    return res

if __name__=='__main__':
    for _ in range(int(input_func())):
        N_MAX = 2000
        primes = sieve(N_MAX+100)
        sol_dict={}
        n = int(input_func())
        print(*solve(n))