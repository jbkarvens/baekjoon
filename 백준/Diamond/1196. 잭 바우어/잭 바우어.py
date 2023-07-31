from math import log1p

# -ln(1-x)
def my_ln(x):
    a=0
    for i in range(1,100000):
        a+=x**i/i
    return a

def har(n):
    cut = 10**6
    if n<cut:
        a=0
        for i in range(1,n+1):
            a+=1/i
    else:
        bern = [1,1/6,-1/30,1/42,-1/30,5/66,-691/2730,7/6,-3617/510,43867/798,-174611/330]
        a=0.57721566490153286060651209
        a+=log1p(n-1)+0.5/n
        for i in range(1,8):
            a-=bern[i]/(2*i*n**(2*i))
    return a

if __name__=='__main__':
    n,k=map(int,input().split())
    if k<10**6:
        a=0
        for i in range(n-k+1,n+1):
            a+=n/i
    else:
        if k/n<0.5:
            a=n*my_ln(k/n)+0.5-0.5*n/(n-k)-1/12/n+1/(120*n**3)+n/12/(n-k)**2-n/(120*(n-k)**4)
        else:
            a=n*(har(n)-har(n-k))
    print(a)