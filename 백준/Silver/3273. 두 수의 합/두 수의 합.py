import sys
input=sys.stdin.readline
       
N=int(input())
A=list(map(int,input().split()))
x=int(input())
s,e=0,N-1
ans=0
A.sort()
while s<e:
    if A[s]+A[e]>x:
        e-=1
    else:
        if A[s]+A[e]==x:
            ans+=1
        s+=1
print(ans)