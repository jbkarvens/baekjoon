import sys
input=sys.stdin.readline

def dfs(parity,u,N):
    if rec[0]>=bis[0]+min(sum(diagplus),sum(diagminus)):
        return
    for i in range(max(0,u-(N-1)),min(u,N-1)+1):
        j=u-i
        if not board[i][j] or not diagminus[i-j+N-1]:
            continue
        diagplus[u]=False
        diagminus[i-j+N-1]=False
        bis[0]+=1
        if u+2<2*N-1:
            dfs(parity,u+2,N)
        rec[0]=max(rec[0],bis[0])
        diagplus[u]=True
        diagminus[i-j+N-1]=True
        bis[0]-=1
    if u+2<2*N-1:
        dfs(parity,u+2,N)
    
N=int(input())
board=[]
for _ in range(N):
    board.append(list(map(int,input().split())))
ans=0

parity=0
diagplus=[False for _ in range(2*N-1)]
diagminus=[False for _ in range(2*N-1)]
bis=[0]
rec=[0]
for i in range(N):
    for j in range(N):
        if board[i][j] and (i+j)%2==parity:
            if not diagplus[i+j]:
                diagplus[i+j]=True
            if not diagminus[i-j+N-1]:
                diagminus[i-j+N-1]=True
dfs(parity,parity,N)
ans+=rec[0]

parity=1
diagplus=[False for _ in range(2*N-1)]
diagminus=[False for _ in range(2*N-1)]
bis=[0]
rec=[0]
for i in range(N):
    for j in range(N):
        if board[i][j] and (i+j)%2==parity:
            if not diagplus[i+j]:
                diagplus[i+j]=True
            if not diagminus[i-j+N-1]:
                diagminus[i-j+N-1]=True
dfs(parity,parity,N)
ans+=rec[0]

print(ans)