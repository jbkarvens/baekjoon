import sys
N,M=map(int,sys.stdin.readline().split())
pkm=dict()
for i in range(N):
    name_=sys.stdin.readline().rstrip()
    pkm[name_]=i+1
    pkm[i+1]=name_
for _ in range(M):
    q=sys.stdin.readline().rstrip()
    if q.isdigit():
        print(pkm[int(q)])
    else:
        print(pkm[q])