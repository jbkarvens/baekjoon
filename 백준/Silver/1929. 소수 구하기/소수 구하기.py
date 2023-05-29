def mySieve(num):
    primelst=[True for _ in range(num+1)]
    primelst[0]=False
    primelst[1]=False
    for i in range(2,num+1):
        if primelst[i]:
            j=2*i
            while j<=num:
                primelst[j]=False
                j+=i
    myprimes=[]
    for i in range(2,num+1):
        if primelst[i]:
            myprimes.append(i)
    return myprimes
M,N=map(int,input().split())
lst=mySieve(N)
for p in lst:
    if p>=M:
        print(p)