N,C=map(int,input().split())
X=[int(input()) for _ in range(N)]
X.sort()
low,high=0,X[-1]-X[0]
while low<=high:
    mid=(low+high)//2
    cout=1
    cur=0
    for i in range(N):
        if X[i]-X[cur]>=mid:
            cout+=1
            cur=i
        if cout>=C:
            break
    if cout>=C:
        low=mid+1
    else:
        high=mid-1
print(high)