def find(x):
    if root[x]==x:
        return x
    root[x]=find(root[x])
    return root[x]
def union(x,y):
    rx=find(x)
    ry=find(y)
    if rx!=ry:
        root[ry]=rx

for _ in range(int(input())):
    N=int(input())
    board=[]
    root=[i for i in range(N*N)]
    for _ in range(N):
        board.append(list(input().strip()))
    # i,j : (i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j)
    for i in range(N):
        for j in range(N):
            if board[i][j]=='.':
                continue
            for di,dj in [(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0)]:
                ni=i+di
                nj=j+dj
                if ni<0 or ni>=N or nj<0 or nj>=N:
                    continue
                if board[i][j]==board[ni][nj]:
                    union(i*N+j,ni*N+nj)
    # not fin:0 black:1 white:2
    res=0
    for i in range(N):
        for j in range(N):
            if find(i)==find(N*(N-1)+j) and board[0][i]=='B':
                res=1
                break
            elif find(N*i)==find(N*j+N-1) and board[i][0]=='W':
                res=2
                break
        if res:
            break
    if res==1:
        print("Black wins")
    elif res==2:
        print("White wins")
    else:
        print("Not finished")
                