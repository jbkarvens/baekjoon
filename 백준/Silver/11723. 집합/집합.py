import sys
input = sys.stdin.readline

S = 0
for _ in range(int(input())):
    query = input().split()
    if query[0] == 'add':
        k = int(query[1])
        S |= 1 << (k - 1)
    elif query[0] == 'remove':
        k = int(query[1])
        S &= ~ (1 << (k - 1))
    elif query[0] == 'check':
        k = int(query[1])
        B = 1 << (k - 1)
        if (S & B) == B:
            print(1)
        else:
            print(0)
    elif query[0] == 'toggle':
        k = int(query[1])
        S ^= 1 << (k - 1)
    elif query[0] == 'all':
        S = (1 << 20) - 1
    elif query[0] == 'empty':
        S = 0