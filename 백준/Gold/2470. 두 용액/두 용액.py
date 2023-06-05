import sys
input=sys.stdin.readline
       
N=int(input())
A=list(map(int,input().split()))
A.sort()
s,e=0,N-1
rec=10**9*3
while s<e:
    if rec>abs(A[s]+A[e]):
        ans=(A[s],A[e])
        rec=abs(A[s]+A[e])
    if A[s]+A[e]>0:
        e-=1
    else:
        s+=1
print(*ans)