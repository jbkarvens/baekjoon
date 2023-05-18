def stars(n,a=0,b=0):
    if n==1:
        lst[a][b]='*'
    else:
        m=n//3
        stars(m,a,b)
        stars(m,a,b+m)
        stars(m,a,b+2*m)
        stars(m,a+m,b)
        for i in range(a+m,a+2*m):
            for j in range(b+m,b+2*m):
                lst[i][j]=' '
        stars(m,a+m,b+2*m)
        stars(m,a+2*m,b)
        stars(m,a+2*m,b+m)
        stars(m,a+2*m,b+2*m)
N=int(input())
lst=[[None for _ in range(N)] for _ in range(N)]
stars(N)
for i in range(len(lst)):
    print(''.join(lst[i]))