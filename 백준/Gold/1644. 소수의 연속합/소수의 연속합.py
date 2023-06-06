import sys
input=sys.stdin.readline

def psieve(n):
    n=max(100,n)
    plst=[True for _ in range(n+1)]
    pset=[2]
    for j in range(4,n+1,2):
        plst[j]=False
    for i in range(3,n+1,2):
        if not plst[i]:
            continue
        pset.append(i)
        for j in range(2*i,n+1,i):
            plst[j]=False
    return pset

N=int(input())
P=psieve(N)
s,e=0,0
subsum=P[0]
ans=0
while True:
    if subsum<N:
        e+=1
        if e==len(P):
            break
        subsum+=P[e]
    else:
        if subsum==N:
            ans+=1
        subsum-=P[s]
        s+=1
print(ans)