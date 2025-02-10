N,B=map(int,input().split())
prime=dict()
bb=B
for i in range(2,30):
    if bb%i==0:
        prime[i]=0
        while bb%i==0:
            bb//=i
            prime[i]+=1
pexp=dict()
for p in prime:
    nn=N
    pexp[p]=0
    while nn:
        nn//=p
        pexp[p]+=nn
rem=1
for i in range(1,N+1):
    for p in prime:
        while i%p==0:
            i//=p
    rem=(rem*i)%B
emin=min([pexp[p]//prime[p] for p in pexp])
for p in prime:
    rem=(rem*pow(p,pexp[p]-prime[p]*emin,B))%B
print(rem)
