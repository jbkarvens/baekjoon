def ccw(a,b,c):
    z=(a[0]-b[0])*(c[1]-b[1])-(a[1]-b[1])*(c[0]-b[0])
    if z<0: return 1
    elif z>0: return -1
    else: return 0
def cross(A,B,C,D):
    if ccw(A,B,C)*ccw(A,B,D)<=0 and ccw(C,D,A)*ccw(C,D,B)<=0:
        return 1
    else:
        return 0
x1,y1,x2,y2=map(int,input().split())
x3,y3,x4,y4=map(int,input().split())
A=[x1,y1]
B=[x2,y2]
C=[x3,y3]
D=[x4,y4]
print(cross(A,B,C,D))