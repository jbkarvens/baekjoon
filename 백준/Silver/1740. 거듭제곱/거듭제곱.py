n=int(input())
r,p=0,1
while n!=0:
    if n&1!=0:
        r+=p
    n>>=1
    p*=3
print(r)