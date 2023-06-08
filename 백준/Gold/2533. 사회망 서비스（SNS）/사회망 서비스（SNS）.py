import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

# dp1 : i 골랐을 때 i의 subtree에서 최솟값
# dp0 : i 안골랐을때
dp0 = [None for _ in range(N + 1)]
dp1 = [None for _ in range(N + 1)]

def dp_tree(current_node,parent_node):
    dp0[current_node] = 0
    dp1[current_node] = 1
    for v in adj[current_node]:
        if v == parent_node:
            continue
        dp_tree(v,current_node)
        dp0[current_node]+=dp1[v]
        dp1[current_node]+=min(dp0[v],dp1[v])

dp_tree(1,-1)
print(min(dp0[1],dp1[1]))