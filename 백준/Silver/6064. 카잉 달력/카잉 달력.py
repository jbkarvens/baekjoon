import math
for _ in range(int(input())):
    M,N,x,y=map(int,input().split())
    g=math.gcd(M,N)
    if (x-y)%g!=0:
        print(-1)
        continue
    r=x+M*(y-x)//g*pow(M//g,-1,N//g)
    print(1+(r-1)%(M*N//g))