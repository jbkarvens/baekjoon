import sys
for i in range(int(sys.stdin.readline())):
    print("Case #{0}: {1}".format(i+1,sum(map(int,sys.stdin.readline().split()))))