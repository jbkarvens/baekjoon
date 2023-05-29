ang=[]
for i in range(3):
    ang.append(int(input()))
if ang[0]==ang[1]==ang[2]==60:
    print('Equilateral')
elif sum(ang)!=180:
    print('Error')
elif ang[0]==ang[1] or ang[0]==ang[2] or ang[1]==ang[2]:
    print('Isosceles')
else:
    print('Scalene')