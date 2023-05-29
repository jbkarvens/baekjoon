def psieve(n):
    lst=[True for _ in range(n+1)]
    lst[0]=lst[1]=False
    for i in range(2,n+1):
        if lst[i]:
            j=i+i
            while j<=n:
                lst[j]=False
                j+=i
    plst=[]
    for i in range(n+1):
        if lst[i]:
            plst.append(i)
    return plst
while True:
    n=int(input())
    if n!=0:
        print(len(psieve(2*n))-len(psieve(n)))
    elif n==0:
        break