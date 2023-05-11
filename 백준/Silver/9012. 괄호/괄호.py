T=int(input().rstrip())
for _ in range(T):
    lst=input().rstrip()
    tmp=[]
    isvp=True
    for i in range(len(lst)):
        if lst[i]=='(':
            tmp.append('(')
        elif lst[i]==')':
            try:
                tmp.pop()
            except:
                isvp=False
                break
    if len(tmp)!=0:
        isvp=False
    if isvp:
        print('YES')
    else:
        print('NO')