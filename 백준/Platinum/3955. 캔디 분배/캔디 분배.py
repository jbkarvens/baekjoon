for _ in range(int(input())):
    K,C=map(int,input().split())
    q=[]
    r=[C,K]
    while True:
        qnew=r[-2]//r[-1]
        rnew=r[-2]-qnew*r[-1]
        if rnew==0:
            break
        q.append(qnew)
        r.append(rnew)
    if r[-1]!=1:
        print('IMPOSSIBLE')
        continue
    i=len(q)-1
    u=0
    v=1
    while i>=0:
        u,v=v,u-v*q[i]
        i-=1
    v=-v
    if v<=0:
        t=(-v)//K+1
        u+=K*t
        v+=C*t
    if u>10**9:
        print('IMPOSSIBLE')
    else:
        print(u)