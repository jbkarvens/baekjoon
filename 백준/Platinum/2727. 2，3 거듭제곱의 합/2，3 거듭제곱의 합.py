import math
def mySum(n,lst):
    if n==0:
        return lst
    if n==1:
        return [[0,0]]+lst
    if n%2==0 or n%3==0:
        tmp2,s2=n,0
        while tmp2%2==0:
            s2+=1
            tmp2//=2
        tmp3,s3=n,0
        while tmp3%3==0:
            s3+=1
            tmp3//=3
        tmplst=[[x[0]+s2,x[1]+s3] for x in mySum(n//(pow(2,s2)*pow(3,s3)),lst)]
        return sorted(tmplst)
    k=int(math.log(n,3))
    m=pow(3,k)
    return [[0,k]]+mySum(n-m,lst)

for _ in range(int(input())):
    lst=mySum(int(input()),[])
    print(len(lst))
    for e in lst:
        print(*e)