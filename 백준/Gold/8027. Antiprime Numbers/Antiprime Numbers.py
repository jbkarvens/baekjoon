prime=[2,3,5,7,11,13,17,19,23,29]
N=2*10**9
def div(n):
    divs=dict()
    for p in prime:
        cnt=0
        while n%p==0:
            n//=p
            cnt+=1
        divs[p]=cnt
    res=1
    for p in divs:
        res*=divs[p]+1
    return res

chk=dict()
chk[1]=1
for p in prime:
    cur=set()
    for n in chk:
        n*=p
        while n<=N:
            cur.add(n)
            n*=p
    for n in cur:
        chk[n]=div(n)
chk=sorted(chk.items())
arr=[]
best=-1
for n,e in chk:
    if e>best:
        best=e
        arr.append(n)
n=int(input())
for m in reversed(arr):
    if m<=n:
        print(m)
        break