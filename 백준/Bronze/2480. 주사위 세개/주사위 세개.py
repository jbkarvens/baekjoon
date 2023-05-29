a,b,c=map(int,input().split())
if a>b:a,b=b,a
if b>c:b,c=c,b
if a>b:a,b=b,a
if c==b:p=10000+1000*c if b==a else 1000+100*c
elif b==a:p=1000+100*a
else:p=100*c
print(p)