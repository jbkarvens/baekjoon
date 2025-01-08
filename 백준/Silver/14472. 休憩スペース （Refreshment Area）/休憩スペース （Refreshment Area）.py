import sys
input=sys.stdin.readline
N,M,D=map(int,input().split())
arr=[]
for i in range(N):
    arr.append(list(input().strip()))
cnt=0
for i in range(N-D+1):
    for j in range(M):
        if all([arr[i+k][j]=='.' for k in range(D)]):
            cnt+=1
for i in range(N):
    for j in range(M-D+1):
        if all([arr[i][j+k]=='.' for k in range(D)]):
            cnt+=1
print(cnt)