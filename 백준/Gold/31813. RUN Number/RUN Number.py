import sys
input=sys.stdin.readline

def solve(n):
    if n==0:
        return []
    e=1
    while e<=n:
        e=10*e+1
    e//=10
    e*=(n//e)
    return [e]+solve(n-e)
    

for _ in range(int(input())):
    N,K=map(int,input().split())
    arr=solve(K)
    print(len(arr))
    print(*arr)