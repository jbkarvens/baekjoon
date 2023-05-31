chk=True
d=[list(map(int,input().split())) for _ in range(4)]
x=[None,0,0,0,0,0,0]
x[1]=d[0][1]
x[2]=d[0][2]
x[3]=d[1][2]
x[4]=d[0][3]
x[5]=d[1][3]
x[6]=d[2][3]
a=x[1]
b=(x[2]**2-x[3]**2+a**2)/(2*a)
if 4*a**2*x[2]**2-(x[2]**2-x[3]**2+a**2)**2<0:
    chk=False
else:
    c=(4*a**2*x[2]**2-(x[2]**2-x[3]**2+a**2)**2)**0.5/(2*a)
    d=(a**2+x[4]**2-x[5]**2)/(2*a)
    e=b**2+c**2-2*b*d-x[6]**2+x[4]**2
    if 4*c**2*x[4]**2<4*c**2*d**2+e**2:
        chk=False
if chk:
    print('YES')
else:
    print('NO')