N=int(input())
road=list(map(int,input().split()))
price=list(map(int,input().split()))
ans,i=0,0
while i<N-1:
    road_len=road[i]
    p_now=price[i]
    i+=1
    while i<N-1 and price[i]>p_now:
        road_len+=road[i]
        i+=1
    ans+=road_len*p_now
print(ans)