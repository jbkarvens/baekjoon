import sys
input=sys.stdin.readline

def isbingo():
    res=0
    for i in range(size):
        if all([checkboard[i][j] for j in range(size)]):
            res+=1
        if all([checkboard[j][i] for j in range(size)]):
            res+=1
    if all([checkboard[i][i] for i in range(size)]):
        res+=1
    if all([checkboard[i][size-i-1] for i in range(size)]):
        res+=1
    return True if res>=3 else False


bingo=[]
seq=[]
size=5
for _ in range(size):
    bingo.append(list(map(int,input().split())))
for _ in range(size):
    seq+=list(map(int,input().split()))
cnt=0
checkboard=[[False for _ in range(size)] for _ in range(size)]

while not isbingo():
    pos=0
    for i in range(size*size):
        if seq[cnt]==bingo[i//5][i%5]:
            pos=i
            break
    checkboard[pos//5][pos%5]=True
    cnt+=1
print(cnt)
