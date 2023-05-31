dp=[0,1,2,4]
for _ in range(int(input())):
    n=int(input())
    if len(dp)<=n:
        for i in range(len(dp),n+1):
            dp.append(sum(dp[i-3:i]))
    print(dp[n])