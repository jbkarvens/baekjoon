import sys
import collections
import random
input=sys.stdin.readline

if __name__=='__main__':
    n=int(input())
    adj=[dict() for _ in range(n+1)]
    for _ in range(n-1):
        a,b,c=map(int,input().split())
        adj[a][b]=c
        adj[b][a]=c
    root = random.randint(1,n)
    logn=17
    parent=[[None for _ in range(n+1)] for _ in range(logn)]
    distmax=[[None for _ in range(n+1)] for _ in range(logn)]
    distmin=[[None for _ in range(n+1)] for _ in range(logn)]
    queue=collections.deque([root])
    parent[0][root]=root
    distmax[0][root]=distmin[0][root]=0
    while queue:
        node=queue.popleft()
        for v in adj[node]:
            if parent[0][node]==v:
                continue
            parent[0][v]=node
            distmax[0][v]=adj[v][node]
            distmin[0][v]=adj[v][node]
            queue.append(v)
    for i in range(1,logn):
        for v in range(1,n+1):
            w=parent[i-1][v]
            parent[i][v]=parent[i-1][w]
            distmax[i][v]=max(distmax[i-1][v],distmax[i-1][w])
            distmin[i][v]=min(distmin[i-1][v],distmin[i-1][w])
    for _ in range(int(input())):
        d,e=map(int,input().split())
        depth_d,depth_e=0,0
        dd,ee=d,e
        for i in reversed(range(logn)):
            d_temp=parent[i][dd]
            e_temp=parent[i][ee]
            if d_temp!=root:
                dd=d_temp
                depth_d+=1<<i
            if e_temp!=root:
                ee=e_temp
                depth_e+=1<<i
        if dd!=root:
            depth_d+=1
        if ee!=root:
            depth_e+=1
        dmax,dmin=-1,10**7
        if depth_d<depth_e:
            d,e=e,d
            depth_d,depth_e=depth_e,depth_d
        s=depth_d-depth_e
        for i in range(logn):
            if s&(1<<i):
                dmax=max(dmax,distmax[i][d])
                dmin=min(dmin,distmin[i][d])
                d=parent[i][d]
        for i in reversed(range(logn)):
            dd=parent[i][d]
            ee=parent[i][e]
            if dd!=ee:
                dmax=max(dmax,distmax[i][d],distmax[i][e])
                dmin=min(dmin,distmin[i][d],distmin[i][e])
                d=dd
                e=ee
        if d!=e:
            dmax=max(dmax,distmax[0][d],distmax[0][e])
            dmin=min(dmin,distmin[0][d],distmin[0][e])
        sys.stdout.write(f'{dmin} {dmax}\n')
                