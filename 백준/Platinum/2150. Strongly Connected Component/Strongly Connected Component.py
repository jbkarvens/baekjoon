import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def strongconnect(v):
    index[v]=idx_num[0]
    lowlink[v]=idx_num[0]
    idx_num[0]+=1
    stack.append(v)
    onstack[v]=True
    for w in adj[v]:
        if index[w]==None:
            strongconnect(w)
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

if __name__=='__main__':
    V,E=map(int,input().split())
    adj=[[] for _ in range(V+1)]
    for _ in range(E):
        a,b=map(int, input().split())
        adj[a].append(b)
    index=[None for _ in range(V+1)]
    idx_num=[0]
    stack=[]
    onstack=[False for _ in range(V+1)]
    lowlink=[None for _ in range(V+1)]
    scc=[]
    for node in range(1,V+1):
        if index[node]==None:
            strongconnect(node)
    for component in scc:
        component.sort()
    scc.sort(key=lambda x:x[0])
    sys.stdout.write(f'{len(scc)}\n')
    for component in scc:
        for element in component:
            sys.stdout.write(f'{element} ')
        sys.stdout.write('-1\n')