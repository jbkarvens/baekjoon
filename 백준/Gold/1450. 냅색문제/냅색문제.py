import sys
input=sys.stdin.readline

N,C=map(int,input().split())
W=list(map(int,input().split()))

w1=W[:N//2]
w2=W[N//2:]

n1,n2=len(w1),len(w2)
w1sum=[0 for _ in range(2**n1)]
w2sum=[0 for _ in range(2**n2)]
m1,m2=2**n1,2**n2

k=1
for i in range(n1):
    for j in range(m1):
        if 0<=j%(2*k)<k:
            w1sum[j]+=w1[i]
    k*=2
w1sum.sort()
k=1
for i in range(n2):
    for j in range(m2):
        if 0<=j%(2*k)<k:
            w2sum[j]+=w2[i]
    k*=2
w2sum.sort()

ans=0
for i in range(m1):
    s,e=0,m2-1
    while s<=e:
        m=(s+e)//2
        if w1sum[i]+w2sum[m]<=C:
            s=m+1
        else:
            e=m-1
    ans+=(e+1)
print(ans)