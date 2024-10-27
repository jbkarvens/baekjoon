import sys
input = sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))
B,C=map(int,input().split())
res=0
for a in A:
    if a<=B:
        res+=1
    else:
        res+=-((-a+B)//C) + 1
print(res)