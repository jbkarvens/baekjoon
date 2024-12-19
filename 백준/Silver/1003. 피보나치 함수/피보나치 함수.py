import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N=int(input())
    x0,y0=1,0
    x1,y1=0,1
    for _ in range(N):
        x0,x1=x1,x0+x1
        y0,y1=y1,y0+y1
    print(x0,y0)