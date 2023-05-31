k=1
m=[list(map(int,input().split())) for _ in range(4)]
x=m[0][1]
y=m[0][2]
z=m[1][2]
u=m[0][3]
v=m[1][3]
w=m[2][3]
b=y**2-z**2+x**2
b/=2*x
t=(2*x*y)**2-(y**2-z**2+x**2)**2
if t<0:k=0
else:
 c=t**0.5/(2*x)
 d=(x**2+u**2-v**2)/(2*x)
 e=b**2+c**2-2*b*d-w**2+u**2
 if 4*c**2*(u**2-d**2)<e**2:
  k=0
print('YES'if k else'NO')