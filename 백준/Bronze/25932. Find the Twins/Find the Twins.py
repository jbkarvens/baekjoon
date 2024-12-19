import sys
for _ in range(int(sys.stdin.readline())):
    arr=list(map(int,sys.stdin.readline().split()))
    zack,mack=False,False
    for n in arr:
        if n==18:
            mack=True
        elif n==17:
            zack=True
    print(*arr)
    if zack:
        if mack:
            print("both")
        else:
            print("zack")
    else:
        if mack:
            print("mack")
        else:
            print("none")
    print()