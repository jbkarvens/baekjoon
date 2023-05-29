class mat:
    def __init__(self,A):
        self.X=A[:]
    def __mul__(self,other):
        A=self.X
        B=other.X
        n=len(A)
        m=len(B)
        k=len(B[0])
        C=[[0 for _ in range(k)] for _ in range(n)]
        for i in range(n):
            for j in range(k):
                tmp=0
                for t in range(m):
                    tmp+=A[i][t]*B[t][j]
                C[i][j]=tmp
        return mat(C)
A=[]
n,_=map(int,input().split())
for _ in range(n):
    A.append(list(map(int,input().split())))
A=mat(A)
B=[]
m,_=map(int,input().split())
for _ in range(m):
    B.append(list(map(int,input().split())))
B=mat(B)
C=(A*B).X
for i in range(n):
    print(*C[i])