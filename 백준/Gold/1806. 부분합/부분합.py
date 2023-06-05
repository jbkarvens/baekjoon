import sys
input=sys.stdin.readline
       
N,S=map(int,input().split())
A=list(map(int,input().split()))
s,e=0,0
subsum=A[0]
ans=N+1
while True:
    if subsum<S:
        e+=1
        if e==N:
            break
        subsum+=A[e]
    else:
        ans=min(e-s+1,ans)
        if e>s:
            s+=1
            subsum-=A[s-1]
        else:
            e+=1
            if e==N:
                break
            subsum+=A[e]
print(0 if ans==N+1 else ans)