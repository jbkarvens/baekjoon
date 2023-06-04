import sys
input=sys.stdin.readline

INF=10**8
N,M=map(int,input().split())
edge=[]
for _ in range(M):
    edge.append(list(map(int,input().split())))
d=[INF for _ in range(N+1)]
d[1]=0
for _ in range(N-1):
    for a,b,t in edge:
        if not d[a]==INF and d[a]+t<d[b]:
            d[b]=d[a]+t
chk=False
for a,b,t in edge:
    if not d[a]==INF and d[a]+t<d[b]:
        chk=True
        break
if chk:
    print(-1)
else:
    for i in range(2,N+1):
        if d[i]==INF:
            print(-1)
        else:
            print(d[i])