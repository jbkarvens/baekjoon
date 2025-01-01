import sys
input=sys.stdin.readline

run=[]
for n in range(1,19):
    for e in range(1,10):
        run.append(e*(pow(10,n)-1)//9)

def solve(n,k):
    if n==0:
        return []
    if k==0:
        return False
    for i in range(len(run)):
        if n<run[i]:
            break
    while i>=0:
        i-=1
        arr=solve(n-run[i],k-1)
        if arr!=False:
            return [run[i]]+arr

for _ in range(int(input())):
    N,K=map(int,input().split())
    arr=solve(K,1+N)
    print(len(arr))
    print(*arr)