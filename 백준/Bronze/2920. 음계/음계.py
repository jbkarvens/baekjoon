lst=list(map(int,input().split()))
if lst[0]<lst[1]:
    up=1
else:
    up=-1
for i in range(7):
    if lst[i]<lst[i+1]:
        if not up==1:
            up=0
            break
    elif up==1:
        up=0
        break
if up==1:
    print('ascending')
elif up==-1:
    print('descending')
else:
    print('mixed')