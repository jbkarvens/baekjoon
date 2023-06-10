import sys
input_func=sys.stdin.readline

NUM = 10**9 + 7

def totient(n):
    tot = list(range(n + 1))
    for i in range(2, n + 1):
        if tot[i] != i:
            continue
        p = tot[i]
        for j in range(i, n + 1, i):
            tot[j] -= tot[j] // p
    return tot

if __name__ =='__main__':
    K = int(input_func())
    A, B = [], []
    for _ in range(K):
        a, b = map(int, input_func().split())
        A.append(a)
        B.append(b)
    
    B_MAX = max(B)
    tot = totient(B_MAX)
    B_min = min(B)
    inv = [1 for _ in range(B_MAX + 1)]
    for i in range(1, B_MAX + 1):
        inv[i] = pow(i, -1, NUM)
    dP = [1 for _ in range(B_MAX + 1)]
    dzero = [0 for _ in range(B_MAX + 1)]
    for i in range(K):
        d = 1
        res_bef = B[i] - A[i] + 1
        while d <= B[i]:
            res_cur = B[i] // d - (A[i] - 1) // d
            if d > 1:
                res_bef = B[i] // (d - 1) - (A[i] - 1) // (d - 1)
            if res_cur == 0:
                dzero[d] += 1
            else:
                dP[d] = (res_cur * dP[d]) % NUM
            if res_bef == 0:
                dzero[d] -= 1
            else:
                dP[d] = (dP[d] * inv[res_bef]) % NUM
            if A[i] - 1 >= d:
                d = min(B[i] // (B[i] // d), (A[i] - 1) // ((A[i] - 1) // d)) + 1
            else :
                d = B[i] // (B[i] // d) + 1
            
    P = 0
    P0 = 1
    zero_cout = 0
    for i in range(K):
        P0 = (P0 * (B[i] - A[i] + 1)) % NUM
    prod = P0
    for d in range(1, B_min + 1):
        prod = (prod * dP[d]) % NUM
        zero_cout += dzero[d]
        if zero_cout == 0:
            P = (P + tot[d] * prod) % NUM
    print(P)