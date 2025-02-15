for _ in range(int(input())):
    a,b,c=map(int,input().split())
    suc=True
    if not(a>=c and (a+c)%2==0):
        suc=False
    elif a==0 and b%2==1:
        suc=False
    if suc:
        print('Yes')
    else:
        print('No')
        