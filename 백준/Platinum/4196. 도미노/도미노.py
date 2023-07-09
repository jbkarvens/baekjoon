import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def strongconnect(v):
    index[v]=index_num[0]
    lowlink[v]=index_num[0]
    index_num[0]+=1
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
    for _ in range(int(input())):
        n,m=map(int, input().split())
        adj=[[] for _ in range(n+1)]
        for _ in range(m):
            x,y=map(int, input().split())
            adj[x].append(y)
        stack=[]
        onstack=[False for _ in range(n+1)]
        index_num=[0]
        index=[None for _ in range(n+1)]
        lowlink=[None for _ in range(n+1)]
        scc=[]
        for node in range(1,n+1):
            if index[node]==None:
                strongconnect(node)
        
        myscc_index=[None for _ in range(n+1)]
        for i,component in enumerate(scc):
            for node in component:
                myscc_index[node]=i
        # scc의 각 파트들을 node로 하는 tree를 구성
        scc_adj=[set() for _ in range(len(scc))]
        for x in range(1,n+1):
            scc_x=myscc_index[x]
            for y in adj[x]:
                scc_y=myscc_index[y]
                if scc_x==scc_y:
                    continue
                if scc_y not in scc_adj[scc_x]:
                    scc_adj[scc_x].add(scc_y)
        end_node=[True for _ in range(len(scc))]
        for x in range(len(scc)):
            for y in scc_adj[x]:
                end_node[y]=False
        print(sum(end_node))