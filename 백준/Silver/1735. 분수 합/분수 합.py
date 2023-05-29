a,b=map(int,input().rstrip().split())
c,d=map(int,input().rstrip().split())
x,y=a*d+b*c,b*d
i,j=x,y
while i%j!=0:
    i,j=j,i%j
x=x//j
y=y//j
print(x,y)