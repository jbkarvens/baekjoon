import math
N,M,K = map(int,input().split())
A = list(map(int,input().split()))

L = math.lcm(*A)
def solve():
    a,mod=A[0]-1,A[0]
    for i in range(2,K+1):
        b,y=A[i-1]-i,A[i-1]
        g=math.gcd(y,mod)
        if (a-b)%g!=0:
            return False
        t = (a-b)//g*pow(y//g,-1,mod//g)
        a=b+y*t
        mod=math.lcm(mod,y)
        a%=mod
        if mod>=N or a+K>=M:
            return False
    if mod>=N or a+K>=M:
        return False
    for i in range(1,K+1):
        if math.gcd(mod,a+i)!=A[i-1]:
            return False
    return True

if solve():
    print("YES")
else:
    print("NO")