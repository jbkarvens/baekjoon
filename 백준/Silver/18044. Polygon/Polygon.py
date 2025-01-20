import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    lsum=sum(arr)-arr[-1]
    i=1
    while lsum>0 and lsum<=arr[-i]:
        lsum-=arr[-i-1]
        i+=1
    if lsum==0:
        print(lsum)
    else:
        print(lsum+arr[-i])