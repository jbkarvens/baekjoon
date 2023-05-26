def fib(n,m):
    if n==0:
        return 0
    a,b=1,1
    ls=[]
    while n>1:
        ls.append(n%2==1)
        n>>=1
    ls.reverse()
    for tf in ls:
        a,b=(a*(2*b-a))%m,(a*a+b*b)%m
        if tf:
            a,b=b,(a+b)%m
    return a

def find_fib(num,e):
    k=pow(10,e)
    if e==1:
        a,b,n=1,1,1
        res=[]
        while a!=1 or b!=1 or n==1:
            if a==num:
                res.append(n)
            a,b=b,(a+b)%k
            n+=1
        return res,n-1
    lst,T=find_fib(num%(k//10),e-1)
    ans=[]
    chk=False
    n=0
    while not chk:
        for i in lst:
            f=fib(n+i,k)
            if f==num:
                ans.append(n+i)
        n+=T
        if fib(n,k)==0 and fib(n+1,k)==1:
            chk=True
    return ans,n
    

if __name__=='__main__':
    ans,_=find_fib(int(input()),13)
    if len(ans)==0:
        print(-1)
    else:
        print(min(ans))