import sys
input=sys.stdin.readline

def f(lst,v):
    x=0
    for a in lst:
        x+=a//v
    return x

K,N=map(int,input().split())
lst=[]
for _ in range(K):
    lst.append(int(input().rstrip()))
low,high=1,2**32
while high-low>1:
    mid=(low+high)//2
    if f(lst,mid)>=N:
        low=mid
    else:
        high=mid
print(low)