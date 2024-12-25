import sys
sys.setrecursionlimit(10**4)
input=sys.stdin.readline

N,M=map(int,input().split())
root=[i for i in range(N+1)]

def find(x):
    if x==root[x]:
        return x
    root[x]=find(root[x])
    return root[x]

def union(x,y):
    x=find(x)
    y=find(y)
    if x!=y:
        root[x]=y

for _ in range(M):
    u,v=map(int,input().split())
    union(u,v)
for i in range(1,N+1):
    find(i)
print(len(set(root[1:])))