N=10**9+7
n,m=map(int,input().split())
x,y,e=n,m,[]
while y>0:x,y=y,x%y
while x>1:
    e.append(x%2)
    x//=2
x=y=1
while len(e)>0:
    i=e.pop()
    if i: x,y=y*y+x*x,y*(y+2*x)
    else: x,y=x*(2*y-x),x*x+y*y
    x%=N
    y%=N
print(x)