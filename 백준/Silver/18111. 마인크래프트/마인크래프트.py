H=257
N,M,B=map(int,input().split())
lv=[0 for _ in range(H)]
for _ in range(N):
    lst=list(map(int,input().split()))
    for i in range(H):
        lv[i]+=lst.count(i)
tlst=[None for _ in range(H)]
for i in range(H):
    low,high=0,0
    for j in range(i):
        low+=lv[j]*(i-j)
    for j in range(i+1,H):
        high+=lv[j]*(j-i)
    if low<=B+high:
        tlst[i]=low+high*2
t,ht=None,None
for i in range(H):
    if tlst[i]!=None:
        if t==None:
            t,ht=tlst[i],i
        else:
            if t>=tlst[i]:
                t,ht=tlst[i],i
print(t,ht)