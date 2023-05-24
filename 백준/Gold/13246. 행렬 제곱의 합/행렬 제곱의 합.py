NUM=1000
class mat:
    def __init__(self,lst):
        self.Y=[[v%NUM for v in ls] for ls in lst]
    def __add__(self,other):
        U=self.Y
        V=other.Y
        W=[[U[i][j]+V[i][j] for j in range(len(U[0]))] for i in range(len(U))]
        return mat(W)
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
    def __pow__(self,other):
        U=self
        tmp=other
        tmplst=[]
        while tmp>1:
            if tmp&1==1:
                tmplst.append(True)
            else:
                tmplst.append(False)
            tmp>>=1
        tmplst=tmplst[::-1]
        for tf in tmplst:
            U=U*U
            if tf:
                U=self*U
        return U

N,B=map(int,input().split())
A=[]
for _ in range(N):
    A.append(list(map(int,input().split())))
S=mat(A)
A=mat(A)
tmp=B
Blst=[]
while tmp>1:
    if tmp&1==1:
        Blst.append(True)
    else:
        Blst.append(False)
    tmp>>=1
Blst=Blst[::-1]
i=1
for tf in Blst:
    S=S+S*(A**i)
    i*=2
    if tf:
        S=A+S*A
        i+=1

for i in range(N):
    print(*((S.Y)[i]))