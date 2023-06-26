from random import randint
MR_TEST_LIST = [2,3,5,7,11,13,17,19,23,29]
SMALL_PRIME=100

def is_small_prime(n):
    if n<=1:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    i=3
    while i*i<=n:
        if n%i==0: return False
        i+=2
    return True

def MR(n):
    if n<SMALL_PRIME:
        return is_small_prime(n)
    s,tmp=0,n-1
    while tmp&1==0:
        tmp>>=1
        s+=1
    d=(n-1)>>s
    for a in MR_TEST_LIST:
        a_witness=False
        cal=pow(a,d,n)
        if cal==1 or cal==n-1:
            a_witness=True
            continue
        for _ in range(1,s):
            cal=pow(cal,2,n)
            if cal==n-1:
                a_witness=True
        if not a_witness:
            return False
    return True

def isPrime(n):
    if n<SMALL_PRIME:
        return is_small_prime(n)
    else:
        return MR(n)

def get_div(pfac,idx,div):
    k=len(idx)
    if len(idx)==len(pfac):
        cur = 1
        for i in range(k):
            cur*=pow(pfac[i][0],idx[i])
        div.append(cur)
        return
    for i in range(pfac[k][1]+1):
        get_div(pfac,idx+[i],div)

def divisor(prime_list):
    div = []
    pfac = []
    for p in prime_list:
        if len(pfac)==0 or pfac[-1][0]!=p:
            pfac.append([p,1])
        else:
            pfac[-1][1]+=1
    get_div(pfac,[],div)
    div.sort()
    return div

if __name__=='__main__':
    T=200000
    # m = N-1
    fac = [2]*12+[3]*6+[5]*4+[7]*2+[11]*1
    m = 1
    for p in fac:
        m*=p
    divs=divisor(fac)
    plst = []
    for d in divs:
        if 10**7<d+1<10**8 and isPrime(d+1):
            plst.append(d+1)
    moddict=dict()
    idxset=set()
    while len(moddict)<T:
        x1=[]
        while len(x1)<6:
            i=randint(0,len(plst)-1)
            if i in x1:
                continue
            x1.append(i)
        x1.sort()
        if tuple(x1) in idxset:
            continue
        prod=1
        for i in x1:
            prod=(prod*plst[i])%m
        idxset.add(tuple(x1))
        moddict[pow(prod,-1,m)]=x1
    count=0
    ans_idx=[]
    while count<T:
        x2=[]
        while len(x2)<5:
            i=randint(0,len(plst)-1)
            if i in x1 or i in x2:
                continue
            x2.append(i)
        count+=1
        prod=1
        for i in x2:
            prod=(prod*plst[i])%m
        if prod in moddict:
            ans_idx = moddict[prod]+x2
            break
    ans = [plst[i] for i in ans_idx]
    ans.sort()
    print(*ans)
    # test
    n = 1
    for p in ans:
        n*=p
    for p in ans:
        if (n-1)%(p-1)!=0:
            print('WRONG!!!')