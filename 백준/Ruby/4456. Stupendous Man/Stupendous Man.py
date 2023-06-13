import sys
input_func=sys.stdin.readline

while True:
    n = int(input_func())
    if n==0:
        break
    x = list(map(int, input_func().split()))
    checkcross = True
    for i in range(2*n):
        for j in range(i+1, 2*n):
            if x[i]==x[j] and (i-j)%2==0:
                checkcross = False
    if not checkcross:
        print('escaped')
        continue
    for i in range(2*n):
        for j in range(i+1, 2*n):
            if x[i]==x[j]:
                tmp = x[i+1:j][::-1]
                for k in range(i+1, j):
                    x[k] = tmp[k-i-1]
    idx_left = [None for _ in range(n+1)]
    idx_right = [None for _ in range(n+1)]
    for i in range(2*n):
        v = x[i]
        if idx_left[v]==None:
            idx_left[v] = i
        else:
            idx_right[v] = i
    yes = False
    for S in range(0,1<<(n+1),2):
        chk = True
        for i in range(1,n+1):
            for j in range(1, n+1):
                if idx_left[i]<idx_left[j]<idx_right[i]<idx_right[j] and (S&(1<<i)!=0) == (S&(1<<j)!=0):
                    chk = False
        if chk:
            yes = True
    if yes:
        print('caught')
    else:
        print('escaped')