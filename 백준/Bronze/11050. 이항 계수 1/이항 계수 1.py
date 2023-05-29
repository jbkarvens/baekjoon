n,k=map(int,input().split())
num=1
for i in range(1,n+1):
    num*=i
for i in range(1,k+1):
    num=num//i
for i in range(1,n-k+1):
    num=num//i
print(num)