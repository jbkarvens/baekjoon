import sys
input_func=sys.stdin.readline

NUM = 10**9 + 7
B_MAX = 2 * 10**5

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
    tot = totient(B_MAX)
    
    for _ in range(int(input_func())):
        K = int(input_func())
        A, B = [], []
        for _ in range(K):
            a, b = map(int, input_func().split())
            A.append(a)
            B.append(b)
        
        P, Q = 0, 1
        for d in range(1, min(B) + 1):
            prod = 1
            for ai, bi in zip(A, B):
                prod *= (bi // d - (ai - 1) // d)
            P += tot[d] * prod
        for ai, bi in zip(A, B):
            Q *= (bi - ai + 1)
        u, v = P, Q
        while v > 0:
            u, v = v, u % v
        if (Q // u) % NUM == 0:
            print(-1)
        else:
            print((-(P // u) * pow(Q // u, -1, NUM)) % NUM)