N,M=map(int,input().split())
lst=list(map(int,input().split()))
low,high=0,2*10**9
while low<=high:
    mid=(high+low)//2
    a=0
    for v in lst:
        if v>mid:
            a+=v-mid
    if a>=M:
        low=mid+1
    else:
        high=mid-1
print(high)