def solve_sdk(d):
    if d==len(blank):
        return
    for v in range(1,9+1):
        x,y=blank[d]
        if check_sdk(x,y,v):
            sdk[x][y]=v
            solve_sdk(d+1)
            u,v=blank[-1]
            if sdk[u][v]!=0:
                return
            sdk[x][y]=0

def check_sdk(x,y,v):
    for i in range(9):
        if sdk[i][y]==v:
            return False
    for j in range(9):
        if sdk[x][j]==v:
            return False
    for i in range(3):
        for j in range(3):
            if sdk[x-x%3+i][y-y%3+j]==v:
                return False
    return True



sdk=[None for _ in range(9)]
for i in range(9):
    sdk[i]=list(map(int,input().split()))

blank=[(i,j) for i in range(9) for j in range(9) if sdk[i][j]==0]

solve_sdk(0)
for i in range(9):
    print(*sdk[i])