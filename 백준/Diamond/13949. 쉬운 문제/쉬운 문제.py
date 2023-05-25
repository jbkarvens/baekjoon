k,n=map(int,input().split())
a,b,c=1,k,k+k*k
s,i=[a,b,c],0
for _ in range(n):
    print(a,b,c)
    a,b,c,=b,c,k*b+k*c-a
    a,b,c,=b,c,k*b+k*c-a
    a,b,c,=b,c,k*b+k*c-a
    while c>10**100 or a in s or b in s or c in s:
        a,b,c=s[i],s[i+1],s[i+2]
        i+=3
        a,b,c,=a,c,k*a+k*c-b
        a,b,c,=b,c,k*b+k*c-a
        a,b,c,=b,c,k*b+k*c-a
    s+=[a,b,c]