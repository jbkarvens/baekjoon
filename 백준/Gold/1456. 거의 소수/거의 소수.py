A,B=map(int,input().split())
N=int(B**0.5)
plst=[True for _ in range(N+1)]
plst[0],plst[1]=False,False
for i in range(4,N+1,2):
    plst[i]=False
for i in range(3,N+1,2):
    if plst[i]:
        j=i+i
        while j<=N:
            plst[j]=False
            j+=i

count=0
for p,isprime in enumerate(plst):
    if isprime:
        tmp=p*p
        while tmp<=B:
            if tmp<A:
                tmp*=p
                continue
            count+=1
            tmp*=p
print(count)