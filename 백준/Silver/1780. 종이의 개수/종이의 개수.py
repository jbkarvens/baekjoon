def dc(A):
    n=len(A)
    c=A[0][0]
    chk=True
    for i in range(n*n):
        if A[i//n][i%n]!=c:
            chk=False
            break
    if chk:
        if c==-1:
            return 1,0,0
        elif c==0:
            return 0,1,0
        else:
            return 0,0,1
    a,b,c=0,0,0
    for i in range(9):
        a1,b1,c1=dc([r[(n//3)*(i%3):(n//3)*(i%3+1)] for r in A[(n//3)*(i//3):(n//3)*(i//3+1)]])
        a+=a1
        b+=b1
        c+=c1
    return a,b,c

N=int(input())
A=[]
for _ in range(N):
    A.append(list(map(int,input().split())))
a,b,c=dc(A)
print(a)
print(b)
print(c)