def sq(n):
    if n==0:
        return [[1,3],[1,4],[-1,5]]
    if n<0:
        return [[-x[0],x[1]] for x in sq(-n)]
    if n==2:
        return [[1,6],[-1,5],[-1,3]]
    if n==int(n**0.5)**2:
        return [[1,int(n**0.5)]]
    if n%2==1:
        return [[1,(n+1)//2],[-1,(n-1)//2]]
    if n%4==0:
        return [[1,n//4+1],[-1,n//4-1]]
    for i in range(1,int((n/2)**0.5)+1):
        j=int((n-i*i)**0.5)
        if i*i+j*j==n and i!=j:
            return [[1,i],[1,j]]
    return [[1,(n+2)//2],[-1,n//2],[-1,1]]
lst=sq(int(input()))
print(len(lst))
for x in lst:
    if x[0]==1:
        print('+ '+str(x[1]))
    else:
        print('- '+str(x[1]))