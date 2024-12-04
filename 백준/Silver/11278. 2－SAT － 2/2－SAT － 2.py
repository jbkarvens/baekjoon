import sys
input=sys.stdin.readline

N,M=map(int,input().split())
C=[]
for _ in range(M):
    C.append(list(map(int,input().split())))
f_true=False
for xx in range(2**N):
    x=[(xx>>i)&1 for i in range(N)]
    success=True
    for clause in C:
        u,v=clause
        if u>0:
            uu=x[u-1]
        else:
            uu=1-x[-u-1]
        if v>0:
            vv=x[v-1]
        else:
            vv=1-x[-v-1]
        if uu==False and vv==False:
            success=False
            break
    if success:
        f_true = True
        break

if f_true:
    print(1)
    print(*x)
else:
    print(0)