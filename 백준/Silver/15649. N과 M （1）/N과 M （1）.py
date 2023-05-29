def nPm(n,m,lst):
    if len(lst)==m:
        print(*lst)
    else:
        for i in range(1,n+1):
            if not i in lst:
                lst.append(i)
                nPm(n,m,lst)
                lst.pop()
N,M=map(int,input().split())
lst=[]
nPm(N,M,lst)