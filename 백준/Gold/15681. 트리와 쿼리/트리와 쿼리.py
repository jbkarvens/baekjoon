import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N,R,Q=map(int,input().split())
adj=[[] for _ in range(N+1)]
for _ in range(N-1):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

parent=[None for i in range(N+1)]
size=[None for i in range(N+1)]

def maketree(cur_node,parent_node):
    parent[cur_node]=parent_node
    size[cur_node]=1
    for v in adj[cur_node]:
        if v==parent_node:
            continue
        maketree(v,cur_node)
        size[cur_node]+=size[v]

maketree(R,-1)

for _ in range(Q):
    print(size[int(input())])