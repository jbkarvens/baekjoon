def qt(A):
    n=len(A)
    c=A[0][0]
    chk=True
    for i in range(n*n):
        if A[i//n][i%n]!=c:
            chk=False
            break
    if chk:
        return str(c)
    a1=qt([r[:n//2] for r in A[:n//2]])
    a2=qt([r[n//2:] for r in A[:n//2]])
    a3=qt([r[:n//2] for r in A[n//2:]])
    a4=qt([r[n//2:] for r in A[n//2:]])
    return '('+a1+a2+a3+a4+')'

N=int(input())
A=[]
for _ in range(N):
    A.append(input())
print(qt(A))