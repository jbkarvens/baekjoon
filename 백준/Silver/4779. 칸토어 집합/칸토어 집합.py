def cantor(n):
    if n==0:
        print('-',end='')
    else:
        cantor(n-1)
        for _ in range(3**(n-1)):
            print(' ',end='')
        cantor(n-1)
while True:
    try:
        cantor(int(input()))
        print('')
    except:
        break
