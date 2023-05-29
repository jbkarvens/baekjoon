N_up=1000000
lst=[True for _ in range(N_up+1)]
lst[0]=lst[1]=False
for i in range(2,N_up+1):
    if lst[i]:
        j=i+i
        while j<=N_up:
            lst[j]=False
            j+=i
plst=[]
for i in range(N_up+1):
    if lst[i]:
        plst.append(i)
pset=set(plst)
T=int(input())
for _ in range(T):
    N=int(input())
    cout=0
    for i in range(len(plst)):
        if plst[i]>N//2:
            break
        elif N-plst[i] in pset:
            cout+=1
    print(cout)