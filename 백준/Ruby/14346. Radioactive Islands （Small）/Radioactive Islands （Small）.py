# from matplotlib import pyplot as plt
FAIL_ANS = 100000
PRECISION = 0.001
Y_UP=20
Y_DOWN=-20
X_LEFT = -10
X_RIGHT = 10
ONE_STEP=0.01
C_UP = 10
C_DOWN = -10
A_UP = 10
A_DOWN = -10
def F(x,y,yp,c=0):
    a =1 / (x**2 + (y - c)**2)
    return 2*(1+yp*yp)/(1+a)*(a*a)*(x*yp-(y-c)*(1+yp**2))

def L(x,y,yp,c=0):
    return (1+yp*yp)**0.5 * (1+ 1/(x*x+(y-c)*(y-c)))

def RK4(x,y,yp,c=0):
    h=ONE_STEP
    n=int((X_RIGHT-X_LEFT)/h)
    ans=0
    # xrem=[]
    # yrem=[]
    for _ in range(n):
        # xrem.append(x)
        # yrem.append(y)
        if not Y_DOWN<y<Y_UP:
            return FAIL_ANS,y
        ans+=L(x,y,yp,c)*h
        dx1 = h*yp
        dv1 = h*F(x,y,yp,c)
        dx2 = h*(yp+dv1/2)
        dv2 = h*F(x+h/2,y+dx1/2,yp+dv1/2,c)
        dx3 = h*(yp+dv2/2)
        dv3 = h*F(x+h/2,y+dx2/2,yp+dv1/2,c)
        dx4 = h*(yp+dv3)
        dv4 = h*F(x+h,y+dx3,yp+dv1,c)
        dx = (dx1+2*dx2+2*dx3+dx4)/6
        dv = (dv1+2*dv2+2*dv3+dv4)/6
        x += h
        y += dx
        yp += dv
    return ans,y
    # return ans,y,xrem,yrem

def find_yp0(a,b,c,low,high):
    ans = FAIL_ANS
    while high-low>=PRECISION/2:
        mid = (low+high)/2
        ans,y=RK4(X_LEFT,a,mid,c)
        # ans,y,xrem,yrem=RK4(X_LEFT,a,mid,c)
        if y>=b:
            high = mid
        else:
            low = mid
    # plt.plot(xrem,yrem)
    return ans

def solve(a,b,c):
    yp0=[(C_DOWN-a)/(0-X_LEFT),(C_UP-a)/(0-X_LEFT),(c-a)/(0-X_LEFT)]
    yp0.sort()
    ans = FAIL_ANS
    for i in range(len(yp0)-1):
        ans = min(ans, find_yp0(a,b,c,yp0[i],yp0[i+1]))
    return ans

if __name__=='__main__':
    for i in range(int(input())):
        n,a,b=input().split()
        c=list(map(float,input().split()))
        n=int(n)
        a=float(a)
        b=float(b)
        print(f'Case #{i+1}: {round(solve(a,b,c[0]),2)}')
