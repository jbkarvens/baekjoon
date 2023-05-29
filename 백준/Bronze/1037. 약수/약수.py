d=int(input())
lst=list(map(int,input().split()))
lst.sort()
if d==1:
    print(lst[0]**2)
else:
    print(lst[0]*lst[d-1])