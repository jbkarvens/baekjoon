a1,a0=map(int,input().split())
c=int(input())
n0=int(input())
if c>=a1:
    if (c-a1)*n0-a0>=0:
        print(1)
    else:
        print(0)
else:
    print(0)