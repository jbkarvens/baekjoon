T=int(input())
n=int(input())
A=list(map(int,input().split()))
m=int(input())
B=list(map(int,input().split()))
subA=dict()
subB=dict()
for i in range(n):
    x=0
    for j in range(n-i):
        x+=A[i+j]
        if x in subA:
            subA[x]+=1
        else:
            subA[x]=1
for i in range(m):
    x=0
    for j in range(m-i):
        x+=B[i+j]
        if x in subB:
            subB[x]+=1
        else:
            subB[x]=1
res=0
for x in subA:
    if T-x in subB:
        res+=subA[x]*subB[T-x]
print(res)