def sieve(n):
    pchk=[True for _ in range(n+1)]
    for i in range(2,n+1):
        if pchk[i]:
            j=i+i
            while j<=n:
                pchk[j]=False
                j+=i
    return [i for i in range(2,n+1) if pchk[i]]

def fac(n):
    plst=sieve(n)
    flst=[[] for _ in range(n+1)]
    for p in plst:
        r=p
        e=1
        while r<=n:
            i=r
            while i<=n:
                if (i//r)%p!=0:
                    flst[i].append([p,e])
                i+=r
            r*=p
            e+=1
    return flst

# e=1일떄는 hint없이, e>1이면 처음으로 q^e 배수가 되는 index인 hint 입력값을 줄 것
def fib_qdiv(q,e,hint=None):
    qe=pow(q,e)
    if e==1:
        n=1
        a,b=1,1
    else:
        n=hint
        a,b=1,1
        h_bin=[]
        while hint>1:
            h_bin.append(hint%2==1)
            hint>>=1
        h_bin.reverse()
        for tf in h_bin:
            # 다음 공식으로 F_hint를 빠르게 구한다
            # F_2n+1 = F_n^2+F_n+1^2
            # F_2n = F_n*(F_n+1 - F_n)+F_n+1 F_n
            a,b=(a*(2*b-a))%qe,(a*a+b*b)%qe
            if tf:
                a,b=b,(a+b)%qe
    c,d=a,b
    m=n
    while c%qe!=0:
        # a b는 F_n F_n+1 역할 c d는 F_m F_m+1 역할 F_m이 q^e배수 되는 처음 위치 찾기
        # F_m+n+1 = F_m F_n + F_m+1 F_n+1
        # F_m+n   = F_m(F_n+1 - F_n) + F_m+1 F_n
        c,d=(c*(b-a)+d*a)%qe, (c*a+d*b)%qe
        m+=n
    return m
    
if __name__=='__main__':
    n,p=map(int,input().split())
    qdiv_dict={}
    plst=sieve(p)
    for q in plst:
        e=1
        m=fib_qdiv(q,e)
        qdiv_dict[q]=m
        qe=q
        while True:
            e+=1
            qe*=q
            m=fib_qdiv(q,e,m)
            if m>n:
                break
            qdiv_dict[qe]=m
    fib_exp={}
    for q in plst:
        qe=q
        cout=0
        while qe in qdiv_dict:
            cout+=n//qdiv_dict[qe]
            qe*=q
        fib_exp[q]=cout
    pfac=fac(p)
    for i in range(2,p+1):
        lst=[]
        for qlst in pfac[i]:
            q,e=qlst[0],qlst[1]
            lst.append(fib_exp[q]//qlst[1])
        print(min(lst))