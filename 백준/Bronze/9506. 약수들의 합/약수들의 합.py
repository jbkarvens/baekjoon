while True:
    N=int(input())
    if N==-1:
        break
    i=1
    lst,frontlst,backlst=[],[],[]
    while i*i<=N:
        if N%i==0:
            frontlst.append(i)
        i+=1
    for e in frontlst:
        backlst.append(N//e)
    if frontlst[-1]==backlst[-1]:
        backlst=backlst[-2::-1]
    else:
        backlst=backlst[::-1]
    lst=frontlst+backlst
    if sum(lst)!=2*N:
        print('{0} is NOT perfect.'.format(N))
    else:
        sen=str(N)+' = 1'
        for d in lst:
            if 1<d<N:
                sen=sen+' + '+str(d)
        print(sen)