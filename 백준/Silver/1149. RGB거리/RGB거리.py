N=int(input())
min_cost=[0,0,0]
for _ in range(N):
    cost=list(map(int,input().split()))
    tmp=[v+1001 for v in min_cost]
    for i in range(3):
        for j in range(3):
            if i!=j and min_cost[i]+cost[j]<tmp[j]:
                tmp[j]=min_cost[i]+cost[j]
    for i in range(3):
        min_cost[i]=tmp[i]
print(min(min_cost))