import sys
input=sys.stdin.readline
mod=998244353
n,t=map(int, input().split())
X=[]
for _ in range(n):
    X.append(int(input()))
ans,cur=1,t+1
for i in range(n)[::-1]:
    cur-=X[i]-1
    ans=(ans*cur)%mod
ans=(ans*(cur-n)*pow(cur,-1,mod))%mod
print(ans)