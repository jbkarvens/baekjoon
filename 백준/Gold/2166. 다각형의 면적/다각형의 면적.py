import sys
input=sys.stdin.readline
N,C=int(input()),[]
for _ in range(N):
    C.append(list(map(int,input().split())))
S=0
for i in range(1,N-1):
    x2,y2=C[i+1][0]-C[0][0],C[i+1][1]-C[0][1]
    x1,y1=C[i][0]-C[0][0],C[i][1]-C[0][1]
    S+=(x1*y2-x2*y1)/2
print(round(abs(S),1))