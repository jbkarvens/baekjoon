NUM=10**9+7
n,k=map(int,input().split())
a,b=1,1
for i in range(1,k+1):
    a=(a*(n-k+i))%NUM
    b=(b*i)%NUM
print((a*pow(b,-1,NUM))%NUM)