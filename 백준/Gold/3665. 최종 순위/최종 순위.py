import sys
input=sys.stdin.readline

if __name__=='__main__':
    for _ in range(int(input())):
        N = int(input())
        T = [*map(int, input().split())]
        adj = [set() for _ in range(N+1)]
        in_degree=[0 for _ in range(N+1)]
        for i in range(N):
            for j in range(i+1,N):
                adj[T[i]].add(T[j])
                in_degree[T[j]]+=1
        M = int(input())
        for _ in range(M):
            a,b=map(int,input().split())
            if a in adj[b]:
                a,b=b,a
            adj[b].add(a)
            adj[a].remove(b)
            in_degree[b]-=1
            in_degree[a]+=1
        
        result = []
        q = []
        for i in range(1,N+1):
            if in_degree[i]==0:
                q.append(i)
        fail = False
        while q:
            if len(q)>1:
                fail = True
                break
            node = q.pop()
            result.append(node)
            for vertex in adj[node]:
                in_degree[vertex]-=1
                if in_degree[vertex]==0:
                    q.append(vertex)
        if len(result)<N:
            fail = True
        if fail:
            print("IMPOSSIBLE")
        else:
            print(*result)