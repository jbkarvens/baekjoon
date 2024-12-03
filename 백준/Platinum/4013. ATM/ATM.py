import sys
import collections
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# Get input
N,M=map(int,input().split())
D=[]
for _ in range(M):
    D.append(list(map(int,input().split())))
C=[]
for _ in range(N):
    C.append(int(input()))
S,P=map(int,input().split())
ATM=list(map(int,input().split()))

# find strongly connected components
graph=[[] for _ in range(N+1)]
for d in D:
    x,y=d
    graph[x].append(y)
scc=[i for i in range(N+1)]
stack = []
onstack=[False for _ in range(N+1)]
lowlink=[None for _ in range(N+1)]
index=[None for _ in range(N+1)]
cnt=0
scc=[]
visited=[False for _ in range(N+1)]

def dfs(v):
    visited[v]=True
    global cnt
    index[v]=cnt
    lowlink[v] = cnt
    cnt+=1
    stack.append(v)
    onstack[v]=True
    for w in graph[v]:
        if index[w]==None:
            dfs(w)
            lowlink[v]=min(lowlink[v],lowlink[w])
        elif onstack[w]:
            lowlink[v]=min(lowlink[v],index[w])
    if lowlink[v]==index[v]:
        scc.append([])
        while True:
            w=stack.pop()
            onstack[w]=False
            scc[-1].append(w)
            if w==v:
                break
            
for i in range(1,N+1):
    if not visited[i]:
        dfs(i)

# Create new scc graph
scc_N = len(scc)
scc_V = [None for _ in range(N+1)]
for i,comp in enumerate(scc):
    for v in comp:
        scc_V[v]=i
scc_E=[]
for comp in scc:
    check=set(comp)
    scc_E.append([])
    for v in comp:
        for w in graph[v]:
            if w not in check:
                scc_E[-1].append(scc_V[w])
                check.add(v)
scc_atm=[False for _ in range(scc_N)]
for v in ATM:
    scc_atm[scc_V[v]]=True
scc_S=scc_V[S]
scc_C=[0 for _ in range(scc_N)]
for v in range(N):
    scc_C[scc_V[v+1]]+=C[v]

# The solving bfs
deque=collections.deque()
# visited=[False for _ in range(scc_N)]

score=[0 for _ in range(scc_N)]
result = 0
deque.append(scc_S)
score[scc_S]=scc_C[scc_S]
while deque:
    v=deque.popleft()
    if scc_atm[v]:
        result=max(result,score[v])
    for w in scc_E[v]:
        if score[w]<score[v]+scc_C[w]:
            score[w]=score[v]+scc_C[w]
            deque.append(w)
print(result)