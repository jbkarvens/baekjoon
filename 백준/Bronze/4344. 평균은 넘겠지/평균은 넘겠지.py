for _ in range(int(input())):
    tmplst=list(map(int,input().split()))
    N,lst=tmplst[0],tmplst[1:]
    avg=sum(lst)/N
    count=0
    print('{0:.3f}%'.format(100*sum([1 if e>avg else 0 for e in lst])/N))