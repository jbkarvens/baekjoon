import sys
import collections
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
    begin=True
    t=int(input())
    for test in range(t):
        if not begin:
            _=input()
        else:
            begin=False
        n,m=map(int, input().split())
        adj=[[] for _ in range(n)]
        for _ in range(m):
            x,y=map(int, input().split())
            adj[x].append(y)
        stack=[]
        onstack=[False for _ in range(n)]
        index_num=[0]
        index=[None for _ in range(n)]
        lowlink=[None for _ in range(n)]
        scc=[]
        for node in range(n):
            if index[node]==None:
                strongconnect(node)
        
        myscc_index=[None for _ in range(n)]
        for i,component in enumerate(scc):
            for node in component:
                myscc_index[node]=i
        # scc의 각 파트들을 node로 하는 tree를 구성
        scc_adj=[set() for _ in range(len(scc))]
        for x in range(n):
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
        if sum(end_node)!=1:
            sys.stdout.write('Confused\n')
        else:
            start=end_node.index(True)
            visited=[False for _ in range(len(scc))]
            q=collections.deque([start])
            visited[start]=True
            while q:
                v=q.popleft()
                visited[v]=True
                for w in scc_adj[v]:
                    if visited[w]:
                        continue
                    q.append(w)
            if all(visited):
                scc[start].sort()
                for v in scc[start]:
                    sys.stdout.write(f'{v}\n')
            else:
                sys.stdout.write('Confused\n')
        if test!=t-1:
            sys.stdout.write('\n')