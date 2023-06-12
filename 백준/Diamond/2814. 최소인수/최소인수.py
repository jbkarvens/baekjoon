import sys
input_func = sys.stdin.readline

def sieve(n):
    table = [True for _ in range(n+1)]
    prime_list = []
    for i in range(2, n+1):
        if table[i]:
            prime_list.append(i)
            for j in range(i+i, n+1, i):
                table[j] = False
    return prime_list

def count(n,plst,cur_prod,i):
    if i==len(plst) or plst[i]*cur_prod>n:
        return 0
    res = n//(cur_prod*plst[i])
    res += count(n,plst,cur_prod,i+1)
    res -= count(n,plst,cur_prod*plst[i],i+1)
    return res

def solve(N,P):
    N_MAX = 10**9
    if N==1:
        return P
    if P*P>N_MAX:
        return 0
    if P*P*P>N_MAX:
        prime_list = sieve(10**6)
        for i, q in enumerate(prime_list):
            if q==P:
                break
        if N-2+i>=len(prime_list):
            return 0
        pp = prime_list[N-2+i]
        if pp*P>N_MAX:
            return 0
        return pp*P
    else:
        plst = sieve(P-1)
        low, high = 1, N_MAX//P
        if high-count(high,plst,1,0)<N:
            return 0
        while low<=high:
            mid = (low + high)//2
            if (mid-count(mid, plst,1,0))<N:
                low = mid + 1
            else:
                high = mid - 1
        ans = (high+1)*P
        if ans>N_MAX:
            return 0
        return ans
    

if __name__=='__main__':
    N_MAX = 10**9
    N, P = map(int,input_func().split())
    print(solve(N,P))