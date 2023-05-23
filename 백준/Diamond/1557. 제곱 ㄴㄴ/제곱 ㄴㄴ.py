N=10**9*2
M=int(N**0.5)
mu=[1 for _ in range(M+1)]
prime=[True for _ in range(M+1)]
for p in range(2,M+1):
    if prime[p]:
        mu[p]*=(-1)
        i=p+p
        j=1+1
        while i<=M:
            prime[i]=False
            if j%p==0:
                mu[i]=0
            else:
                mu[i]*=(-1)
            i+=p
            j+=1
mu_lst=[i for i in range(2,M+1) if mu[i]!=0]

def count_square_free(n):
    result=n
    for i in mu_lst:
        if i>int(n**0.5):
            break
        result+=mu[i]*(n//(i*i))
    return result

def nth_square_free(k):
    n=k
    r=count_square_free(n)
    while r<k:
        n+=(k-r)
        r=count_square_free(n)
    return n

print(nth_square_free(int(input())))