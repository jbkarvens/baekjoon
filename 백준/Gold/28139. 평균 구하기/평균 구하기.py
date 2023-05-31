N=int(input())
c=[list(map(int,input().split())) for _ in range(N)]
s=0
for i in range(N):
    for j in range(i+1,N):
        s+=((c[i][0]-c[j][0])**2+(c[i][1]-c[j][1])**2)**0.5
print(2*s/N)