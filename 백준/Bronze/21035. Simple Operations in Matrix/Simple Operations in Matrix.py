import sys
input=sys.stdin.readline

N,M=map(int,input().split())
A=[]
for _ in range(N):
    A.append(list(map(int,input().split())))
for _ in range(int(input())):
    flag,i,k=input().split()
    i=int(i)-1
    k=int(k)
    if flag=='row':
        for j in range(M):
            A[i][j]+=k
    elif flag=='col':
        for j in range(N):
            A[j][i]+=k
s1=sum([sum(A[i]) for i in range(N)])
s2=min([min(A[i]) for i in range(N)])
s3=max([max(A[i]) for i in range(N)])
print(s1,s2,s3)