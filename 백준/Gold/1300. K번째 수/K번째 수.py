def f(x,N):
    s=0
    for i in range(1,min(x,N)+1):
        s+=min(N,x//i)
    return s
def bin_search(K,N):
    low,high=1,N*N
    while low<=high:
        mid=(low+high)//2
        if f(mid,N)<K:
            low=mid+1
        else:
            high=mid-1
    return high

N=int(input())
K=int(input())
print(bin_search(K,N)+1)