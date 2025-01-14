for _ in range(int(input())):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    dd=(x1-x2)**2+(y1-y2)**2
    if dd>(r1+r2)**2:
        print(0)
    elif dd==(r1+r2)**2:
        print(1)
    elif (r1-r2)**2<dd<(r1+r2)**2:
        print(2)
    elif dd==(r1-r2)**2:
        if r1==r2 and dd==0:
            print(-1)
        else:
            print(1)
    else:
        print(0)