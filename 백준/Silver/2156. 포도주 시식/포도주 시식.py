import sys
# input=sys.stdin.readline
n=int(input())
val=[]
for _ in range(n):
    val.append(int(input()))
# dp[k-1][j]: 1~k번째까지의 잔만 있었을 때 오른쪽 연속 j개를 고른 경우 최댓값
dp=[[0,val[0],0]]
if n>1:
    dp.append([val[0],val[1],val[0]+val[1]])
for i in range(2,n):
    dp.append([max(dp[i-1]),dp[i-1][0]+val[i],dp[i-1][1]+val[i]])
print(max(dp[n-1]))