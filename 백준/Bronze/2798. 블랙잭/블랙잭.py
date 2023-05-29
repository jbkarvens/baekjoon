N,M=map(int,input().split())
lst=list(map(int,input().split()))
mySum=-1
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            tmp=lst[i]+lst[j]+lst[k]
            if mySum<tmp<=M:
                mySum=tmp
print(mySum)