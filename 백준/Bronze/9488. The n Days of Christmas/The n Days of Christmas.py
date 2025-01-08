import sys
input=sys.stdin.readline
while True:
    a=int(input())
    if a==0:
        break
    print(a*(a+1)*(a+2)//6)