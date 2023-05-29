import sys
input=sys.stdin.readline
while True:
    n=input().rstrip()
    if n=='0':
        break
    t=True
    for i in range(len(n)//2):
        if n[i]!=n[-1-i]:
            t=False
            break
    if t: print('yes')
    else: print('no')