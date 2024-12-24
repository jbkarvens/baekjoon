N=int(input())
a=[0]+list(map(int,input().split()))
s=[[0]*i for i in range(N+1)]
for i in range(2,N+1):
    for j in range(i-1):
        s[i][j]=s[i-1][j]+abs(a[i]-a[i-1])
    s[i][i-1]=min([s[i-1][k]+abs(a[i]-a[k]) for k in range(1,i-1)]+[s[i-1][0]])
print(min(s[N]))