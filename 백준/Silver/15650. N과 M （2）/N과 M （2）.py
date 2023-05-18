def nCm(n,m,lst):
    if len(lst)==m:
        print(*lst)
    else:
        start=0
        if len(lst)>0:
            start=lst[-1]
        for i in range(start+1,n+1):
            if not i in lst:
                lst.append(i)
                nCm(n,m,lst)
                lst.pop()
N,M=map(int,input().split())
lst=[]
nCm(N,M,lst)