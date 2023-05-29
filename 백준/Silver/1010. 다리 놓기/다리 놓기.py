T=int(input())
for _ in range(T):
    n,m=map(int,input().split())
    num=1
    n=min(n,m-n)
    for i in range(m-n+1,m+1):
        num*=i
    for i in range(1,n+1):
        num=num//i
    print(num)