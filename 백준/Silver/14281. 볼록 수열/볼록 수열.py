import sys
N=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split()))
update=True
res=0
while update:
    update=False
    for i in range(N-2):
        if 2*arr[i+1]>arr[i]+arr[i+2]:
            x=(arr[i]+arr[i+2])//2
            res+=arr[i+1]-x
            arr[i+1]=x
            update=True
print(res)