A=int(input())
B=int(input())
C=int(input())
print(A+B-C)
d,tmp=0,B
while tmp>0:
    tmp//=10
    d+=1
print(A*10**d+B-C)