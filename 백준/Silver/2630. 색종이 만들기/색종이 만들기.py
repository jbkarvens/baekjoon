def wb(A):
    n=len(A)
    b=A[0][0]
    chk=True
    for i in range(n*n):
        if A[i//n][i%n]!=b:
            chk=False
            break
    if chk:
        return 1-b,b
    w1,b1=wb([r[:n//2] for r in A[:n//2]])
    w2,b2=wb([r[n//2:] for r in A[:n//2]])
    w3,b3=wb([r[:n//2] for r in A[n//2:]])
    w4,b4=wb([r[n//2:] for r in A[n//2:]])
    return w1+w2+w3+w4,b1+b2+b3+b4

N=int(input())
A=[]
for _ in range(N):
    A.append(list(map(int,input().split())))
w,b=wb(A)
print(w)
print(b)