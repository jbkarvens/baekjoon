import sys
input=sys.stdin.readline

N=int(input())
W=int(input())
coor=[None]
for _ in range(W):
    coor.append(list(map(int,input().split())))

rec1=[None for _ in range(W+1)]
rec2=[None for _ in range(W+1)]
dp1=[0 for _ in range(W+1)]
dp2=[0 for _ in range(W+1)]
dp1[1]=abs(1-coor[1][0])+abs(1-coor[1][1])
dp2[1]=abs(N-coor[1][0])+abs(N-coor[1][1])

subsum=[0 for _ in range(W+1)]
for i in range(2,W+1):
    subsum[i]=subsum[i-1]+(abs(coor[i][0]-coor[i-1][0])+abs(coor[i][1]-coor[i-1][1]))

for k in range(2,W+1):
    for i in range(k-1):
        if i==0:
            # dp(0,k-1)
            dp1[k]=dp2[1]+subsum[k-1]-subsum[1]+coor[k][0]-1+coor[k][1]-1
            rec1[k]=0
            #dp(k-1,0)
            dp2[k]=dp1[1]+subsum[k-1]-subsum[1]+abs(coor[k][0]-N)+abs(coor[k][1]-N)
            rec2[k]=0
        else:
            # dp(i,k-1)
            ti1=dp2[i+1]+subsum[k-1]-subsum[i+1]+abs(coor[i][0]-coor[k][0])+abs(coor[i][1]-coor[k][1])
            # dp(k-1,i)
            ti2=dp1[i+1]+subsum[k-1]-subsum[i+1]+abs(coor[i][0]-coor[k][0])+abs(coor[i][1]-coor[k][1])
            if ti1<dp1[k]:
                rec1[k]=i
                dp1[k]=ti1
            if ti2<dp2[k]:
                rec2[k]=i
                dp2[k]=ti2

ans=10**10
idx=None
isone=False

for k in range(W):
    # dp(k,W)
    t2=dp2[k+1]+subsum[W]-subsum[k+1]
    # dp(W,k)
    t1=dp1[k+1]+subsum[W]-subsum[k+1]
    if ans>t2:
        ans=t2
        idx=k
        isone=False
    if ans>t1:
        isone=True
        ans=t1
        idx=k

rec=[]
k=W
while True:
    if idx==0:
        if isone:
            for i in range(k):
                rec+=[1]
        else:
            for i in range(k):
                rec+=[2]
        break
    if isone:
        for i in range(k-idx):
            rec+=[1]
        k=idx
        isone=False
        idx=rec1[idx+1]
    else:
        for i in range(k-idx):
            rec+=[2]
        k=idx
        isone=True
        idx=rec2[idx+1]
        
print(ans)
for i in reversed(range(W)):
    print(rec[i])