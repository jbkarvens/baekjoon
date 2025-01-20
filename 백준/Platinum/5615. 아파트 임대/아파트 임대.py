def MR(n):
    if n<100:
        if n==1:
            return False
        elif n==2:
            return False
        d=3
        while d*d<=n:
            if n%d==0:
                return False
            d+=2
        return True
    s,d=0,n-1
    while not d&1:
        s+=1
        d>>=1
    for a in [2,3,5,7,11,13,17,19]:
        x=y=pow(a,d,n)
        for _ in range(s):
            y=pow(x,2,n)
            if y==1 and x!=1 and x!=n-1:
                return False
            x=y
        if y!=1:
            return False
    return True
res=0
for _ in range(int(input())):
    x=int(input())
    if MR(2*x+1):
        res+=1
print(res)