import sys
input=sys.stdin.readline

def find(x):
    if x==root[x]:
        return x
    root[x]=find(root[x])
    return root[x]
def union(x,y):
    rx=find(x)
    ry=find(y)
    if rx==ry:
        return
    else:
        root[rx]=ry
        return
def connected():
    global M,N
    for i in range(M):
        for j in range(N):
            if arr[i][j]==0:
                continue
            for di,dj in [(0,-1),(0,1),(-1,0),(1,0)]:
                ni=i+di
                nj=j+dj
                if ni<0 or ni>=M or nj<0 or nj>=N:
                    continue
                if arr[ni][nj]==0:
                    continue
                union(N*i+j,N*ni+nj)
    cur=None
    for i in range(M*N):
        if not arr[i//N][i%N]:
            continue
        if cur==None:
            cur=find(i)
            continue
        if cur!=find(i):
            return False
    return True
def showarr():
    global M,N
    for i in range(M):
        print(*arr[i],sep='')
    print()

M,N=map(int,input().split())
arr=[]
for _ in range(M):
    arr.append(list(input().strip()))
for i in range(M):
    for j in range(N):
        arr[i][j]=int(arr[i][j])
root=[i for i in range(M*N)]
cnt=0
while not connected():
    tmp=[[0 for _ in range(N)] for _ in range(M)]
    for i in range(M):
        for j in range(N):
            c=arr[i][j]
            tmp[i][j]=max(tmp[i][j],arr[i][j])
            if c==0:
                continue
            for di in range(-c,c+1):
                for dj in range(-c,c+1):
                    ni=i+di
                    nj=j+dj
                    if ni<0 or ni>=M or nj<0 or nj>=N:
                        continue
                    if arr[ni][nj]<arr[i][j]:
                        tmp[ni][nj]=max(tmp[ni][nj],c)
    for i in range(M):
        for j in range(N):
            arr[i][j]=tmp[i][j]
    cnt+=1
print(cnt)