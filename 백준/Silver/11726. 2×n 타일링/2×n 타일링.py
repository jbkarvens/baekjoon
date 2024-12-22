n=int(input())
arr=[None,1,2]
mod=10007
while len(arr)<=n:
    arr.append((arr[-1]+arr[-2])%mod)
print(arr[n])