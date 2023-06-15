import sys
lucky = list(range(-1,1010000,2))
for i in range(2,6600):
    x = lucky[i]
    del lucky[x::x]
lucky_set = set(lucky[:72000+1])
for _ in range(int(sys.stdin.readline())):
    if int(sys.stdin.readline()) in lucky_set:
        sys.stdout.write('lucky\n')
    else:
        sys.stdout.write('unlucky\n')