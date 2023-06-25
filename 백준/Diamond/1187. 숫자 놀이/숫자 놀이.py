def solve(A,n,idx):
    if n==1:
        return idx
    idx1=idx[:n-1]
    a1=solve(A,n//2,idx1)
    idx2=idx[n-1:2*n-2]
    a2=solve(A,n//2,idx2)
    rem=[]
    i1,i2=0,0
    for v in idx:
        if v==a1[i1]:
            if i1<n//2-1:
                i1+=1
        elif v==a2[i2]:
            if i2<n//2-1:
                i2+=1
        else:
            rem.append(v)
    a3=solve(A,n//2,rem)
    s1=sum([A[i] for i in a1])
    s2=sum([A[i] for i in a2])
    s3=sum([A[i] for i in a3])
    if (s1+s2)%n==0:
        return sorted(a1+a2)
    elif (s1+s3)%n==0:
        return sorted(a1+a3)
    else:
        return sorted(a2+a3)

if __name__=='__main__':
    N=int(input())
    A=[*map(int,input().split())]
    ans=solve(A,N,list(range(2*N-1)))
    print(*[A[i] for i in ans])