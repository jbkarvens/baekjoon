import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    x,y=[],[]
    for i in range(N):
        xi,yi=map(int,input().split())
        x.append(xi)
        y.append(yi)
    for i in range(N):
        print(i+1,x[i]+10,y[i]+500000000)