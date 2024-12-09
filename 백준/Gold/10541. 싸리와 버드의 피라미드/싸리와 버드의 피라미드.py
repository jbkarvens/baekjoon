import sys
input=sys.stdin.readline

N=int(input())
W=input().strip()
MOD=len(W)
psum=[[0 for _ in range(len(W))] for _ in range(26)]
for i,c in enumerate(W):
    for j in range(26):
        if i>0:
            psum[j][i]=psum[j][i-1]
    psum[ord(c)-ord('A')][i]+=1

for _ in range(int(input())):
    A,C=input().split()
    A=int(A)
    C=ord(C)-ord('A')
    res=0
    left=(A-1)*A//2
    right=A*(A+1)//2-1
    if left%MOD!=0:
        res-=psum[C][left%MOD-1]
    res+=psum[C][right%MOD]
    x=(A-right%MOD-(MOD+1-left%MOD))//MOD
    res+=psum[C][-1]*(x+1)
    print(res)
    