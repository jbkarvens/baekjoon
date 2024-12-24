N=int(input())
arr=list(map(int,input().split()))
arr=[0]+arr
score=[[0 for _ in range(i)] for i in range(N+1)]
for i in range(2,N+1):
    for j in range(i):
        if j==i-1:
            score[i][j]=min([score[i-1][k]+abs(arr[i]-arr[k]) for k in range(1,i-1)]+[score[i-1][0]])
        else:
            score[i][j]=score[i-1][j]+abs(arr[i]-arr[i-1])
print(min(score[N]))