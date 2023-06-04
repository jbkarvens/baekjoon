import sys
input=sys.stdin.readline

DIRECTION=[(0,-1),(0,1),(1,0),(-1,0)]

N=int(input())
lst=[]
for _ in range(N):
    sen=input().rstrip()
    lst.append([])
    for i in range(N):
        lst[-1].append(int(sen[i]))

label=[[None for _ in range(N)] for _ in range(N)]
cout=[]
label_num=[0]

def dfs(x,y):
    if label[x][y]==None:
        label[x][y]=label_num[0]
        cout[label_num[0]]+=1
    for dx,dy in DIRECTION:
        u,v=x+dx,y+dy
        if not(0<=u<N and 0<=v<N) or lst[u][v]==0:
            continue
        if label[u][v]==None:
            dfs(u,v)

for num in range(N*N):
    x,y=num//N,num%N
    if lst[x][y] and label[x][y]==None:
        cout.append(0)
        dfs(x,y)
        label_num[0]+=1
cout.sort()
print(len(cout))
for c in cout:
    print(c)