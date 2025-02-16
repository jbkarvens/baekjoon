w,n=map(int,input().split())
A=list(map(int, input().split()))
A.sort()
subA=[0]*(w+1)
for i in range(n):
    for j in range(i+1,n):
        x=A[i]+A[j]
        if w<x:
            continue
        subA[x]=(i,j)
suc=False
for i in range(n):
    for j in range(i+1,n):
        x=A[i]+A[j]
        if x<=w and subA[w-x] and not i in subA[w-x] and not j in subA[w-x]:
            suc=True
            break
    if suc:
        break
if suc:
    print('YES')
else:
    print('NO')