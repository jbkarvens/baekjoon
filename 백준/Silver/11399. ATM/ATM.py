N=int(input())
P=list(map(int,input().split()))
P.sort()
ans=0
for i in range(N):
    ans+=(N-i)*P[i]
print(ans)