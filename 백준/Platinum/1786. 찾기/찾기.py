import sys
input = sys.stdin.readline

def kmp(S, W):
    T=[0 for _ in range(len(W)+1)]
    pos,cnd=1,0
    T[0]=-1
    while pos<len(W):
        if W[pos]==W[cnd]:
            T[pos]=T[cnd]
        else:
            T[pos]=cnd
            while cnd>=0 and W[pos]!=W[cnd]:
                cnd=T[cnd]
        pos+=1
        cnd+=1
    T[pos]=cnd

    j=k=0
    P=[]
    while j<len(S):
        if W[k]==S[j]:
            j+=1
            k+=1
            if k==len(W):
                P.append(j-k)
                k=T[k]
        else:
            k=T[k]
            if k<0:
                j+=1
                k+=1
    return P

if __name__=='__main__':
    T=input().rstrip()
    P=input().rstrip()
    res=kmp(T,P)
    res =[v+1 for v in res]
    print(len(res))
    print(*res)
