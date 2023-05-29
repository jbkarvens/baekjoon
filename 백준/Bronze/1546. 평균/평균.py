N=int(input())
lst=list(map(int,input().split()))
print(sum(lst)*100/N/max(lst))
