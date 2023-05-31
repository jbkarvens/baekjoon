def ccw(a,b,c):
    z=(a[0]-b[0])*(c[1]-b[1])-(a[1]-b[1])*(c[0]-b[0])
    if z<0:
        return 1
    elif z>0:
        return -1
    else:
        return 0
def cross(A,B,C,D):
    ab=ccw(A,B,C)*ccw(A,B,D)
    cd=ccw(C,D,A)*ccw(C,D,B)
    if ab==0 and cd==0:
        if A>B: A,B=B,A
        if C>D: C,D=D,C
        
        if A<=D and C<=B:
            return 1
        else:
            return 0
    elif ab<=0 and cd<=0:
        return 1
    else:
        return 0
def crosspt(A,B,C,D):
    x1,y1=A
    x2,y2=B
    x3,y3=C
    x4,y4=D
    slope_fn=(x4-x3)*(y2-y1)-(x2-x1)*(y4-y3)
    rem=(x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
    if slope_fn!=0:
        s=rem/slope_fn
        return x3+(x4-x3)*s,y3+(y4-y3)*s
    elif rem==0:
        if A>B: A,B=B,A
        if C>D: C,D=D,C
        if A==D:
            return A
        elif B==C:
            return B
    return None,None
x1,y1,x2,y2=map(int,input().split())
x3,y3,x4,y4=map(int,input().split())
A=(x1,y1)
B=(x2,y2)
C=(x3,y3)
D=(x4,y4)
docross=cross(A,B,C,D)
print(docross)
if docross:
    x,y=crosspt(A,B,C,D)
    if x!=None:
        print(x,y)