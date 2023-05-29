chess=[1,1,2,2,2,8]
lst=list(map(int,input().split()))
print(*[chess[i]-lst[i] for i in range(len(chess))])