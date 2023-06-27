import sys
input=sys.stdin.readline
import math

def cal_size(n,x):
    if n==1:
        cal_list[n]=x[-1]
        return
    cal_size(n-1,x)
    if cal_list[n-1]==10**7+1:
        if x[-n]==1:
            cal_list[n]=1
        else:
            cal_list[n]=10**7+1
    else:
        if cal_list[n-1]*math.log(x[-n])>math.log(10**7):
            cal_list[n]=10**7+1
        else:
            cal_list[n]=pow(x[-n],cal_list[n-1])
    return

def factors(n):
    if n in factor:
        return factor[n]
    result=dict()
    tmp=n
    for p in range(2,100):
        while n%p==0:
            n//=p
            if p in result:
                result[p]+=1
            else:
                result[p]=1
    factor[tmp]=result
    return result

def solve(n,x,m):
    if n==1:
        return x[-1]%m
    elif n==2:
        return pow(x[-2],x[-1],m)
    # x와 공통소인 없는거:m2
    rem,mod=[],[]
    m2=m
    for p in factors(x[-n]):
        if p in factors(m):
            pp=pow(p,factors(m)[p])
            m2//=pp
            mod.append(pp)
            rem.append(pow(x[-n],cal_list[n-1],pp))
    mod.append(m2)
    phi_m2=m2
    for p in factors(m2):
        phi_m2-=phi_m2//p
    rem.append(pow(x[-n],solve(n-1,x,phi_m2),m2))
    M_tot=1
    for m in mod:
        M_tot*=m
    result=0
    for r,m in zip(rem,mod):
        mm=M_tot//m
        result += r*mm*pow(mm,-1,m)
    return result%M_tot

if __name__=='__main__':
    factor=dict()
    while True:
        b=int(input())
        if b==0:
            break
        i=int(input())
        n=int(input())
        X=[b]*i
        cal_list=[None for _ in range(i+1)]
        cal_size(i,X)
        ans=solve(i,X,10**n)
        ans=str(ans)
        while len(ans)<n:
            ans='0'+ans
        sys.stdout.write(ans+'\n')