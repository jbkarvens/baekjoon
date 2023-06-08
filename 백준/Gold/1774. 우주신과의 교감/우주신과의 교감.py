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
root=list(range(n+1))
rank=[1 for _ in range(n+1)]
x,y=[None],[None]
for _ in range(n):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)
E=[]
for i in range(1,n+1):
    for j in range(1,i):
        d=((x[i]-x[j])**2+(y[i]-y[j])**2)**0.5
        E.append([d,i,j])
E.sort()

for _ in range(m):
    a,b=map(int,input().split())
    union(a,b)

ans=0
idx=0
while True:
    if rank[find(1)]==n:
        break
    d,i,j=E[idx]
    rt_i=find(i)
    rt_j=find(j)
    if rt_i==rt_j:
        idx+=1
        continue
    union(i,j)
    ans+=d
print(f'{round(ans,2):.2f}')
    