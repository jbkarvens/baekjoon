import sys
import cmath
input=sys.stdin.readline

while True:
    a,m,b,n = map(int,input().split())
    if (a,m,b,n) == (0,0,0,0):
        break
    am = pow(a,1/m)
    bn = pow(b,1/n)
    poly = [1]
    for t in range(m):
        for s in range(n):
            u = -am*(cmath.cos(2*cmath.pi*t/m) + cmath.sin(2*cmath.pi*t/m)*1j) -bn*(cmath.cos(2*cmath.pi*s/n) + cmath.sin(2*cmath.pi*s/n)*1j)
            tmp = [0 for _ in range(len(poly)+1)]
            for k in range(len(poly)):
                tmp[k] += poly[k]
                tmp[k+1] += poly[k]*u
            poly = tmp
    for k in range(len(poly)):
        poly[k] = round(poly[k].real)
    print(*poly)