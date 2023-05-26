def cal_for_small(N):
    plst=[True for i in range(N+1)]
    Mobius_lst=[1 for _ in range(N+1)]
    
    Mobius_lst[2]=-1
    for j in range(2+2,N+1,2):
        plst[j]=False
        if j%4!=0:
            Mobius_lst[j]=-Mobius_lst[j]
        else:
            Mobius_lst[j]=0
    for i in range(3,N+1,2):
        if plst[i]:
            Mobius_lst[i]=-1
            i2=i*i
            for j in range(i+i,N+1,i):
                plst[j]=False
                if j%i2!=0:
                    Mobius_lst[j]=-Mobius_lst[j]
                else:
                    Mobius_lst[j]=0
    del plst
    return Mobius_lst

def S(N):
    if N<100:
        if N==0:
            return 0
        elif N==1:
            return 1
        lst=cal_for_small(N)
        cout=0
        for i in range(1,N+1):
            if lst[i]!=0:
                cout+=1
        return cout
    L=int(N**(1/5))
    D=int((N/L)**0.5)
        
    result=0

    Mobius_lst=cal_for_small(D)
    M_lst=[None for _ in range(D+1)]
    s=0
    for i in range(1,D+1):
        s+=Mobius_lst[i]
        M_lst[i]=s
    
    for i in range(1,D+1):
        result+=Mobius_lst[i]*(N//(i*i))

    M_other=[0 for _ in range(L+1)]
    for i in reversed(range(1,L)):
        Mx=1
        x=int((N/i)**0.5)
        cut=int(x**0.5)
        for j in range(1,x//(cut+1)+1):
            Mx-=M_lst[j]*(x//j-x//(j+1))
        for j in range(2,cut+1):
            if x//j<=D:
                Mx-=M_lst[x//j]
            else:
                Mx-=M_other[i*j*j]
        M_other[i]=Mx
        result+=Mx
        
    result-=(L-1)*M_lst[D]
    return result

if __name__=='__main__':
    mn,mx=map(int,input().split())
    print(S(mx)-S(mn-1))