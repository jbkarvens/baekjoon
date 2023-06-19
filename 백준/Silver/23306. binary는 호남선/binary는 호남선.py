import sys
input = sys.stdin.readline
print = sys.stdout.write

if __name__=='__main__':
    N = int(input())
    print('? 1\n')
    sys.stdout.flush()
    a=int(input())
    print(f'? {N}\n')
    sys.stdout.flush()
    b=int(input())
    if a<b:
        ans = 1
    elif a==b:
        ans = 0
    else:
        ans = -1
    print(f'! {ans}\n')
    sys.stdout.flush()