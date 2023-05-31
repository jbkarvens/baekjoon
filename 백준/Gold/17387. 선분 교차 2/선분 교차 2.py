def ccw(a,b,c):
    z=(a[0]-b[0])*(c[1]-b[1])-(a[1]-b[1])*(c[0]-b[0])
    if z<0: return 1
    elif z>0: return -1
    else: return 0
def cross(A,B,C,D):
    ab=ccw(A,B,C)*ccw(A,B,D)
    cd=ccw(C,D,A)*ccw(C,D,B)
    if ab==0 and cd==0:
        if A[0]>B[0] or (A[0]==B[0] and A[1]>B[1]):
            A,B=B,A
        if C[0]>D[0] or (C[0]==D[0] and C[1]>D[1]):
            C,D=D,C
        if A[0]>C[0] or (A[0]==C[0] and A[1]>C[1]):
            A,B,C,D=C,D,A,B
        if B[0]<C[0] or (B[0]==C[0] and B[1]<C[1]):
            return 0
        else:
            return 1
    elif ab<=0 and cd<=0: return 1
    else: return 0
x1,y1,x2,y2=map(int,input().split())
x3,y3,x4,y4=map(int,input().split())
A=(x1,y1)
B=(x2,y2)
C=(x3,y3)
D=(x4,y4)
print(cross(A,B,C,D))