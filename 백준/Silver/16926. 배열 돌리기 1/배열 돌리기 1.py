import sys
from collections import deque
input=sys.stdin.readline

n,m,r = map(int,input().split())
A=[]
for _ in range(n):
    A.append(list(map(int,input().split())))
B=[[None for _ in range(m)] for _ in range(n)]
for k in range(min(n,m)//2):
    deq = deque()
    for i in range(k,n-k-1):
        deq.append(A[i][k])
    for i in range(k,m-k-1):
        deq.append(A[n-k-1][i])
    for i in reversed(range(k+1,n-k)):
        deq.append(A[i][m-k-1])
    for i in reversed(range(k+1,m-k)):
        deq.append(A[k][i])
    deq.rotate(r)
    cnt = 0
    for i in range(k,n-k-1):
        B[i][k]=deq[cnt]
        cnt+=1
    for i in range(k,m-k-1):
        B[n-k-1][i]=deq[cnt]
        cnt+=1
    for i in reversed(range(k+1,n-k)):
        B[i][m-k-1]=deq[cnt]
        cnt+=1
    for i in reversed(range(k+1,m-k)):
        B[k][i]=deq[cnt]
        cnt+=1
for i in range(n):
    print(*B[i])