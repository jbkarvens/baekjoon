def f(lst,h):
    a=0
    for v in lst:
        a+=max(v-h,0)
    return a

N,M=map(int,input().split())
lst=list(map(int,input().split()))
low,high=0,10**9
while high-low>1:
    mid=(high+low)//2
    if f(lst,mid)>=M:
        low=mid
    else:
        high=mid
print(low)