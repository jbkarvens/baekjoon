import math
d,k=map(int,input().split())
g=math.gcd(d,k)
a=d
if d%4==2 and k%2==0 and k>2:
    a*=2
while g>1:
    a*=g
    k//=g
    g=math.gcd(d,k)
print(a)