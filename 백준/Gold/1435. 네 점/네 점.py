k=True
m=[list(map(int,input().split())) for _ in range(4)]
x1=m[0][1]
x2=m[0][2]
x3=m[1][2]
x4=m[0][3]
x5=m[1][3]
x6=m[2][3]
a=x1
b=(x2**2-x3**2+a**2)/(2*a)
t=(2*a*x2)**2-(x2**2-x3**2+a**2)**2
if t<0:
    k=False
else:
    c=t**0.5/(2*a)
    d=(a**2+x4**2-x5**2)/(2*a)
    e=b**2+c**2-2*b*d-x6**2+x4**2
    if 4*c**2*(x4**2-d**2)<e**2:
        k=False
if k:
    print('YES')
else:
    print('NO')