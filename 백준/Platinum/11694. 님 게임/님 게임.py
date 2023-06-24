if __name__=='__main__':
    N=int(input())
    P=[*map(int,input().split())]
    win=True
    nim = 0
    chk = True
    for p in P:
        nim^=p
        if p!=1:
            chk = False
    if chk:
        if N%2==1:
            win = True
        else:
            win = False
    else:
        if nim==0:
            win = True
        else:
            win = False
    if not win:
        print('koosaga')
    else:
        print('cubelover')