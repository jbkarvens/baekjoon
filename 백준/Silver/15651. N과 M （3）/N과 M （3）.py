def nCm(n,m,lst):
    if len(lst)==m:
        print(*lst)
    else:
        for i in range(1,n+1):
            lst.append(i)
            nCm(n,m,lst)
            lst.pop()

N,M=map(int,input().split())
lst=[]
nCm(N,M,lst)