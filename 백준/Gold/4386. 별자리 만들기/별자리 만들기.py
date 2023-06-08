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

n=int(input())
coor=[]
for _ in range(n):
    coor.append(list(map(float,input().split())))
E=[]
for i in range(n):
    for j in range(i):
        d=((coor[i][0]-coor[j][0])**2+(coor[i][1]-coor[j][1])**2)**0.5
        E.append([d,i,j])
root=list(range(n))
rank=[1 for _ in range(n)]

E.sort()
ans=0
idx=0
for _ in range(n-1):
    while True:
        c,i,j=E[idx]
        rt_i=find(i)
        rt_j=find(j)
        if rt_i==rt_j:
            idx+=1
            continue
        union(i,j)
        ans+=c
        break
print(round(ans,2))