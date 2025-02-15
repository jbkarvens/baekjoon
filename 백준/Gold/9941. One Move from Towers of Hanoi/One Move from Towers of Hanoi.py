def other(x,y):
    if x=='A':
        if y=='B':
            return 'C'
        else:
            return 'B'
    elif x=='B':
        if y=='A':
            return 'C'
        else:
            return 'A'
    else:
        if y=='A':
            return 'B'
        else:
            return 'A'

def hanoi(k,n,start,end):
    if n==1:
        return 1,start,end
    moves=pow(2,n-1)-1
    if k<=moves:
        return hanoi(k,n-1,start,other(start,end))
    elif k==moves+1:
        return n,start,end
    else:
        return hanoi(k-(moves+1),n-1,other(start,end),end)

t=1
while True:
    k,n=map(int,input().split())
    if k==n==0:
        break
    num,start,end=hanoi(k,n,'A','C')
    print(f'Case {t}: {num} {start} {end}')
    t+=1