def getdigit(n,K):
    arr=[None]*K
    for i in range(K):
        arr[K-1-i]=n%10
        n//=10
    return arr
N,K,P,X=map(int,input().split())
#    -0
# 3| _ |5
# 4| 1 |6
#    -2
nums=[[1,0,1,1,1,1,1],[0,0,0,0,0,1,1],[1,1,1,0,1,1,0],
      [1,1,1,0,0,1,1],[0,1,0,1,0,1,1],[1,1,1,1,0,0,1],
      [1,1,1,1,1,0,1],[1,0,0,0,0,1,1],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1]]
res=0
digit_cur=getdigit(X,K)
for i in range(1,N+1):
    cnt=0
    digit_new=getdigit(i,K)
    for j in range(K):
        for k in range(7):
            cnt+=nums[digit_cur[j]][k]^nums[digit_new[j]][k]
    if cnt<=P:
        res+=1
print(res-1)