import sys
input=sys.stdin.readline

n=int(input())
u,v=map(int,input().split())
E=[[] for _ in range(n+1)]
for _ in range(int(input())):
    x,y=map(int,input().split())
    E[x].append(y)
    E[y].append(x)
chon=[-1]

def dfs(cnt,node,node_before):
    if node==v:
        chon[0]=cnt
        return
    for w in E[node]:
        if w==node_before:
            continue
        dfs(cnt+1,w,node)
    return

dfs(0,u,u)
print(chon[0])