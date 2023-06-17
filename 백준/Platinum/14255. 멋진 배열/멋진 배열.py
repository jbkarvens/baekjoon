def solve(A):
    n=len(A)
    for t in range(n):
        for i in range(t,n):
            for j in range(i+1,n):
                diff = None
                for k in range(n):
                    if not(A[i][k] == None) and not (A[j][k] == None):
                        diff=A[i][k]-A[j][k]
                        break
                if not(diff==None):
                    for k in range(n):
                        if not(A[j][k]==None):
                            if not(A[i][k]==None):
                                if A[j][k]+diff!=A[i][k]:
                                    return []
                            else:
                                A[i][k]=A[j][k]+diff
                                if A[i][k]<0:
                                    return []
                        elif not(A[i][k]==None):
                            A[j][k]=A[i][k]-diff
                            if A[j][k]<0:
                                return []
                    if diff>0:
                        A[i]=A[j]
                    else:
                        A[j]=A[i]
    simpA=[]
    chk=[]
    for i in range(n):
        added=False
        for k in range(n):
            if k in chk and not(A[i][k]==None):
                added=True
                break
            elif not(A[i][k]==None):
                simpA.append(A[i])
                for k2 in range(n):
                    if not(A[i][k2]==None):
                        chk.append(k2)
                added=True
                break
        if not added:
            simpA.append(A[i])
            for k in range(n):
                if not (A[i][k]==None):
                    chk.append(k)
    res=[]
    for i in range(len(simpA)):
        mymin=None
        for k in range(n):
            if not(simpA[i][k]==None):
                if mymin==None:
                    mymin=simpA[i][k]
                else:
                    mymin=min(mymin,simpA[i][k])
        res.append(mymin)
    return res


if __name__=='__main__':
    NUM = 10**9+7
    n=int(input())
    A=[[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        sen=input().rstrip()
        for j in range(n):
            if sen[j]!='-':
                A[i][j]=int(sen[j])
    lst=solve(A)
    a,b=1,1
    for m in lst:
        a=(a*(m+1))%NUM
        b=(b*m)%NUM
    print((a-b)%NUM)