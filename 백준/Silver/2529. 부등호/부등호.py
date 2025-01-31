import sys
input=sys.stdin.readline
import itertools
k=int(input())
arr=list(input().split())
for i in range(k):
    if arr[i]=='<':
        arr[i]=True
    else:
        arr[i]=False
high=0
low=10**10
for seq in itertools.permutations([0,1,2,3,4,5,6,7,8,9],k+1):
    suc=True
    for i in range(k):
        if arr[i] and seq[i]>seq[i+1]:
            suc=False
            break
        elif not arr[i] and seq[i]<seq[i+1]:
            suc=False
            break
    if suc:
        num=int(''.join([str(c) for c in seq]))
        high=max(high,num)
        low=min(low,num)
print(high)
if len(str(low))!=k+1:
    print('0'+str(low))
else:
    print(low)