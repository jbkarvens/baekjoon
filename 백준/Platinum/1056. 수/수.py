import math
D={1:0,2:1}
def A(n):
    if n in D:
        return D[n]
    r=n-1
    for k in range(2,int(math.log(n)/math.log(2))+2):
        a=int(n**(1/k))
        if a**k>n:a-=1
            
        for i in range(1,k):
            if k%i==0:
                b=a**i
                if a>1:
                    r=min(n-a**k+1+A(b),r)
                b=(a+1)**i
                if a>0:
                    r=min((a+1)**k-n+1+A(b),r)
    D[n]=r
    return r
print(A(int(input())))