def legendre(a,p):
    if a==1 or p==2:
        return 1
    if not 0<a<p:
        return legendre(a%p,p)
    if a==p-1:
        return pow(-1,(p-1)//2)
    if a==2:
        return pow(-1,(p*p-1)//8)
    if a%2==0:
        return legendre(2,p)*legendre(a//2,p)
    if a>p/2:
        return legendre(p-1,p)*legendre(p-a,p)
    i=3
    while i*i<=a:
        if a%i==0:
            return legendre(i,p)*legendre(a//i,p)
        i+=2
    return pow(-1,((a-1)*(p-1))//4)*legendre(p,a)
for i in range(int(input())):
    if i>0:
        print()
    a,p=map(int,input().split())
    print('Scenario #{}:'.format(i+1))
    print(legendre(a, p))