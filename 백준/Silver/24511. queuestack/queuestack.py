import sys
import collections
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
M = int(input())
C = list(map(int,input().split()))

deq = collections.deque([B[i] for i in range(N) if A[i]==0])
res=[]
for c in C:
    deq.appendleft(c)
    res.append(deq.pop())
print(*res)