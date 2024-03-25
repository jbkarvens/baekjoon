import sys
input=sys.stdin.readline

MOD = 10**9+7
NUM = 4*10**6
fact = [1]
res = 1
for i in range(1,NUM+1):
    res = (i*res)%MOD
    fact.append(res)

for _ in range(int(input())):
    n,k = map(int,input().split())
    print((fact[n]*pow(fact[k]*fact[n-k],-1,MOD))%MOD)