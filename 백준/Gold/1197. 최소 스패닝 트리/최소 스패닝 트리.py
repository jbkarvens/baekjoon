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

n,m=map(int,input().split())
E=[]
for _ in range(m):
    a,b,c=map(int,input().split())
    E.append([a,b,c])
E.sort(key=lambda x: x[2])
root=[i for i in range(n+1)]
rank=[1 for i in range(n+1)]
ans=0
idx=0
for i in range(n-1):
    while True:
        a,b,c=E[idx]
        rt_a=find(a)
        rt_b=find(b)
        if rt_a==rt_b:
            idx+=1
            continue
        union(a,b)
        ans+=c
        idx+=1
        break
print(ans)