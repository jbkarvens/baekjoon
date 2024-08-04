import sys
input=sys.stdin.readline

p = 1000000007
res = 1
for i in range(2,501):
    res = (res*i)%p
fact = [pow(res,-1,p)]
for i in reversed(range(1,501)):
    fact.append((fact[-1]*i)%p)
fact.reverse()
factprod=[1]
for f in fact:
    factprod.append((factprod[-1]*f)%p)
for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().split()))
    res = factprod[n]
    for i in range(n):
        for j in range(i+1,n):
            res = (res*(A[j]-A[i]))%p
    print(res)