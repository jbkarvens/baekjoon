for _ in range(int(input())):
    N,M=map(int,input().split())
    value=list(map(int,input().split()))
    lst=list(range(N))
    result=[]
    start,end=0,N-1
    while start<=end:
        if value[start]==max(value[start:end+1]):
            result.append(lst[start])
            start+=1
        else:
            value.append(value[start])
            lst.append(lst[start])
            start+=1
            end+=1
    print(result.index(M)+1)