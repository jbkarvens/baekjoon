import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def sc(v):
    global ii
    idx[v]=ii
    low[v]=ii
    ii+=1
    stack.append(v)
    ons[v]=True
    
    for w in E[v]:
        if idx[w]==None:
            sc(w)
            low[v]=min(low[v],low[w])
        elif ons[w]:
            low[v]=min(low[v],idx[w])
    if low[v]==idx[v]:
        scc.append([])
        w=None
        while w!=v and stack:
            w=stack.pop()
            ons[w]=False
            scc[-1].append(w)
        

N,M=map(int,input().split())
scc=[]
idx=dict()
low=dict()
ons=dict()
E=dict()
stack=[]
ii=0
for i in range(1,N+1):
    idx[i]=None
    idx[-i]=None
    low[i]=None
    low[-i]=None
    ons[i]=False
    ons[-i]=False
    E[i]=set()
    E[-i]=set()
for _ in range(M):
    i,j=map(int,input().split())
    E[-i].add(j)
    E[-j].add(i)
for v in idx:
    if idx[v]==None:
        sc(v)
suc=True
for comp in scc:
    for v in comp:
        if -v in comp:
            suc=False
            break
if suc:
    print(1)
else:
    print(0)