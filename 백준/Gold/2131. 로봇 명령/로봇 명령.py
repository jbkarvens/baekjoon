import sys
input=sys.stdin.readline
x,y,d=0,0,0
dxy=[(1,0),(0,1),(-1,0),(0,-1)]
scanarr=[]
# 오:0 위:1 왼:2 아래:3
for _ in range(int(input())):
    inst=input().strip()
    if inst=='Forward':
        x+=dxy[d][0]
        y+=dxy[d][1]
    elif inst=='Turn Left':
        d=(d+1)%4
    elif inst=='Turn Right':
        d=(d-1)%4
    elif inst=='Scan':
        sx=x+dxy[d][0]
        sy=y+dxy[d][1]
        scanarr.append((sx,sy))

def dist(x0,y0,x1,y1):
    dx=x0-x1
    dy=y0-y1
    if dx==0 and dy==0:
        return 1
    elif dx==0 or dy==0:
        return 2
    else:
        return 3

# dp[i][d]:i번째 d방향 scan
M=len(scanarr)
dp=[[10**10 for _ in range(4)] for _ in range(M)]
for d in range(4):
    dp[M-1][d]=1
for i in reversed(range(M-1)):
    for d1 in range(4):
        x0=scanarr[i][0]+dxy[d1][0]
        y0=scanarr[i][1]+dxy[d1][1]
        for d2 in range(4):
            x1=scanarr[i+1][0]+dxy[d2][0]
            y1=scanarr[i+1][1]+dxy[d2][1]
            dp[i][d1]=min(dp[i][d1],dp[i+1][d2]+dist(x0,y0,x1,y1))
ans=10**10
for d in range(4):
    ans=min(ans,dp[0][d]+dist(0,0,scanarr[0][0]+dxy[d][0],scanarr[0][1]+dxy[d][1])-1)
print(ans)