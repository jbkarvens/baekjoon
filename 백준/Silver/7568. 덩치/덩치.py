N=int(input())
x=[]
for _ in range(N):
    x.append(list(map(int,input().split())))
rk=[None for _ in range(N)]
for i in range(N):
    cout=1
    for j in range(N):
        if i==j:
            continue
        if x[j][0]>x[i][0] and x[j][1]>x[i][1]:
            cout+=1
    rk[i]=cout
print(*rk)