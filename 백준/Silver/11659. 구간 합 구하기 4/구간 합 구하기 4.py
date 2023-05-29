import sys
input=sys.stdin.readline
N,M=map(int,input().split())
A=list(map(int,input().split()))
B=[0 for _ in range(N+1)]
for i in range(1,N+1):
    B[i]=B[i-1]+A[i-1]
for _ in range(M):
    i,j=map(int,input().split())
    print(B[j]-B[i-1])