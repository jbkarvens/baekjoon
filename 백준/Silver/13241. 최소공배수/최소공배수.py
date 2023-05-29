A,B=map(int,input().rstrip().split())
x,y=A,B
while x%y!=0:
    x,y=y,x%y
print(A*B//y)