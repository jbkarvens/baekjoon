def dfs(n,m,lst):
    if len(lst)==m:
        print(*lst)
    else:
        start=1
        if len(lst)>0:
            start=lst[-1]
        for i in range(start,n+1):
            lst.append(i)
            dfs(n,m,lst)
            lst.pop()

N,M=map(int,input().split())
lst=[]
dfs(N,M,lst)