N=int(input())
ans,k=0,5
while k<=N:
    ans+=N//k
    k*=5
print(ans)