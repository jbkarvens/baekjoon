import sys
input=sys.stdin.readline
       
INF=10**8 
V,E=map(int,input().split())
d=[[INF for _ in range(V+1)] for _ in range(V+1)]
for i in range(1,V+1):
    d[i][i]=0
for _ in range(E):
    a,b,c=map(int,input().split())
    d[a][b]=c

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            d[i][j]=min(d[i][j],d[i][k]+d[k][j])
for i in range(1,V+1):
    for j in range(i+1,V+1):
        d[i][j]+=d[j][i]
ans=INF
for i in range(1,V):
    ans=min(ans,min(d[i][i+1:]))
if ans==INF:
    print(-1)
else:
    print(ans)