import sys
input=sys.stdin.readline

while True:
    try:
        N=int(input())
    except:
        break
    arr=list(map(int,input().split()))
    if N<3:
        sys.stdout.write('1\n')
        continue
    i=N-3
    diff=arr[-1]-arr[-2]
    while i>=0:
        if arr[i]!=arr[i+1]-diff:
            break
        i-=1
    sys.stdout.write(f'{i+2}\n')