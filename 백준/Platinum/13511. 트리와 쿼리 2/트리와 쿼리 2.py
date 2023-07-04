import sys
import collections
import random
# sys.stdin=open(r'C:\Users\karve\Desktop\test.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    adj=[dict() for _ in range(n+1)]
    for _ in range(n-1):
        u,v,w=map(int,input().split())
        adj[u][v]=w
        adj[v][u]=w
    logn=18
    parent=[[None for _ in range(n+1)] for _ in range(logn)]
    dist=[[None for _ in range(n+1)] for _ in range(logn)]
    root=random.randint(1,n)
    # print(root)
    queue=collections.deque([root])
    parent[0][root],dist[0][root]=root,0
    while queue:
        node = queue.popleft()
        for v in adj[node]:
            if parent[0][node]==v:
                continue
            parent[0][v]=node
            dist[0][v]=adj[node][v]
            queue.append(v)
    for i in range(1,logn):
        for v in range(1,n+1):
            w=parent[i-1][v]
            parent[i][v]=parent[i-1][w]
            dist[i][v]=dist[i-1][v]+dist[i-1][w]
    for _ in range(int(input())):
        query=[*map(int, input().split())]
        if query[0]==1:
            u,v=query[1:]
        elif query[0]==2:
            u,v,k=query[1:]
            k-=1
        depth_u=depth_v=0
        uu,vv=u,v
        for i in reversed(range(logn)):
            temp_u=parent[i][uu]
            if temp_u!=root:
                uu=temp_u
                depth_u+=1<<i
            temp_v=parent[i][vv]
            if temp_v!=root:
                vv=temp_v
                depth_v+=1<<i
        if uu!=root:
            depth_u+=1
        if vv!=root:
            depth_v+=1
        
        if query[0]==1:
            if depth_v>depth_u:
                u,v=v,u
                depth_u,depth_v=depth_v,depth_u
            s=depth_u-depth_v
            result=0
            for i in range(logn):
                if s&(1<<i):
                    result+=dist[i][u]
                    u=parent[i][u]
            for i in reversed(range(logn)):
                uu,vv=parent[i][u],parent[i][v]
                if uu!=vv:
                    result+=dist[i][u]+dist[i][v]
                    u,v=uu,vv
            if u!=v:
                result+=dist[0][u]+dist[0][v]
        elif query[0]==2:
            chk=False
            uu,vv=u,v
            if depth_v>depth_u:
                s=depth_v-depth_u
                ddepth_u,ddepth_v=depth_v,depth_u
                uu,vv=vv,uu
                chk=True
            else:
                ddepth_u,ddepth_v=depth_u,depth_v
                s=depth_u-depth_v
            for i in range(logn):
                if s&(1<<i):
                    uu=parent[i][uu]
            depth=0
            for i in reversed(range(logn)):
                temp_u=parent[i][uu]
                temp_v=parent[i][vv]
                if temp_u!=temp_v:
                    uu,vv=temp_u,temp_v
                    depth+=1<<i
            if uu!=vv:
                depth+=1
            d_u=ddepth_u-(min(ddepth_u,ddepth_v)-depth)
            d_v=ddepth_v-(min(ddepth_u,ddepth_v)-depth)
            # print(depth_u,depth_v,d_u,d_v,depth)
            if chk:
                d_u,d_v=d_v,d_u
            if k<d_u:
                result=u
            else:
                k=d_u+d_v-k
                result=v
            for i in range(logn):
                if k&(1<<i):
                    result=parent[i][result]
        sys.stdout.write(f'{result}\n')