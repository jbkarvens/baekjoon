import sys
input=sys.stdin.readline
N=int(input())
ep=10**(-10)
op=[]
for _ in range(N):
    op.append(int(input()))
op.sort()
m=round(N*0.15+ep)
if N==0:
    print(0)
else:
    if m!=0:
        op=op[m:-m]
    print(round(sum(op)/len(op)+ep))