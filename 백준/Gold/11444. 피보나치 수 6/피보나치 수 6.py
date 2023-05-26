def fib(n,m):
    a,b=1,1
    ls=[]
    while n>1:
        ls.append(n%2==1)
        n>>=1
    ls.reverse()
    for tf in ls:
        # F_2n+1 = F_n^2+F_n+1^2
        # F_2n = F_n*(F_n+1 - F_n)+F_n+1 F_n
        a,b=(a*(2*b-a))%m,(a*a+b*b)%m
        if tf:
            a,b=b,(a+b)%m
    return a
print(fib(int(input()),10**9+7))