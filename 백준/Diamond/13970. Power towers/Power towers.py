import sys
input=sys.stdin.readline
import math

def sieve(n):
    prime_check = [True for _ in range(n+1)]
    factors=[dict() for _ in range(n+1)]
    for p in range(2,n+1):
        if prime_check[p]:
            pp=p
            while pp<=n:
                for i in range(pp,n+1,pp):
                    if i!=p:
                        prime_check[i]=False
                    if p in factors[i]:
                        factors[i][p]+=1
                    else:
                        factors[i][p]=1
                pp*=p
    return factors

def cal_size(n,x):
    if n==1:
        cal_list[n]=x[-1]
        return
    cal_size(n-1,x)
    if cal_list[n-1]==10**6+1:
        if x[-n]==1:
            cal_list[n]=1
        else:
            cal_list[n]=10**6+1
    else:
        if cal_list[n-1]*math.log(x[-n])>math.log(10**6):
            cal_list[n]=10**6+1
        else:
            cal_list[n]=pow(x[-n],cal_list[n-1])
    return

def crt(rem,mod):
    M_tot=1
    for m in mod:
        M_tot*=m
    result=0
    for r,m in zip(rem,mod):
        mm=M_tot//m
        result += r*mm*pow(mm,-1,m)
    return result%M_tot

def solve(n,x,m):
    if n==1:
        return x[-1]%m
    elif n==2:
        return pow(x[-2],x[-1],m)
    # x와 공통소인 없는거:m2
    rem,mod=[],[]
    m2=m
    for p in factors[x[-n]]:
        if p in factors[m]:
            pp=pow(p,factors[m][p])
            m2//=pp
            mod.append(pp)
            rem.append(pow(x[-n],cal_list[n-1],pp))
    mod.append(m2)
    phi_m2=m2
    for p in factors[m2]:
        phi_m2-=phi_m2//p
    rem.append(pow(x[-n],solve(n-1,x,phi_m2),m2))
    return crt(rem,mod)

if __name__=='__main__':
    factors=sieve(10**6+5)
    T,M=map(int,input().split())
    for _ in range(T):
        sen=input().split()
        N,X=int(sen[0]),[*map(int, sen[1:])]
        cal_list=[None for _ in range(N+1)]
        cal_size(N,X)
        sys.stdout.write(str(solve(N,X,M))+'\n')