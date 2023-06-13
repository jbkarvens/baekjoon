import sys
import math
input_func = sys.stdin.readline

# irreducible poly in Z_2
def irr(n):
    lst = [[1,1],
           [1,1,1],
           [1,1,0,1],
           [1,1,0,0,1],
           [1,0,1,0,0,1],
           [1,1,0,0,0,0,1],
           [1,1,0,0,0,0,0,1],
           [1,1,0,1,0,1,0,0,1],
           [1,1,0,0,0,0,0,0,0,1],
           [1,0,0,1,0,0,0,0,0,0,1],
           [1,0,1,0,0,0,0,0,0,0,0,1],
           [1,0,0,1,0,0,0,0,0,0,0,0,1]]
    return lst[n-1]

def poly_mult(x,y):
    n,m = len(x)-1,len(y)-1
    z = [0 for _ in range(n+m+1)]
    for i in range(n+1):
        for j in range(m+1):
            z[i+j] = z[i+j] ^ (x[i] & y[j])
    return z

def poly_mod(x,y):
    n,m = len(x)-1,len(y)-1
    r = x[:]
    for i in reversed(range(m,n+1)):
        if r[i]:
            for j in range(m+1):
                r[i+j-m]^=y[j]
    return r

def to_poly(n):
    res = []
    while n:
        res.append(n&1)
        n>>=1
    return res

def to_int(x):
    cal = 0
    for i,v in enumerate(x):
        if v:
            cal|=(1<<i)
    return cal

def solve(n):
    if n<=3:
        return [1]
    elif n<=49:
        return [1,2,3,4]
    s = int(math.sqrt(n/2))
    e = math.ceil(math.log2(s+1))
    irrf = irr(e)
    ans = []
    for i in range(1,min(1<<e, s+1)):
        z = to_poly(i)
        z3 = poly_mult(z,poly_mult(z,z))
        z3m = poly_mod(z3, irrf)
        i1 = to_int(z3m)
        i2 = i
        ans.append((i2*(1<<e))|i1)
    if ans[-1]>n:
        ans.pop()
        ans.append(1<<(2*e-1))
    return ans

if __name__=='__main__':
    n = int(input_func())
    lst = solve(n)
    print(len(lst))
    print(*lst)