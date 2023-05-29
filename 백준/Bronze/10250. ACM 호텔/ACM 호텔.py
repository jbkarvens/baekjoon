import sys
# input=sys.stdin.readline
for _ in range(int(input())):
    h,w,n=map(int,input().split())
    y=str(1+(n-1)%h)
    x=str(1+(n-1)//h)
    if len(x)<2:
        x='0'+x
    print(y+x)