import sys
input=sys.stdin.readline

for i in range(int(input())):
    r,g,b,k=map(int, input().split())
    mod=10**9+7
    ans = -pow(b,k,mod)*pow(pow(1+b,k,mod),-1,mod)*r+r+k+k*g*pow(b,-1,mod)
    ans%=mod
    sys.stdout.write(f'{ans}\n')