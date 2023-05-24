NUM=1000
class mat:
    def __init__(self,lst):
        self.Y=[[v%NUM for v in ls] for ls in lst]
    def __mul__(self,other):
        U=self.Y
        V=other.Y
        a=len(U)
        b=len(U[0])
        c=len(V[0])
        W=[[None for _ in range(c)] for _ in range(a)]
        for i in range(a):
            for k in range(c):
                tmp=0
                for j in range(b):
                    tmp+=U[i][j]*V[j][k]
                W[i][k]=tmp%NUM
        return mat(W)

N,B=map(int,input().split())
A=[]
for _ in range(N):
    A.append(list(map(int,input().split())))
X=[x[:] for x in A]
A=mat(A)
X=mat(X)

Blst=[]
tmp=B
while tmp>1:
    if tmp&1==1:
        Blst.append(True)
    else:
        Blst.append(False)
    tmp>>=1
Blst=Blst[::-1]
for tf in Blst:
    X=X*X
    if tf:
        X=A*X

for i in range(N):
    print(*((X.Y)[i]))