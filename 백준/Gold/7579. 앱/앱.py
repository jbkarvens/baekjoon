MAX_C=100
N,M=map(int,input().split())
mi=list(map(int,input().split()))
ci=list(map(int,input().split()))
# dp[t] = cost가 t이하면서 얻을 수 있는 최대 메모리값
dp=[0 for _ in range(N*MAX_C+1)]
for i in range(N):
    tmp=dp[:]
    for j in range(len(dp)):
        if ci[i]<=j:
            tmp[j]=max(dp[j],mi[i]+dp[j-ci[i]])
    dp=tmp

ans=0
while True:
    if dp[ans]>=M:
        break
    ans+=1
print(ans)