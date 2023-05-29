while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    else:
        lst=''
        if a%b==0:
            lst='multiple'
        elif b%a==0:
            lst='factor'
        else:
            lst='neither'
        print(lst)