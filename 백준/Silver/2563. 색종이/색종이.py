paper=[[False for _ in range(100)] for _ in range(100)]
N=int(input())
for _ in range(N):
    x,y=map(int,input().split())
    for i in range(10):
        for j in range(10):
            if not paper[x+i][y+j]:
                paper[x+i][y+j]=True
print(sum([sum(l) for l in paper]))