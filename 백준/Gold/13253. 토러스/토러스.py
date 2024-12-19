import sys
input=sys.stdin.readline

N,M,x,y=map(int, input().split())
u=0
nx,ny=0,0
fail=False
while not(nx==x and ny==y):
    u+=1
    nx=(nx+1)%N
    ny=(ny+1)%M
    if u>N*M:
        fail=True
        break
if fail:
    print(-1)
else:
    v=0
    nx,ny=0,0
    while not(nx==x and ny==y):
        v+=1
        nx=(nx-1)%N
        ny=(ny-1)%M
    n=u+v
    k=min(u,v)
    print(k*n-k*k)