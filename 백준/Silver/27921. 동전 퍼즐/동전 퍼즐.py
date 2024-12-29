import sys
input=sys.stdin.readline

h1,w1=map(int,input().split())
arr1=[]
for _ in range(h1):
    arr1.append(list(input().strip()))
for i in range(h1):
    for j in range(w1):
        if arr1[i][j]=='O':
            arr1[i][j]=True
        elif arr1[i][j]=='.':
            arr1[i][j]=False

h2,w2=map(int,input().split())
arr2=[]
for _ in range(h2):
    arr2.append(list(input().strip()))
for i in range(h2):
    for j in range(w2):
        if arr2[i][j]=='O':
            arr2[i][j]=True
        elif arr2[i][j]=='.':
            arr2[i][j]=False

high=-1
for u in range(h1+h2):
    for v in range(w1+w2):
        cnt=0
        for i in range(h1):
            for j in range(w1):
                x=i-h1+u
                y=j-w1+v
                if not(0<=x<h2) or not(0<=y<w2):
                    continue
                if arr1[i][j] and arr2[x][y]:
                    cnt+=1
        high=max(high,cnt)
print(sum([sum(arr1[i]) for i in range(h1)])-high)