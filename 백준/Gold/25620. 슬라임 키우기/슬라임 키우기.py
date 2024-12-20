import sys
input=sys.stdin.readline
N,Q=map(int,input().split())
A=list(map(int,input().split()))
LIMIT=10**9
X=[]
Y=[]
for i in range(Q):
    x,y=map(int, input().split())
    X.append(x)
    Y.append(y)
test=list(range(N))
for i in range(Q):
    ntest=[]
    if X[i]==0:
        continue
    if Y[i]==0:
        for j in test:
            if A[j]<=X[i]:
                A[j]=0
            else:
                ntest.append(j)
        test=ntest
        continue
    if Y[i]==1:
        continue
    for j in test:
        if A[j]<=X[i]:
            num=A[j]*Y[i]
            A[j]=num
            if num<=LIMIT:
                ntest.append(j)
        else:
            ntest.append(j)
    test=ntest
A.sort()
print(*A)