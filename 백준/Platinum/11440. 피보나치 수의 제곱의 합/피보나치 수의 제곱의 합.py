NUM=10**9+7
n=int(input())
lst=[]
while n>1:
    if n%2==1:
        lst.append(True)
    else:
        lst.append(False)
    n//=2
lst=lst[::-1]
a,b=1,1
for tf in lst:
    a,b=a*(2*b-a),a*a+b*b
    if tf:
        a,b=b,a+b
    a%=NUM
    b%=NUM
print((a*b)%NUM)