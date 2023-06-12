import sys
input_func = sys.stdin.readline

def bet(p,high,low):
    q = (1-p)/p
    return (1-q**low)/(q**high-q**low)

def profit(p,x,high,low):
    prob = bet(p,high,low)
    return high*prob+low*(1-x)*(1-prob)

x,p=map(float,input_func().split())
if p==0:
    print(0)
else:
    p/=100
    x/=100
    u,v=1,-1
    cur = profit(p,x,u,v)
    while True:
        chk= True
        for du,dv in [(1,0),(-1,0),(0,1),(0,-1)]:
            up,vp=u+du,v+dv
            if up==0 or vp==0:
                continue
            tmp = profit(p,x,up,vp)
            if tmp>cur:
                cur=tmp
                u,v=up,vp
                chk=False
                break
        if chk:
            break
    print(profit(p,x,u,v))