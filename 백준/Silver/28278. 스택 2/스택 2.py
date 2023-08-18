import sys
input=sys.stdin.readline
print=sys.stdout.write

if __name__=='__main__':
    stack_=[]
    for _ in range(int(input())):
        q=list(map(int,input().split()))
        if q[0]==1:
            stack_.append(q[1])
        elif q[0]==2:
            if len(stack_):
                print(f'{stack_.pop()}\n')
            else:
                print('-1\n')
        elif q[0]==3:
            print(f'{len(stack_)}\n')
        elif q[0]==4:
            print(f'{int(not stack_)}\n')
        elif q[0]==5:
            if len(stack_):
                print(f'{stack_[-1]}\n')
            else:
                print('-1\n')