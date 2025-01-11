import sys
input=sys.stdin.readline
print=sys.stdout.write
N,P=map(int,input().split())
res=1
M=5*10**8
if N<M:
    for i in range(1,N+1):
        res=(res*i)%P
    print(f'{res}')
else:
    tmp=1
    for i in range(N+1,P):
        tmp=(tmp*i)%P
    res=(-pow(tmp,-1,P))%P
    print(f'{res}')