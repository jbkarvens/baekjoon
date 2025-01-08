import sys
while True:
    a=int(sys.stdin.readline())
    if a==0:
        break
    sys.stdout.write(str(a*(a+1)*(a+2)//6)+'\n')