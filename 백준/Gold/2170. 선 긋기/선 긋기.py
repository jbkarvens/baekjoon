import sys
input=sys.stdin.readline
arr=[]
for _ in range(int(input())):
    x,y=map(int, input().split())
    arr.append([x,y])
arr.sort()
res=0
M=10**10
s,e=-M,-M
for x,y in arr:
    if e<x:
        res+=e-s
        s,e=x,y
    else:
        e=max(e,y)
res+=e-s
sys.stdout.write(f'{res}')