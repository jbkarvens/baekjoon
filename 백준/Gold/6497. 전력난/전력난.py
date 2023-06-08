import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def find(x):
    if root[x]==x:
        return x
    root[x]=find(root[x])
    return root[x]

def union(x,y):
    rt_x=find(x)
    rt_y=find(y)
    if rt_x==rt_y:
        return
    if rank[rt_x]>rank[rt_y]:
        root[rt_y]=rt_x
        rank[rt_x]+=rank[rt_y]
    else:
        root[rt_x]=rt_y
        rank[rt_y]+=rank[rt_x]

while True:
    n,m=map(int,input().split())
    if n==m==0:
        break
    E=[]
    for _ in range(m):
        x,y,z=map(int,input().split())
        E.append([z,x,y])
    tot=0
    for c,_,_ in E:
        tot+=c
    E.sort()
    root=list(range(n))
    rank=[1 for _ in range(n)]
    cost=0
    idx=0
    while rank[find(0)]!=n:
        c,x,y=E[idx]
        rt_x=find(x)
        rt_y=find(y)
        if rt_x==rt_y:
            idx+=1
            continue
        union(x,y)
        cost+=c
    print(tot-cost)