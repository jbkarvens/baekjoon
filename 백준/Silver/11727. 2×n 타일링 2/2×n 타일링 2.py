n=int(input())
arr=[None,1,3]
while len(arr)<=n:
    arr.append((arr[-1]+2*arr[-2])%10007)
print(arr[n])