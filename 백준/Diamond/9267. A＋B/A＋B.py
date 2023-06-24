import math
def solve(a,b,x):
    if b==0:
        a,b=b,a
    if a==0:
        if b==0:
            if x==0:
                return True
            else:
                return False
        else:
            if x%b==0:
                return True
            else:
                return False
    r0,r1=a,b
    s0,s1=1,0
    t0,t1=0,1
    while r1!=0:
        q = r0//r1
        r0,r1=r1,r0-q*r1
        s0,s1=s1,s0-q*s1
        t0,t1=t1,t0-q*t1
    ans=False
    if x%r0==0:
        s0=s0*(x//r0)
        t0=t0*(x//r0)
        a0,b0=a//r0,b//r0
        s,t=s0-b0*(s0//b0),t0+a0*(s0//b0)
        k=0
        while True: 
            d=math.gcd(s+b0*k,t-a0*k)
            if d==1 and s+b0*k>=0 and t-a0*k>=0:
                ans = True
                break
            if t-a0*k<0:
                break
            k+=1
    return ans

if __name__=='__main__':
    a,b,x=map(int,input().split())
    print('YES'if solve(a,b,x) else 'NO')