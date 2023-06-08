import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
weight = list(map(int,input().split()))
weight.insert(0,None)
adj=[[] for _ in range(N + 1)]
for _ in range(N-1):
    u, v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

# 0/1 : i 마을 안고른/고른 경우 i node의 subtree에서 최대 weight 합
dp0 = [None for _ in range(N + 1)]
dp1 = [None for _ in range(N + 1)]

# 0-0-0으로 이어지면 최대가 아니므로 이 case는 걱정할 필요 없음
def dp_tree(current_node, parent_node):
    dp0[current_node] = 0
    dp1[current_node] = weight[current_node]
    for v in adj[current_node]:
        if v == parent_node:
            continue
        dp_tree(v, current_node)
        dp0[current_node]+=max(dp0[v],dp1[v])
        dp1[current_node]+=dp0[v]

dp_tree(1,-1)
print(max(dp0[1], dp1[1]))