import sys
input = sys.stdin.readline
SMALL = 72000
lucky = list(range(-1,1010000,2))
for i in range(2,SMALL+1):
    x = lucky[i]
    del lucky[x::x]
lucky = lucky[:SMALL+1]
lucky_set=set()
for lk in lucky:
    lucky_set.add(lk)
for _ in range(int(input())):
    if int(input()) in lucky_set:
        print('lucky')
    else:
        print('unlucky')