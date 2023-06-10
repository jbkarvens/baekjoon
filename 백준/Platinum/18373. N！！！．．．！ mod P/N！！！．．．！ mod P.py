n,k,p=map(int,input().split())
a=0
if n==2:
    a=2%p
elif k==n==3:
    k,n=2,6
if k==2 and 2<n<=12:
    for i in range(3,n+1):k*=i
    if k<p:
        if n==12:
            t=1
            for i in range(k+1,p):t=(t*i)%p
            a=pow(-t,-1,p)
        else:
            t=1
            for i in range(2,k+1):t=(t*i)%p
            a=t
print(a)