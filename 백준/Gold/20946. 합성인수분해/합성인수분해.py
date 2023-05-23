from random import randint
import math
MR_lst=[2,3,5,7,11,13]
def MR(n):
    if n<=1:
        return False
    if n in MR_lst:
        return True
    for a in MR_lst:
        s,d=0,n-1
        while d&1==0:
            s+=1
            d>>=1
        k=pow(a,d,n)
        if k==1 or (s>0 and k==n-1):
            continue
        a_witness=True
        for _ in range(1,s):
            k=(k*k)%n
            if k==n-1:
                a_witness=False
                break
        if a_witness:
            return False
    return True

def brent(n):
    y,c=randint(1,n-1),randint(1,n-1)
    g,r,q=1,1,1
    while g==1:
        x=y
        for _ in range(r):
            y=(y*y+c)%n
        ys=y
        for i in range(r):
            y=(y*y+c)%n
            q=(q*(x-y))%n
        g=math.gcd(q,n)
        r*=2
    if g==n:
        while True:
            ys=(ys*ys+c)%n
            g=math.gcd(x-ys,n)
            if g>1:
                break
    return g

def factor(n):
    if n==1:
        return []
    if MR(n):
        return [n]
    if n%2==0:
        return [2]+factor(n//2)
    for i in range(3,100,2):
        if n%i==0:
            return [i]+factor(n//i)
    k=brent(n)
    while k==1 or k==n:
        k=brent(n)
    return factor(k)+factor(n//k)

if __name__=='__main__':
    n=int(input())
    lst=sorted(factor(n))
    if len(lst)==1:
        print(-1)
    else:
        comp_lst=[]
        while len(lst)>3:
            comp_lst.append(lst[0]*lst[1])
            lst.remove(lst[0])
            lst.remove(lst[0])
        a=1
        for p in lst:
            a*=p
        comp_lst.append(a)
        print(*comp_lst)