import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N=int(input())
w=list(map(int,input().split()))
w.insert(0,None)
adj=[[] for _ in range(N+1)]
for _ in range(N-1):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

# node i의 subtree의 maximal independent set 크기(0은 i포함하는 것 1은 포함 X)
dp0=[None for _ in range(N+1)]
dp0_node=[None for _ in range(N+1)]
dp1=[None for _ in range(N+1)]
dp1_node=[None for _ in range(N+1)]

def dp_tree(cur_node,parent_node):
    dp0[cur_node]=0
    dp0_node[cur_node]=[]
    dp1[cur_node]=w[cur_node]
    dp1_node[cur_node]=[cur_node]
    for v in adj[cur_node]:
        if parent_node==v:
            continue
        dp_tree(v,cur_node)
        if dp1[v]>dp0[v]:
            dp0[cur_node]+=dp1[v]
            dp0_node[cur_node]+=dp1_node[v]
        else:
            dp0[cur_node]+=dp0[v]
            dp0_node[cur_node]+=dp0_node[v]
        dp1[cur_node]+=dp0[v]
        dp1_node[cur_node]+=dp0_node[v]


dp_tree(1,-1)
a,b=dp0[1],dp1[1]
if a>b:
    print(a)
    dp0_node[1].sort()
    print(*dp0_node[1])
else:
    print(b)
    dp1_node[1].sort()
    print(*dp1_node[1])