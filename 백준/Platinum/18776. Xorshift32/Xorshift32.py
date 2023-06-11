import sys
input_func=sys.stdin.readline

def xorshift32(x):
    filt=(1<<32)-1
    x^=x<<13
    x&=filt
    x^=x>>17
    x&=filt
    x^=x<<5
    x&=filt
    return x

def matmul(A,B):
    n,m,k=len(A),len(A[0]),len(B[0])
    res = [[None for _ in range(k)] for _ in range(n)]
    for i in range(n):
        for j in range(k):
            cal = 0
            for t in range(m):
                cal += A[i][t]*B[t][j]
            res[i][j] = cal&1
    return res

def get_xorshift_mat(e):
    N = 32
    shift1 = [[1 if j==i-13 or i==j else 0 for j in range(N)] for i in range(N)]
    shift2 = [[1 if j==i+17 or i==j else 0 for j in range(N)] for i in range(N)]
    shift3 = [[1 if j==i-5 or i==j else 0 for j in range(N)] for i in range(N)]
    xorshift = matmul(matmul(shift3,shift2),shift1)
    for _ in range(e):
        xorshift = matmul(xorshift,xorshift)
    return xorshift

def to_vector(x):
    lst=[]
    for _ in range(32):
        if x&1:
            lst.append([1])
        else:
            lst.append([0])
        x>>=1
    return lst

def to_int(x):
    res = 0 
    for i in range(32):
        if x[i][0]:
            res|=1<<i
    return res

def baby_giant(x,t):
    xsh_str='''1 0 0 0 0 0 0 1 0 1 1 0 0 1 1 0 0 1 0 0 0 0 0 1 1 0 1 1 0 1 0 0
    1 0 1 0 0 1 1 0 0 1 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 1 0
    0 1 1 0 0 1 1 0 0 0 1 0 1 0 0 0 0 0 0 1 0 0 1 1 1 1 1 0 1 1 0 1
    0 1 1 1 1 0 1 0 1 1 1 1 1 1 1 0 0 1 1 1 0 0 0 0 0 0 1 0 0 1 0 0
    1 1 0 0 0 0 0 0 0 1 0 1 0 1 1 0 0 1 0 0 1 0 0 1 0 0 0 1 0 0 0 1
    1 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 1 1 0 1 0 0 0 1 1 1 0 0 1
    0 1 1 1 0 0 1 1 0 0 1 1 0 1 0 1 1 0 0 0 1 0 0 1 0 0 0 0 0 1 0 0
    1 1 0 0 0 0 1 0 0 1 1 0 0 0 0 0 0 1 0 1 1 1 0 0 1 1 0 0 1 0 0 0
    1 0 1 0 0 0 0 0 1 1 1 1 0 0 1 1 0 0 1 1 1 0 1 1 1 1 0 1 0 0 0 1
    0 1 1 1 1 0 0 0 0 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 1 0 1 1 0 1 0 1
    1 1 0 0 1 1 1 0 1 1 0 1 1 1 0 0 0 1 1 0 0 1 1 1 0 0 0 0 1 1 0 1
    1 1 0 0 0 1 0 1 1 1 0 1 0 0 0 1 1 1 0 1 1 1 0 0 1 0 1 1 0 1 1 0
    0 1 0 1 0 0 1 1 1 0 1 1 0 1 1 1 0 0 0 1 1 0 0 1 0 1 0 0 1 0 1 1
    1 0 1 1 1 1 1 0 1 1 1 1 0 0 1 1 1 0 0 0 1 1 0 0 0 1 0 0 1 0 0 1
    1 0 1 1 1 1 0 1 1 1 1 0 0 0 0 1 1 0 1 1 1 0 0 0 0 1 0 1 1 1 1 1
    1 0 0 1 0 0 0 0 1 0 1 0 1 1 1 0 0 1 0 0 1 0 1 1 0 0 0 0 1 1 0 1
    1 1 1 0 0 0 1 0 1 0 0 0 0 0 0 1 0 0 1 0 0 1 1 0 1 0 0 1 0 1 0 0
    0 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 0 1 0 0 1 0 0 1 0 1 0 0 0 1 1 0
    0 1 0 0 1 0 1 1 1 0 1 1 0 1 0 0 1 1 0 0 0 1 1 1 0 1 0 0 1 0 0 0
    1 1 1 1 0 0 0 1 1 1 0 0 1 1 0 0 1 0 1 0 0 1 0 1 0 0 1 1 0 0 0 1
    1 0 0 1 0 0 0 1 0 1 1 0 1 0 0 1 1 1 0 0 1 0 1 0 1 1 0 1 0 0 0 0
    0 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1 1 1 1 0 0 1 0 1 1 1 1 1 0
    0 0 1 0 0 0 0 0 0 1 1 0 0 0 1 1 0 0 1 1 1 1 1 0 0 1 1 1 0 1 1 1
    0 0 0 1 0 0 1 1 1 1 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 1 1 1 1 1 0 0
    0 0 0 1 1 1 0 1 0 1 0 1 0 1 0 0 1 0 0 1 1 1 0 1 0 1 0 1 1 0 1 1
    1 1 1 0 0 1 1 1 1 1 1 1 0 0 0 0 1 0 1 1 1 0 1 0 0 0 0 1 1 1 0 1
    0 1 0 1 0 1 1 1 0 1 0 0 1 0 0 0 0 0 1 0 1 1 0 0 1 0 1 0 0 0 0 0
    1 1 1 0 1 1 0 1 1 1 0 1 1 1 1 1 0 0 1 0 1 1 1 1 1 0 1 0 1 1 0 0
    1 1 0 0 1 0 1 0 0 0 0 0 1 1 0 1 1 0 1 0 1 1 0 0 0 1 0 0 1 1 0 1
    0 0 0 0 1 0 1 0 1 1 0 1 0 1 1 1 0 0 1 0 0 0 0 0 0 1 1 1 1 0 1 1
    0 0 1 0 0 1 0 1 1 0 1 0 0 1 0 0 0 0 1 0 1 0 0 1 0 0 0 1 0 1 0 0
    0 0 0 1 0 1 1 0 0 1 1 1 0 0 1 1 1 0 0 0 0 1 0 0 0 1 0 1 1 1 0 1'''
    xsh_m=[[] for _ in range(32)]
    for i in range(32):
        xsh_m[i]=list(map(int,(xsh_str.split('\n')[i]).split()))
    N_baby = 2**16+1
    N_giant = 2**16+1
    baby={}
    y = t
    for i in range(N_baby):
        baby[y] = i
        y = xorshift32(y)
    z = x
    for i in range(N_giant):
        if z in baby:
            return 1+((2**16)*i-baby[z])%(2**32-1)
        res = 0
        for i in range(32):
            cal = 0
            for j in range(32):
                cal^=xsh_m[i][j]&((z>>j)&1)
            res = res|(cal<<i)
        z = res

if __name__ == '__main__':
    x,t=map(int,input_func().split())
    # xorshift_mult = get_xorshift_mat(16)
    print(baby_giant(x,t))
    
    # x=357635132
    # t=x
    # for i in range(9457835):
    #     t=xorshift32(t)
    # print(x,t)
    # print(baby_giant(xorshift_mult,x,t))
    
    
    # from random import randint
    # cout=0
    # while True:
    #     cout+=1
    #     if cout%100==0:
    #         print(cout)
    #     x= randint(1,2**32-1)
    #     ans = randint(2**16,2**21)
    #     t=x
    #     for _ in range(ans-1):
    #         t=xorshift32(t)
    #     if ans!=baby_giant(xorshift_mult,x,t):
    #         print(x,ans,t)
    #         break